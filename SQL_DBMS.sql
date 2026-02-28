CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    password_hash TEXT NOT NULL,
    role VARCHAR(20) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE soldiers (
    personnel_id VARCHAR(20) PRIMARY KEY,
    service_number VARCHAR(20),
    full_name VARCHAR(100),
    nick_name VARCHAR(50),
    gender VARCHAR(10),
    date_of_birth DATE,
    age INT,
    blood_group VARCHAR(5),
    nationality VARCHAR(50),
    photograph_url TEXT,

    defence_wing VARCHAR(20),
    regiment_or_unit VARCHAR(100),
    rank VARCHAR(50),
    rank_level_code INT,
    joining_date DATE,
    years_of_service INT,
    commission_type VARCHAR(30),
    current_posting_location VARCHAR(100),
    deployment_status VARCHAR(30),
    specialization VARCHAR(100),
    clearance_level VARCHAR(30),

    technical_skills TEXT,
    combat_skills_rating INT,
    weapon_qualification TEXT,
    languages_known TEXT,
    certifications TEXT,
    flight_hours INT,
    sea_hours INT,
    field_missions_count INT,
    last_training_date DATE,

    medical_fitness_status VARCHAR(30),
    bmi FLOAT,
    stress_level_index FLOAT,
    last_medical_checkup DATE,
    injury_history VARCHAR(10),
    psychological_assessment_score FLOAT,
    emergency_contact VARCHAR(15),

    login_attempts INT,
    failed_login_count INT,
    last_login_time TIMESTAMP,
    access_level VARCHAR(30),
    device_used VARCHAR(50),
    suspicious_activity_flag BOOLEAN,
    data_download_volume_mb FLOAT,
    location_access_log VARCHAR(100),

    mission_assigned VARCHAR(50),
    mission_risk_level VARCHAR(20),
    performance_rating FLOAT,
    disciplinary_record VARCHAR(10),
    leave_frequency_days INT,
    overtime_hours FLOAT,
    fatigue_index FLOAT,
    incident_reports_count INT,

    communication_frequency INT,
    social_media_risk_score FLOAT,
    sentiment_score_reports FLOAT,
    financial_stress_flag BOOLEAN,
    peer_feedback_score FLOAT,
    anomaly_score FLOAT,
    overall_risk_level VARCHAR(20)
);

CREATE TABLE cdr_records (
    id SERIAL PRIMARY KEY,
    caller_id VARCHAR(20),
    receiver_id VARCHAR(20),
    call_start_time TIMESTAMP,
    call_duration INT,
    call_type VARCHAR(20),
    tower_id VARCHAR(20),

    imei VARCHAR(30),
    sim_id VARCHAR(30),

    call_frequency INT,

    cell_tower_latitude FLOAT,
    cell_tower_longitude FLOAT,
    area_code VARCHAR(20),

    unique_contacts_count INT,
    time_gap_between_calls INT,
    night_activity_flag BOOLEAN,
    multi_sim_usage_flag BOOLEAN,
    device_change_count INT
);

CREATE TABLE logistics_inventory (
    id SERIAL PRIMARY KEY,
    base_id VARCHAR(50),
    location VARCHAR(100),
    supply_type VARCHAR(50),
    current_stock FLOAT,
    minimum_required FLOAT,
    daily_consumption FLOAT,
    last_supply_date DATE,
    next_expected_supply DATE,
    transport_status VARCHAR(50),
    mission_intensity_level VARCHAR(20)
);

CREATE TABLE legal_frameworks (
    id SERIAL PRIMARY KEY,
    law_name VARCHAR(200),
    jurisdiction VARCHAR(100),
    domain VARCHAR(50),
    description TEXT,
    severity_level INT
);

CREATE TABLE legal_keyword_mapping (
    id SERIAL PRIMARY KEY,
    keyword VARCHAR(100),
    mapped_law_id INT REFERENCES legal_frameworks(id),
    risk_weight FLOAT
);