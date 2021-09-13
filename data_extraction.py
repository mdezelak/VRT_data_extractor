import sys
import json
import numpy as np

sys.path.append('../')

from sport_activities_features.hill_identification import HillIdentification
from sport_activities_features.tcx_manipulation import TCXFile
from sport_activities_features.topographic_features import TopographicFeatures
from sport_activities_features.plot_data import PlotData
from datetime import datetime

#read TCX file
tcx_file = TCXFile()
activity  = tcx_file.read_one_file("node.tcx")

#detect hills in data
Hill = HillIdentification(activity['altitudes'], 30)
Hill.identify_hills() 
all_hills = Hill.return_hills()

#extract features from data               
Top = TopographicFeatures(all_hills)

x =  json.loads('{}')
x["num_hills"]      = Top.num_of_hills()
x["avg_altitude"]   = Top.avg_altitude_of_hills(activity['altitudes'])
x["avg_ascent"]     = Top.avg_ascent_of_hills(activity['altitudes'])
x["distance_hills"] = Top.distance_of_hills(activity['positions'])
x["hills_share"]    = Top.share_of_hills(Top.distance_of_hills(activity['positions']), activity['total_distance'])

#time
timestamps = np.array([*activity['timestamps']])
x["duration"]       = datetime.timestamp(timestamps[len(timestamps)-1]) - datetime.timestamp(timestamps[0])
#distnace
x["total_distance"] = activity['total_distance']
#heart_rate
heart_rate = np.array([*activity['heartrates']])
heart_rate = heart_rate[heart_rate != None]
x["avg_heartrate"]  = np.mean(heart_rate)
#average_speed
x["avg_speed"]      = (activity['total_distance'] / x["duration"]) * 3.6
#average_speed
x["ascent"]         = Hill.total_ascent
#forma
x["forma"]          = ((activity['total_distance'] / 1000) + x["avg_speed"]) * ((x["ascent"] / 1000)*0.4)


print(x)
sys.stdout.flush()

