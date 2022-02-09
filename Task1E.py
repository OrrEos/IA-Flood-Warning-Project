import floodsystem.geo as geo
from floodsystem.stationdata import build_station_list

def run():
    stations = build_station_list()
    ret = geo.rivers_by_station_number(stations, 10)
