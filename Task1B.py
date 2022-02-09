from floodsystem.geo import stations_by_distance
from floodsystem.stationdata import build_station_list


def run():
    #Task1B Requirements
    stations = build_station_list()
   
    dist = stations_by_distance(stations, (52.2053, 0.1218))
    print("Closest 10 stations")
    print(dist[:10])
    print("Furthest 10 stations")
    print(dist[-10:])


if __name__ == "__main__":
    print("*** Task 1B: Sorting stations by distance ***")
    run()
