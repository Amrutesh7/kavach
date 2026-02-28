from sqlalchemy import Column, String, Integer, Float, Date
from database import Base


class Soldier(Base):
    __tablename__ = "soldiers"

    personnel_id = Column("Personnel_ID", String, primary_key=True)
    service_number = Column("Service_Number", String)
    full_name = Column("Full_Name", String)
    nick_name = Column("Nick_Name", String)
    gender = Column("Gender", String)
    date_of_birth = Column("Date_of_Birth", Date)
    age = Column("Age", Integer)
    blood_group = Column("Blood_Group", String)
    nationality = Column("Nationality", String)
    photograph_url = Column("Photograph_URL", String)

    defence_wing = Column("Defence_Wing", String)
    regiment_or_unit = Column("Regiment_or_Unit", String)
    rank = Column("Rank", String)
    rank_level_code = Column("Rank_Level_Code", String)
    joining_date = Column("Joining_Date", Date)
    years_of_service = Column("Years_of_Service", Integer)
    commission_type = Column("Commission_Type", String)
    current_posting_location = Column("Current_Posting_Location", String)
    deployment_status = Column("Deployment_Status", String)
    specialization = Column("Specialization", String)
    clearance_level = Column("Clearance_Level", String)

    certifications = Column("Certifications", String)
    weapon_qualification = Column("Weapon_Qualification", String)

    combat_skills_rating = Column("Combat_Skills_Rating", Float)
    flight_hours = Column("Flight_Hours", Float)
    sea_hours = Column("Sea_Hours", Float)
    field_missions_count = Column("Field_Missions_Count", Integer)
    last_training_date = Column("Last_Training_Date", Date)