import requests
import time
import os
from dotenv import load_dotenv
import json

url = "https://maps.googleapis.com/maps/api/distancematrix/json"


# function for fetching key
def fetch_key(file = "key.env"):
    load_dotenv(file)
    key = os.getenv("my_api_key")
    if(not key):
        raise ValueError("API key not found in the .env file")
    return key


# function to collect locations
def get_locations(file = "locations.txt"):
    with open(file,'r') as f:
        content = [line.strip() for line in f if line.strip()]
        return content
    

# function to create time matrix
def get_time_matrix(locations):
    n = len(locations)
    matrix = [[0]*n for _ in range(n)]
    key = fetch_key()

    for i in range(n):
        origins = locations[i]
        for j in range(n):
            if(i == j):
                matrix[i][j] = 0
                continue
            try:
                dest = locations[j]
                params = { "origins":origins , "destinations":dest , "key":key ,"mode":"driving" }
                response = requests.get(url,params=params)
                data = response.json()
            
                if(data["status"]!="OK" or data["rows"][0]["elements"][0]["status"] != "OK"):
                    raise Exception("API error detected or no route found!")
            
                seconds = data["rows"][0]["elements"][0]["duration"]["value"]
                matrix[i][j] = seconds

                time.sleep(1)
        
            except Exception as e:
                print(f"Error in fetching time from {origins} to {locations[j]}:{e}")
                matrix[i][j]=9999

    return matrix


# function to store locations & matrix in json format
def save_matrix_json(locations , matrix, file="matrix.json"):
    data = { "locations": locations , "matrix":matrix}

    with open(file,"w") as f:
        json.dump(data,f,indent=2)


# main function
def main():
    locations = get_locations()
    matrix = get_time_matrix(locations)
    save_matrix_json(locations,matrix)


main()