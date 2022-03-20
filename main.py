import requests
from datetime import datetime

now = datetime.now()
date = now.strftime("%d/%m/%Y")
t = now.strftime("%H:%M:%S")

with open("../api/nutritionix") as api_data:
    neutr_api = api_data.readlines()

clean_api = []

for n_line in neutr_api:
    clean_api.append(n_line.strip("\n"))



xapp = clean_api[0]
xappkey = clean_api[1]


head = {
    "x-app-id": xapp,
    "x-app-key": xappkey
}


EXERZISE_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"

params =  {
     "query":input("What did you do today?:"),
     "gender":"male",
     "weight_kg":110.5,
     "height_cm":187.64,
     "age":35
    }


exercise_data = requests.post(url=EXERZISE_ENDPOINT, headers=head, json=params)

exercise_return_data = exercise_data.json



activity = exercise_return_data()["exercises"][0]["user_input"]
duration = exercise_return_data()["exercises"][0]["duration_min"]
cals = exercise_return_data()["exercises"][0]["nf_calories"]



with open("../api/sheety") as sheety_data:
    sheety_api = sheety_data.readlines()

clean_sheety = []

for n_line in sheety_api:
    clean_sheety.append(n_line.strip("\n"))



data = {
    "sheet1": {

    "date": date,
    "time": t,
    "exercise": activity,
    "duration": duration,
    "calories": cals
}
}

google_sheet = requests.post(url=clean_sheety[3], json=data)


