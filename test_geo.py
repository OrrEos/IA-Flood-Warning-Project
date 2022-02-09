from floodsystem.geo import stations_by_distance, stations_within_radius, rivers_with_station
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
        #checking first value
        assert out[0] == 'Bin Brook'
        #checking length of list
        assert len(out) == 11

    



    

    