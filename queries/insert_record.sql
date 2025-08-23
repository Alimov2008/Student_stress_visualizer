INSERT INTO stress_data (
    timestamp,
    academic_stage,
    peer_pressure,
    home_academic_pressure,
    study_environment,
    coping_strategy,
    bad_habits,
    academic_competition,
    stress_index
)
VALUES (
    :timestamp,
    :academic_stage,
    :peer_pressure,
    :home_academic_pressure,
    :study_environment,
    :coping_strategy,
    :bad_habits,
    :academic_competition,
    :stress_index
);