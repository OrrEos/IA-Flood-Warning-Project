from floodsystem.flood import stations_level_over_threshold, stations_highest_rel_level
from floodsystem.stationdata import build_station_list, update_water_levels

def run():
    # Build list of stations
    stations = build_station_list()
    update_water_levels(stations)

    ret = stations_highest_rel_level(stations, 10)
    #print(ret)
    print("**Stations with highest relative water level:**")
    for i in range(len(ret)):
        print("{} {}".format(ret[i][0], ret[i][1]))

run()