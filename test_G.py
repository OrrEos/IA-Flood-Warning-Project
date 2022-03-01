from floodsystem.stationdata import build_station_list, update_water_levels
from Task2G import run


def test_taskG():
    out = run()
    #assert that a list of severe stations is returned
    #assert type(out) == str
    #assert that it's a list of tuples
    #assert type(out[0]) == tuple
    #check that the list is correctly ordered from high to low
    #for item in range(len(out) - 1):
        #assert out[item][1] > out[item + 1][1]

