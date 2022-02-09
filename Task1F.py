from floodsystem.station import inconsistent_typical_range_stations
from floodsystem.stationdata import build_station_list


def run():
    stations = build_station_list()
    print(inconsistent_typical_range_stations(stations))
run()
