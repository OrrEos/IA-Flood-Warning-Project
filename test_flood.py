from multiprocessing import dummy
from floodsystem.flood import stations_level_over_threshold, stations_highest_rel_level
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.station import MonitoringStation

#initial stations list & getting updated water levels
stations = build_station_list()
update_water_levels(stations)


#creating dummy stations list

#First Dummy Station
station_id = "station_id 1"
measure_id = "measure_id 1"
label = "station 1"
coord = (1.0, 1.0)
typical_range = (0.2, 0.9)
river = "river 1"
town = "Town 1"

dummyStation1 = MonitoringStation(station_id, measure_id, label, coord, typical_range, river, town)
dummyStation1.latest_level = 1.0

'''#Second Dummy Station
station_id = "station_id 2"
measure_id = "measure_id 2"
label = "station 2"
coord = (2.0, 2.0)
typical_range = (0.5, 1.5)
river = "river 2"
town = "Town 2"

dummyStation2 = MonitoringStation(station_id, measure_id, label, coord, typical_range, river, town)
dummyStation2.latest_level = 2.0

#Third Dummy Station
station_id = "station_id 3"
measure_id = "measure_id 3"
label = "station 3"
coord = (3.0, 3.0)
typical_range = (0.1, 0.3)
river = "river 3"
town = "Town 3"

dummyStation3 = MonitoringStation(station_id, measure_id, label, coord, typical_range, river, town)
dummyStation3.latest_level = 3.0

dummy_stations_list = [dummyStation1, dummyStation2, dummyStation3]'''

#task 2b
def test_stations_level_over_threshold():
    
    tol = 0.8
    out = stations_level_over_threshold(stations, tol)
    #check that list is returned
    assert type(out) == list
    #check that items are tuples
    assert(type(out[0])) == tuple
    #check that relative water level is a float and that station name is a string
    assert type(out[0][1]) == float
    assert type(out[0][0]) == str
    #assert type(out[0][0]) == str
    #check that list is at least of length 1
    assert len(out) >= 1

    #check that they are sorted in descending order of relative water level
    for i in range(len(out) - 1):
        assert out[i][1] >= out[i + 1][1]
        assert out[i][1] >= tol

    #checking that dummyStation1 is above the threshold value    
    dummy_stations_list = [dummyStation1]
    assert stations_level_over_threshold(dummy_stations_list, 0.8) == [('station 1', dummyStation1.relative_water_level())]

#test_stations_level_over_threshold()

#task 2C    

def test_stations_highest_rel_level():
    N = 10
    out = stations_highest_rel_level(stations, N)
    #check that list is returned
    assert type(out) == list
    #check that list of length N
    assert len(out) == N

    #check that items are tuples
    assert(type(out[0])) == tuple
    #check that relative water level is a float and that station name is a string
    assert type(out[0][1]) == float
    assert type(out[0][0]) == str
    

    #assert the list is correctly sorted
    for item in range(len(out) - 1):
        assert out[item][1] >= out[item + 1][1]

#test_stations_highest_rel_level()



    

