# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from floodsystem.utils import sorted_by_key  # noqa
from haversine import haversine, Unit
from floodsystem.stationdata import build_station_list


#task 1B: list of (station, distance) tuples from coord p 
#sort the list by distance

#required function signature
def stations_by_distance(stations, p):
    #first, a list of all stations
    stations = build_station_list()
    ret = []
    for station in stations:
        distance_p = haversine(p, station.coord)
        a = (station.name, station.town, distance_p)
        ret.append(a)
    return sorted_by_key(ret, 2, reverse=False)
    
#task 1C
def stations_within_radius(stations, centre, r):
    stations = build_station_list()
    ret = []
    for station in stations:
        distance_x = haversine(centre, station.coord)
        if distance_x <= r:
            ret.append(station.name)
    return sorted(ret)

#task 1Da
def rivers_with_station(stations):
    stations = build_station_list()
    rivers = []
    for station in stations:
        rivers.append(station.river)
    return rivers

#task 1Db
"""
def stations_by_river(stations):
    #stations = build_station_list()
    dict = {}
    for station in stations:
        #Check for river in dictionary, and add new item, or append dictionary list.
        if station.river not in dict:
            dict[station.river] = [station.name]

        else: 
            dict[station.river].append(station.name)#add new name to river key

    return dict
"""

#task 1Db
def stations_by_river(stations):
    stations = build_station_list()
    dict = {}
    for station in stations:
        #Check for river in dictionary, and add new item, or append dictionary list.
        if not station.river  in dict:
            dict.update({station.river: list([station.name])})#add new name to river key
        else:
            dict[station.river] = list(dict[station.river])+[station.name]
    return dict

#task 1E
def rivers_by_station_number(stations, N) :
    riverDict = stations_by_river(stations)
    ret = []
    for key, value in riverDict():
        ret.append((key, len(value)))
    #attempting to sort the value of length of the tuple, so that largest number is first.
    ret.sort(ret, key = ret[[1]], reverse = True)
    return ret[:N]




