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
#required function signature
def stations_by_distance(stations, p):
    #first, a list of all stations
    stations = build_station_list()
    ret = []
    for station in stations:
        distance_p = haversine(p, station.coord)#using the imported haversine function to find distance between locations
        a = (station.name, station.town, distance_p)#creating the tuple for each station
        ret.append(a)
    return sorted_by_key(ret, 2, reverse=False)#sorting the list by decreasing distance from p (the 3rd thing in tuple - distance_p)
    
#task 1C
def stations_within_radius(stations, centre, r):
    stations = build_station_list()
    ret = []
    for station in stations:
        distance_x = haversine(centre, station.coord)#distance between centre point & stations
        if distance_x <= r: #if station is close enough to point
            ret.append(station.name)
    return sorted(ret)#sort the list alphabetically

#task 1Da
def rivers_with_station(stations):
    stations = build_station_list()
    rivers = []
    for station in stations:
        rivers.append(station.river)
    return set(rivers)
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


def stations_by_len_river(stations):
    stations = build_station_list()
    dict = {}
    for station in stations:
        #Check for river in dictionary, and add new item, or append dictionary list.
        if not station.river  in dict:
            dict.update({station.river: len(list([station.name]))})#add new name to river key
        else:
            dict[station.river] +=1
    return dict

#task 1E

def rivers_by_station_number(stations, N) :
    riverDict = stations_by_len_river(stations)
    ret = []
    for i in riverDict.items():
        ret.append((i[0],i[1]))
    #attempting to sort the value of length of the tuple, so that largest number is first.
    ret.sort(key = lambda a:a[1], reverse = True)

    #create list of no. of stations
    numberStations = []
    for i in ret:
        numberStations.append(i[1])
    #if the next river after Nth has same no. of stations, include it
    if numberStations[N] == numberStations[N+1]:
        print(ret[:N+1])
    else: #otherwise just print the N riverss
        print(ret[:N])

    
    



