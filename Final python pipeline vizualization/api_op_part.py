import json 
import urllib.parse
import requests
from dotenv import load_dotenv
import os


#func for fetching key
def fetch_key(file = "key.env"):
    load_dotenv(file)
    key = os.getenv("my_api_key")
    if(not key):
        raise ValueError("API key not found in the .env file")
    return key


#func to load locations from json file
def load_locations(file = "output.json"):
    with open(file,"r") as f:
        data = json.load(f)
    return data["route"]


#func to get polyline output
def get_polyline(locations , api_key):
    origin = urllib.parse.quote(locations[0])
    destination = urllib.parse.quote(locations[-1])
    waypoints = "|".join([urllib.parse.quote(loc) for loc in locations[1:-1]])

    url = (
        f"https://maps.googleapis.com/maps/api/directions/json"
        f"?origin={origin}&destination={destination}&waypoints={waypoints}&key={api_key}"
    )

    response = requests.get(url)
    data = response.json()

    if data["status"] != "OK":
        raise Exception("Error from Google Directions API:",data["status"])
    
    polyline = data["routes"][0]["overview_polyline"]["points"]
    return polyline


#main func
def main():
    api_key = fetch_key()
    locations = load_locations()
    polyline = get_polyline(locations,api_key)

    with open("polyline_op.json","w") as f:
        json.dump({"polyline" : polyline},f, indent=2)
    
    print("Polyline saved for output")


main()