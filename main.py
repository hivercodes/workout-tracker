import requests



with open("../api/nutritionix") as api_data:
    neutr_api = api_data.readlines()

clean_api = []

for n_line in neutr_api:
    clean_api.append(n_line.strip("\n"))

print(clean_api)

xapp = clean_api[0]
xappkey = clean_api[1]


head = {
    "x-app-id": xapp,
    "x-app-key": xappkey
}


EXERZISE_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"

params =  {
     "query":"ran 3 hours",
     "gender":"female",
     "weight_kg":72.5,
     "height_cm":167.64,
     "age":30
    }


exercise_data = requests.post(url=EXERZISE_ENDPOINT, headers=head, json=params)

exercise_return_data = exercise_data.json

print(exercise_return_data()["exercises"])

activity = exercise_return_data()["exercises"][0]["user_input"]
duration = exercise_return_data()["exercises"][0]["duration_min"]
cals = exercise_return_data()["exercises"][0]["nf_calories"]



print(activity, duration, cals)


