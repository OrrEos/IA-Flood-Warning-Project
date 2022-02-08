
from floodsystem.geo import stations_by_river
from floodsystem.stationdata import build_station_list


def run2():
    #part 2: dictionary of rivers: stations
    stations = build_station_list
    RiverDict = stations_by_river(stations)

   # for item in RiverDict:
        #if item in ['River Aire', 'River Cam', 'River Thames'] :
           # print("Key : {} , Value : {}".format(item,RiverDict[item]))

    print(sorted(RiverDict['River Aire']))
    print(sorted(RiverDict['River Cam']))
    print(sorted(RiverDict['River Thames']))


run2()