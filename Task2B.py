from floodsystem.flood import stations_level_over_threshold
from floodsystem.stationdata import build_station_list, update_water_levels

def run():
    # Build list of stations
    stations = build_station_list()
    update_water_levels(stations)
    ret = stations_level_over_threshold(stations, 0.8)
    for i in range(len(ret)):
        print("{} {}".format(ret[i][0], ret[i][1]))
    #print(ret)

run()

