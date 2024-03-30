import sys
from fastapi.testclient import TestClient

sys.path.append("..")

from main import app

client = TestClient(app, base_url="http://localhost:8000")

def test_health_check():
    response = client.get("/")
    assert response.status_code == 200
  
def test_get_listings():
    headers = {"accept": "application/json"}
    response = client.get("/listings", headers=headers)
    print(response)
    assert response.status_code == 200

def test_get_apartments_according_user_pref():
    test_data = {"min_price": 100000,"max_price": 150000,"min_sqft_lot": 1000}
    response = client.post("/search", json=test_data)
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_add_new_apartment():
    test_data = {"address": "new adress","price": 123123,"year_built": 1990,"sqft": 1050,"beds": 1,
                 "bathrooms": 1,"price_per_sqft": 150,"property_type": "house","garage": 2,"HOA_fees": 150,"sqft_lot": 1000}
    response = client.post("/add-listing", json=test_data)
    assert response.status_code == 200
