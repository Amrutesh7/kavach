import os
import sys
import pandas as pd

# ----------------------------
# Fix Python path
# ----------------------------
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

# ----------------------------
# Imports
# ----------------------------
from database import SessionLocal
from models.soldier_model import Soldier

# ----------------------------
# Excel file path
# ----------------------------
EXCEL_PATH = os.path.join(BASE_DIR, "utils", "soldierdata.xlsx")


# ----------------------------
# Helpers
# ----------------------------
def clean_boolean(value):
    if str(value).strip().lower() in ["1", "true", "yes"]:
        return True
    return False


def to_string(value):
    if pd.isna(value):
        return None
    return str(value).strip()


# ----------------------------
# Main import function
# ----------------------------
def import_soldiers():

    if not os.path.exists(EXCEL_PATH):
        print(f"❌ Excel file not found at: {EXCEL_PATH}")
        return

    print(f"📂 Reading file from: {EXCEL_PATH}")

    df = pd.read_excel(EXCEL_PATH)

    # Normalize column names
    df.columns = [col.strip().lower() for col in df.columns]

    db = SessionLocal()

    try:
        for _, row in df.iterrows():

            # 🔥 FORCE personnel_id to STRING
            personnel_id_value = to_string(row.get("personnel_id"))

            if personnel_id_value is None:
                continue

            # Duplicate check (STRING comparison)
            existing = db.query(Soldier).filter(
                Soldier.personnel_id == personnel_id_value
            ).first()

            if existing:
                continue

            soldier = Soldier(
                personnel_id=personnel_id_value,
                service_number=to_string(row.get("service_number")),
                full_name=to_string(row.get("full_name")),
                nick_name=to_string(row.get("nick_name")),
                gender=to_string(row.get("gender")),
                date_of_birth=row.get("date_of_birth"),
                age=row.get("age"),
                blood_group=to_string(row.get("blood_group")),
                nationality=to_string(row.get("nationality")),
                photograph_url=to_string(row.get("photograph_url")),

                defence_wing=to_string(row.get("defence_wing")),
                regiment_or_unit=to_string(row.get("regiment_or_unit")),
                rank=to_string(row.get("rank")),
                rank_level_code=to_string(row.get("rank_level_code")),
                joining_date=row.get("joining_date"),
                years_of_service=row.get("years_of_service"),
                commission_type=to_string(row.get("commission_type")),
                current_posting_location=to_string(row.get("current_posting_location")),
                deployment_status=to_string(row.get("deployment_status")),
                specialization=to_string(row.get("specialization")),
                clearance_level=to_string(row.get("clearance_level")),

                technical_skills=to_string(row.get("technical_skills")),
                combat_skills_rating=row.get("combat_skills_rating"),
                weapon_qualification=to_string(row.get("weapon_qualification")),
                languages_known=to_string(row.get("languages_known")),
                certifications=to_string(row.get("certifications")),
                flight_hours=row.get("flight_hours"),
                sea_hours=row.get("sea_hours"),
                field_missions_count=row.get("field_missions_count"),
                last_training_date=row.get("last_training_date"),

                medical_fitness_status=to_string(row.get("medical_fitness_status")),
                bmi=row.get("bmi"),
                stress_level_index=row.get("stress_level_index"),
                last_medical_checkup=row.get("last_medical_checkup"),
                injury_history=to_string(row.get("injury_history")),
                psychological_assessment_score=row.get("psychological_assessment_score"),
                emergency_contact=to_string(row.get("emergency_contact")),

                login_attempts=row.get("login_attempts"),
                failed_login_count=row.get("failed_login_count"),
                last_login_time=row.get("last_login_time"),
                access_level=to_string(row.get("access_level")),
                device_used=to_string(row.get("device_used")),
                suspicious_activity_flag=clean_boolean(row.get("suspicious_activity_flag")),
                data_download_volume_mb=row.get("data_download_volume_mb"),
                location_access_log=to_string(row.get("location_access_log")),

                mission_assigned=to_string(row.get("mission_assigned")),
                mission_risk_level=to_string(row.get("mission_risk_level")),
                performance_rating=row.get("performance_rating"),
                disciplinary_record=to_string(row.get("disciplinary_record")),
                leave_frequency_days=row.get("leave_frequency_days"),
                overtime_hours=row.get("overtime_hours"),
                fatigue_index=row.get("fatigue_index"),
                incident_reports_count=row.get("incident_reports_count"),

                communication_frequency=row.get("communication_frequency"),
                social_media_risk_score=row.get("social_media_risk_score"),
                sentiment_score_reports=row.get("sentiment_score_reports"),
                financial_stress_flag=clean_boolean(row.get("financial_stress_flag")),
                peer_feedback_score=row.get("peer_feedback_score"),
                anomaly_score=row.get("anomaly_score"),
                overall_risk_level=to_string(row.get("overall_risk_level")),
            )

            db.add(soldier)

        db.commit()
        print("✅ Soldier data imported successfully!")

    except Exception as e:
        db.rollback()
        print("❌ Error occurred:", e)

    finally:
        db.close()


if __name__ == "__main__":
    import_soldiers()