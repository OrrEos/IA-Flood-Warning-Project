from floodsystem.stationdata import build_station_list, update_water_levels
from Task2G import run


def test_taskG():
    out = run()
    #assert that a list of severe stations is returned
    assert type(out) == list
    #check that the list is correctly ordered from high to low
    for item in range(len(out) - 1):
        assert out[item][1] > out[item + 1][1]

test_taskG()