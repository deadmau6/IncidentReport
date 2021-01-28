from fastapi.testclient import TestClient
from ..main import app

client = TestClient(app)

# Tests for GET query_incident_by_id
#################################
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

##################################
# Tests for POST query_incidents
##################################
def test_query_incidents_valid():
    valid = {"address": {"city": "Richmond","state": "VA"}}
    response = client.post("/incidents/", json=valid)
    assert response.status_code == 200
    result = response.json()
    assert len(result['results']) >= 2

def test_query_incidents_bad():
    valid = {"address": {"city": 24,"state": 25}}
    response = client.post("/incidents/", json=valid)
    assert response.status_code == 404

def test_query_incidents_no():
    valid = None
    response = client.post("/incidents/", json=valid)
    assert response.status_code == 200
    result = response.json()
    assert len(result['results']) >= 2

def test_query_incident_crazy():
    valid = {"address": {"cities": ["Richmond"],"state": "VA"}}
    response = client.post("/incidents/", json=valid)
    assert response.status_code == 200
    result = response.json()
    assert len(result['results']) >= 2

##################################
# Tests for GET query_incidents_by_address
##################################
def test_query_incidents_by_address_valid():
    valid = f"/incidents/address/?city=Richmond&state=VA"
    response = client.get(valid)
    assert response.status_code == 200
    result = response.json()
    assert len(result['results']) >= 2

def test_query_incidents_by_address_bad():
    valid = f"/incidents/address/?city=24&state=25"
    response = client.get(valid)
    assert response.status_code == 404

def test_query_incidents_by_address_no():
    valid = f"/incidents/address/"
    response = client.get(valid)
    assert response.status_code == 200
    result = response.json()
    assert len(result['results']) >= 2

def test_query_incident_by_address_crazy():
    valid = f"/incidents/address/?cities=richmond&state=VA"
    response = client.get(valid)
    assert response.status_code == 200
    result = response.json()
    assert len(result['results']) >= 2

##################################
# Tests for GET query_incidents_by_description
##################################
def test_query_incidents_by_description_valid():
    valid = f"/incidents/description/?day_of_week=Monday"
    response = client.get(valid)
    assert response.status_code == 200
    result = response.json()
    assert len(result['results']) >= 2

def test_query_incidents_by_description_bad():
    valid = f"/incidents/description/?day_of_week=80&response_time=Monday"
    response = client.get(valid)
    assert response.status_code == 404

def test_query_incidents_by_description_no():
    valid = f"/incidents/description/"
    response = client.get(valid)
    assert response.status_code == 200
    result = response.json()
    assert len(result['results']) >= 2

def test_query_incident_by_description_crazy():
    valid = f"/incidents/description/?cities=richmond&state=VA"
    response = client.get(valid)
    assert response.status_code == 200
    result = response.json()
    assert len(result['results']) >= 2