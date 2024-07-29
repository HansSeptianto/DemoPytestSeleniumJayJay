import requests
from helper.config import *


def push_result(case_id, status):
    payload = {
        "case_id": case_id,
        "status": status
    }
    head = {
        "accept": "application/json",
        "content-type": "application/json",
        "Token": api_key_qase
    }
    resp = requests.post(f"{host_qase}{project_code_qase}/{test_run_qase}", json=payload, headers=head)
