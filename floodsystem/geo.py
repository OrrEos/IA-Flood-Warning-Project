# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from .utils import sorted_by_key  # noqa
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
