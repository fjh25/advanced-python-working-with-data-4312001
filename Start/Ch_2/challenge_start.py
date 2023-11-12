# Example file for Advanced Python: Working With Data by Joe Marini
# Programming challenge: use advanced data collections on the earthquake data

import json
from collections import defaultdict


# open the data file and load the JSON
with open("../../30DayQuakes.json", "r") as datafile:
    data = json.load(datafile)


quake_type_counter = defaultdict(int)

for q in data["features"]:
    q_type = q["properties"]["type"]
    quake_type_counter[q_type] += 1 

for k,v  in quake_type_counter.items():
    print(f"{k:<20}:  {v}")