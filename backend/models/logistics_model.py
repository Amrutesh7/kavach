from sqlalchemy import Column, String, Float, Date
from database import Base


class LogisticsInventory(Base):
    __tablename__ = "logistics_inventory"

    base_id = Column("Base_ID", String(50), primary_key=True)
    supply_type = Column("Supply_Type", String(50), primary_key=True)

    location = Column("Location", String(100))
    current_stock = Column("Current_Stock", Float)
    minimum_required = Column("Minimum_Required", Float)
    daily_consumption = Column("Daily_Consumption", Float)
    last_supply_date = Column("Last_Supply_Date", Date)
    next_expected_supply = Column("Next_Expected_Supply", Date)
    transport_status = Column("Transport_Status", String(50))
    mission_intensity_level = Column("Mission_Intensity_Level", String(20))