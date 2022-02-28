from floodsystem.flood import stations_level_over_threshold
from floodsystem.stationdata import build_station_list
def test_stations_level_over_threshold():
    stations = build_station_list()
    tol = 0.8
    out = stations_level_over_threshold(stations, tol)
    #check that list is returned
    assert type(out) == list
    #check that items are tuples
    assert type(out[0]) == tuple
    #check that they are sorted in descending order of relative water level

def test_stations_level_over_threshold():
    stations = build_station_list()
    

