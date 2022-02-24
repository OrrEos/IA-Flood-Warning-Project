from floodsystem.flood import stations_level_over_threshold
from floodsystem.stationdata import build_station_list

def run():
    # Build list of stations
    stations = build_station_list()
    ret = stations_level_over_threshold(stations, 0.8)
    print(ret)

run()
