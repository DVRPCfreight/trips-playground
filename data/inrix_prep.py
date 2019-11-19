import csv
import json

trip_matches = 0

matches = []


with open('C:/Temp/trips.csv') as csv_file:
    trips = csv.reader(csv_file, delimiter=',')
    for i, trip in enumerate(trips):
        paths = []
        timestamps = []
        if trip[17] != '1':
            trip_matches = trip[0]           
            with open('C:\Temp\waypoints.csv') as waypointfile:
                waypoints = csv.reader(waypointfile, delimiter=',') 
                waypointfile.seek(0)  
                for waypoint in waypoints:
                    if waypoint[0] == trip_matches:
                        paths.append([waypoint[4], waypoint[3]])
                        timestamps.append(waypoint[2])
                new = json.dumps({'vendor' : trip[17]})
                # , {"path" : paths}, {"timestamps" : timestamps}})
                print (new)
                # print (json.dumps(matches))


