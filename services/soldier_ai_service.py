from models.soldier_model import Soldier

def get_all_soldiers_with_risk(db):
    soldiers = db.query(Soldier).all()

    result = []

    for s in soldiers:
        result.append({
            "personnel_id": s.personnel_id,
            "full_name": s.full_name,
            "defence_wing": s.defence_wing,
            "rank": s.rank,
            "regiment_or_unit": s.regiment_or_unit,
            "current_posting_location": s.current_posting_location,
            "deployment_status": s.deployment_status,
            "clearance_level": s.clearance_level,
            "mission_assigned": s.mission_assigned,
            "performance_rating": s.performance_rating,
            "overall_risk_level": s.overall_risk_level
        })

    return result