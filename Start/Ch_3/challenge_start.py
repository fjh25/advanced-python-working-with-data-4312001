# Example file for Advanced Python: Working With Data by Joe Marini
# Programming challenge: use advanced data collections on the earthquake data

import json
import csv
import datetime
import sys
import pprint

# open the data file and load the JSON
with open("../../30DayQuakes.json", "r") as datafile:
    data = json.load(datafile)

# Create a CSV file with the following information:
# 40 most significant seismic events, ordered by most recent
# Header row: Magnitude, Place, Felt Reports, Date, and Google Map link
# Date should be in the format of YYYY-MM-DD


# google link format: https://google.com/maps/search/?api=1&query=<2nd-number>,<first-number> 
header = [ "Magnitude", "Place", "Felt Reports", "Date", "Google Map Link"]
rows = []

def getsig(q):
    if q["properties"]["sig"] is None:
        return 0
    return q["properties"]["sig"]

data["features"].sort(key=getsig, reverse=True)


# Get the 40 most significant events
for i in range(0,40):
    quake = data['features'][i]
    lat = quake['geometry']['coordinates'][0]
    lon = quake['geometry']['coordinates'][1]

    lon_lat_string = f"{str(lon)},{str(lat)}"
    google_link = f"https://google.com/maps/search/?api=1&query={lon_lat_string}"
    thedate = str(datetime.date.fromtimestamp(int(quake["properties"]["time"]/1000)))


    rows.append([quake['properties']['mag'], 
                quake['properties']['place'], 
                quake['properties']['felt'], 
                thedate, 
                google_link])

def get_date(data_item):
    return data_item[3]

rows.sort(key=get_date, reverse=True)
pprint.pp(rows)


with open("40most_sig_events.csv", "w") as csvfile:
    writer = csv.writer(csvfile, delimiter=",")
    writer.writerow(header)
    writer.writerows(rows)


#rows =  [  [],  [], [] ]
#        "date": str(datetime.date.fromtimestamp(
#            int(q["properties"]["time"]/1000)))

#def getmag(dataitem):
#    magnitude = dataitem["properties"]["mag"]
#    if (magnitude is None):
#        magnitude = 0
#    return float(magnitude)
#
#data['features'].sort(key=getmag, reverse=True)