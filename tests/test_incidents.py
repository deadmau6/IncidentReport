from fastapi.testclient import TestClient
from ..main import app

client = TestClient(app)

def test_query_incident_valid_id():
    valid_number = 'F01705150090' 
    response = client.get(f"/incident/{valid_number}")
    assert response.status_code == 200

def test_query_incident_bad_id():
    valid_number = '001' 
    response = client.get(f"/incident/{valid_number}")
    assert response.status_code == 404

def test_query_incident_no_id():
    valid_number = None
    response = client.get(f"/incident/{valid_number}")
    assert response.status_code == 404

def test_query_incident_crazy_id():
    valid_number = 21
    response = client.get(f"/incident/{valid_number}")
    assert response.status_code == 404