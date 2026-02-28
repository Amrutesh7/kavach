from sqlalchemy.orm import Session
from models.logistics_model import LogisticsInventory
from datetime import date


def analyze_logistics(db: Session):
    records = db.query(LogisticsInventory).all()

    if not records:
        return {"message": "No logistics data available"}

    results = []

    today = date.today()

    for record in records:

        # Days until next supply
        if record.next_expected_supply:
            days_remaining = (record.next_expected_supply - today).days
            days_remaining = max(days_remaining, 0)
        else:
            days_remaining = 0

        predicted_stock = record.current_stock - (
            record.daily_consumption * days_remaining
        )

        # Avoid division by zero
        if record.minimum_required and record.minimum_required > 0:
            stock_ratio = predicted_stock / record.minimum_required
        else:
            stock_ratio = 0

        # Risk classification
        if stock_ratio >= 1.2:
            risk = "LOW"
        elif stock_ratio >= 0.8:
            risk = "MEDIUM"
        else:
            risk = "HIGH"

        readiness_index = round(min(max(stock_ratio, 0), 2), 2)

        results.append({
            "base_id": record.base_id,
            "location": record.location,
            "supply_type": record.supply_type,
            "current_stock": record.current_stock,
            "predicted_stock": round(predicted_stock, 2),
            "minimum_required": record.minimum_required,
            "days_until_supply": days_remaining,
            "readiness_index": readiness_index,
            "risk_level": risk
        })

    return results