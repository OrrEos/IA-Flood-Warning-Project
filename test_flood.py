from floodsystem.flood import stations_level_over_threshold, stations_highest_rel_level
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.station import MonitoringStation

#task 2b
def test_stations_level_over_threshold():
    stations = build_station_list()
    tol = 0.8
    out = stations_level_over_threshold(stations, tol)
    #check that list is returned
    assert type(out) == list
    #check that items are tuples
    #assert type(out[0]) == tuple
    #check that relative water level is a float and that station name is a string
    #for i in out:
    #    assert type(i[0]) == str
    #    assert type(i[1]) == float
    #assert type(out[0][0]) == str
    #check that list is at least of length 1
    #assert len(out) >= 1
    #check that they are sorted in descending order of relative water level
    for i in range(len(out) - 1):
        assert out[i][1] >= out[i + 1][1]
        assert out[i][1] >= tol

test_stations_level_over_threshold()

#task 2C    

def test_stations_highest_rel_level():
    stations = build_station_list()
    N = 10
    out = stations_highest_rel_level(stations, N)
    #check that list is returned
    assert type(out) == list
    #check that list of length N
    #assert len(out) == N
    #assert the list is correctly sorted
    for item in range(len(out) - 1):
        assert out[item].relative_water_level() > out[item + 1].relative_water_level()

test_stations_highest_rel_level()



    

