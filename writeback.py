from google.cloud import bigquery
from datetime import date
import json


##fill in path to SA JSON key
my_json_key = ""

def healthcare_prediction(request):
    client = bigquery.Client.from_service_account_json(
        my_json_key)
    request_json = request.get_json(silent=True)
    print("request_json: ", request_json)
    # check to make sure all params are filled
    patient_id = request_json["data"]["patient_id"]
    # first_name = request_json["form_params"]["First Name"]
    # last_name = request_json["form_params"]["Last Name"]
    age_tier = request_json["form_params"]["Age Tier"]
    gender = request_json["form_params"]["Gender"]
    race = request_json["form_params"]["Race"]
    wellness_screened = request_json["form_params"]["Wellness Screened in the Past Year"]
    # city = request_json["form_params"]["City"]
    state = request_json["form_params"]["State"]
    encounter_type = request_json["form_params"]["Encounter Type"]
    procedure_type = request_json["form_params"]["Procedure Type"]
    practictioner_investigator = request_json["form_params"]["Practictioner Examiner"]
    length_of_stay = request_json["form_params"]["Length of Stay"]
    admission_date = request_json["form_params"]["Admission Date"]
    discharge_date = request_json["form_params"]["Discharge Date"]
    last_discharge_date = request_json["form_params"]["Last Discharge Date"]
    curr_date = date.today()
    # insert record into sql table
    sql_string = f"""
        INSERT INTO
        looker-private-demo.healthcare_demo_live.new_patient_visits(
            patient_id,
            patient_name,
            patient_age_tier__sort_,
            patient_age_tier,
            patient_us_core_ethnicity,
            patient_gender,
            patient_us_core_race,
            patient_is_wellness_screened_in_the_past_year,
            patient_birth_place__city,
            patient_birth_place__state,
            encounter_type_coding_display,
            observation__category__coding_display,
            practitioner_investigator,
            encounter_length_of_stay,
            admission_date,
            discharge_date,
            last_discharge_date
        )
        VALUES (
            '0fd0ae11-7a98-4b18-8246-b41fd3cbd38a',
            'Chong Torp',
            "4",
            '{age_tier}',
            "White",
            '{gender}',
            '{race}',
            '{wellness_screened}',
            'Beverly',
            '{state}',
            '{encounter_type}',
            '{procedure_type}',
            '{practictioner_investigator}',
            CAST('{length_of_stay}' as INT64),
            DATE('{curr_date}),
            DATE('{discharge_date}'),
            DATE('{last_discharge_date}')
        )
        """
    query_job = client.query(sql_string)
    results = query_job.result()

    return (json.dumps({
        "looker": {
            "success": True,
            "refresh_query": True
        }
    }), 200)
