import requests
import json
from .models import CarDealer
from requests.auth import HTTPBasicAuth

# Function to make HTTP GET requests
def get_request(url, **kwargs):
    print(kwargs)
    print("GET from {} ".format(url))
    try:
        response = requests.get(url, headers={'Content-Type': 'application/json'}, params=kwargs)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print("Network exception occurred:", e)
        return None
    status_code = response.status_code
    print("With status {} ".format(status_code))
    json_data = json.loads(response.text)
    return json_data

# Function to make HTTP POST requests
def post_request(url, **kwargs):
    print(kwargs)
    print("POST to {} ".format(url))
    try:
        response = requests.post(url, headers={'Content-Type': 'application/json'}, json=kwargs)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print("Network exception occurred:", e)
        return None
    status_code = response.status_code
    print("With status {} ".format(status_code))
    json_data = json.loads(response.text)
    return json_data

# Function to get dealers from a cloud function
def get_dealers_from_cf(url, **kwargs):
    results = []
    json_result = get_request(url)
    if json_result:
        dealers = json_result
        for dealer in dealers:
            dealer_doc = dealer
            dealer_obj = CarDealer(address=dealer_doc["address"], city=dealer_doc["city"], full_name=dealer_doc["full_name"],
                                   id=dealer_doc["id"], lat=dealer_doc["lat"], long=dealer_doc["long"],
                                   short_name=dealer_doc["short_name"],
                                   st=dealer_doc["st"], zip=dealer_doc["zip"])
            results.append(dealer_obj)
    return results

# Function to get dealer reviews by dealer id from a cloud function
def get_dealer_reviews_from_cf(url, dealerId):
    return get_request(url, dealerId=dealerId)

# Function to analyze review sentiments using Watson NLU
def analyze_review_sentiments(text):
    pass  # Placeholder for implementation



