from sqlalchemy import Column, String, Float, Boolean, TIMESTAMP, Integer
from database import Base

class CDRRecord(Base):
    __tablename__ = "cdr_records"

    caller_id = Column(String(20), primary_key=True)
    receiver_id = Column(String(20), primary_key=True)
    call_start_time = Column(TIMESTAMP, primary_key=True)

    call_duration = Column(Integer)
    call_type = Column(String(20))
    tower_id = Column(String(20))

    imei = Column(String(30))
    sim_id = Column(String(30))

    call_frequency = Column(Integer)

    cell_tower_latitude = Column(Float)
    cell_tower_longitude = Column(Float)
    area_code = Column(String(20))

    unique_contacts_count = Column(Integer)
    time_gap_between_calls = Column(Integer)
    night_activity_flag = Column(Boolean)
    multi_sim_usage_flag = Column(Boolean)
    device_change_count = Column(Integer)