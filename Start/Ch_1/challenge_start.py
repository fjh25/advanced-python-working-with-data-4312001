# Example file for Advanced Python: Working With Data by Joe Marini
# Programming challenge: summarize the earthquake data

import json


# for this challenge, we're going to summarize the earthquake data as follows:
# 1: How many quakes are there in total?
# 2: How many quakes were felt by at least 100 people?
# 3: Print the name of the place whose quake was felt by the most people, with the # of reports
# 4: Print the top 10 most significant events, with the significance value of each

# open the data file and load the JSON
with open("../../30DayQuakes.json", "r") as datafile:
    data = json.load(datafile)
    

# 1: How many quakes are there in total?
def is_earthquake(q):
    if q["properties"]["type"] == "earthquake":
        return True
    else:
        return False


num_earthquakes = list(filter(is_earthquake, data["features"]))

print(f"Total earthquakes: {len(num_earthquakes)}")
print(f"Total quakes: {len(data['features'])}")



# 2: How many quakes were felt by at least 100 people?
#quakes_felt_100 = list(( quake["properties"]["felt"] is not None and quake["properties"]["felt"] >= 100  for quake in data["features"]))
#print(f" Total quakes felt by at least 100 people: {len(quakes_felt_100)}")
quakes_felt_100 = sum( quake["properties"]["felt"] is not None and quake["properties"]["felt"] >= 100  for quake in data["features"])
#print(f" Total quakes felt by at least 100 people: {len(quakes_felt_100)}")
print(f"Total quakes felt by at least 100 people: {quakes_felt_100}")



# 3: Print the name of the place whose quake was felt by the most people, with the # of reports
def getfelt(q):
    if q["properties"]["felt"] is None:
        return 0
    return q["properties"]["felt"]

data["features"].sort(key=getfelt, reverse=True)
print(f"Most felt reports: {data['features'][0]['properties']['place']}  reports: {data['features'][0]['properties']['felt']}")

# 4: Print the top 10 most significant events, with the significance value of each
def getsig(q):
    if q["properties"]["sig"] is None:
        return 0
    return q["properties"]["sig"]

data["features"].sort(key=getsig, reverse=True)

print("The 10 most significant events were:")
for i in range(0,10):
    print(f"Event: {data['features'][i]['properties']['place']},  Significance: {data['features'][i]['properties']['sig']}")