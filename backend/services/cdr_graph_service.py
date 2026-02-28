import networkx as nx
from sqlalchemy.orm import Session
from models.cdr_model import CDRRecord
from collections import defaultdict
from datetime import time


def analyze_cdr_network(db: Session):
    records = db.query(CDRRecord).all()

    if not records:
        return {"message": "No CDR data available"}

    G = nx.DiGraph()

    imei_sim_map = defaultdict(set)
    sim_imei_map = defaultdict(set)
    short_call_counter = defaultdict(int)
    night_activity_counter = defaultdict(int)

    # ----------------------------
    # Build graph + track behavior
    # ----------------------------
    for record in records:

        caller = record.caller_id
        receiver = record.receiver_id

        G.add_edge(caller, receiver, weight=record.call_duration or 1)

        # Track SIM-IMEI relationships
        if record.imei and record.sim_id:
            imei_sim_map[record.imei].add(record.sim_id)
            sim_imei_map[record.sim_id].add(record.imei)

        # Short call burst detection (<10 sec)
        if record.call_duration and record.call_duration < 10:
            short_call_counter[caller] += 1

        # Night activity detection (12 AM – 5 AM)
        if record.call_start_time:
            call_time = record.call_start_time.time()
            if time(0, 0) <= call_time <= time(5, 0):
                night_activity_counter[caller] += 1

    # ----------------------------
    # Graph centrality measures
    # ----------------------------
    degree_centrality = nx.degree_centrality(G)
    betweenness = nx.betweenness_centrality(G)

    results = []

    # ----------------------------
    # Suspicion Scoring
    # ----------------------------
    for node in G.nodes:

        degree_score = degree_centrality.get(node, 0)
        between_score = betweenness.get(node, 0)

        # Behavioral flags
        sim_swap_flag = any(len(sims) > 2 for sims in imei_sim_map.values())
        device_switch_flag = any(len(imeis) > 2 for imeis in sim_imei_map.values())

        # Weighted behavioral scores
        sim_swap_score = 0.1 if sim_swap_flag else 0
        device_switch_score = 0.1 if device_switch_flag else 0
        burst_score = 0.1 if short_call_counter[node] > 5 else 0
        night_score = 0.05 if night_activity_counter[node] > 3 else 0

        suspicion_score = (
            0.4 * degree_score +
            0.3 * between_score +
            sim_swap_score +
            device_switch_score +
            burst_score +
            night_score
        )

        # Risk classification
        if suspicion_score < 0.15:
            risk = "LOW"
        elif suspicion_score < 0.35:
            risk = "MEDIUM"
        else:
            risk = "HIGH"

        results.append({
            "phone_number": node,
            "degree_centrality": round(degree_score, 4),
            "betweenness": round(between_score, 4),
            "short_call_bursts": short_call_counter[node],
            "night_activity_calls": night_activity_counter[node],
            "suspicion_score": round(suspicion_score, 4),
            "risk_level": risk
        })

    # Sort by suspicion score
    results = sorted(results, key=lambda x: x["suspicion_score"], reverse=True)

    return results[:20]