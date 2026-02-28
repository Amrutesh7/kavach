from sqlalchemy.orm import Session
from services.soldier_ai_service import get_all_soldiers_with_risk
from services.cdr_graph_service import analyze_cdr_network
from services.logistics_service import analyze_logistics


def generate_intelligence_report(db: Session):

    # Fetch module outputs
    soldier_data = get_all_soldiers_with_risk(db)
    cdr_data = analyze_cdr_network(db)
    logistics_data = analyze_logistics(db)

    # Count high-risk soldiers
    high_risk_soldiers = [
        s for s in soldier_data
        if s["dynamic_risk_level"] == "HIGH"
    ]

    # Count high-risk phone numbers
    high_risk_cdr = [
        c for c in cdr_data
        if c["risk_level"] == "HIGH"
    ]

    # Count logistics high risk
    high_risk_logistics = [
        l for l in logistics_data
        if l["risk_level"] == "HIGH"
    ]

    overall_threat_score = (
        len(high_risk_soldiers) * 1.5 +
        len(high_risk_cdr) * 2 +
        len(high_risk_logistics) * 1
    )

    if overall_threat_score < 5:
        overall_status = "STABLE"
    elif overall_threat_score < 15:
        overall_status = "ELEVATED RISK"
    else:
        overall_status = "CRITICAL THREAT LEVEL"

    return {
        "summary": {
            "high_risk_soldiers": len(high_risk_soldiers),
            "high_risk_communications": len(high_risk_cdr),
            "high_risk_supply_units": len(high_risk_logistics),
            "overall_threat_score": overall_threat_score,
            "overall_status": overall_status
        },
        "top_high_risk_soldiers": high_risk_soldiers[:5],
        "top_suspicious_communications": high_risk_cdr[:5],
        "critical_supply_alerts": high_risk_logistics[:5]
    }