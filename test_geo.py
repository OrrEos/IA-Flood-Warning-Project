from floodsystem.geo import stations_by_distance, stations_within_radius, rivers_with_station, stations_by_river
from floodsystem.station import inconsistent_typical_range_stations
from floodsystem.stationdata import build_station_list

'''def test_geo():
    #Task 1A
    
    #does the function give an output & if it's a list:
    out = build_station_list()
    assert type(out) == list
    #checking that list is a reasonable length
    assert len(out) >1700
    assert len(out) <2500'''



    #Task 1B
def test_stations_by_distance():
    stations = build_station_list()
    p = (52.2053, 0.1218)#putting in Cambridge value from task
    out = stations_by_distance(stations, p)
    #check that list is returned
    assert type(out) == list
    #check that items are tuples
    assert type(out[0]) == tuple
    #check that first station is Jesus Lock
    assert out[0] == ('Cambridge Jesus Lock', 'Cambridge', 0.840237595667494)
    #check that furthest station is Penberth
    assert out[-1] == ('Penberth', 'Penberth', 467.53431870130544)
    
    #Task 1C
def test_stations_within_radius():
        stations = build_station_list()
        out = stations_within_radius(stations, (52.2053, 0.1218), 10)
        #check that list is returned
        assert type(out) == list
        #checking first value, which is checking the sorting, too
        assert out[0] == 'Bin Brook'
        #checking length of list
        assert len(out) == 11
#Task 1D
def test_rivers_with_station():
    stations = build_station_list()
    out = rivers_with_station(stations)
    #check that out is a set
    assert type(out) == set
    #check that each item in list is a string
    out = list(out)
    assert type(out[0]) == str
    #check that out is of a reasonable length - no. of stations might change in the future?
    assert len(out) > 900
    assert len(out) < 1000
    #checking for duplicates
    #if set(out) is shorter than list (out), then there are duplicates
    assert len(out) == len(set(out))

def test_stations_by_rivers():
    stations = build_station_list
    out = stations_by_river(stations)
    #check that output is a dictionary
    assert type(out) == dict
    #check number of stations listed for Aire:
    aire = out['River Aire']
    assert len(aire) ==24
    #check that it's a list
    assert type(out['River Thames']) == list




#Task1E








    



    

    