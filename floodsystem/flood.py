from .station import MonitoringStation

def stations_level_over_threshold(stations, tol):
    ret = []
    for station in stations:
        if station.typical_range_consistent() and not(station.relative_water_level() ==None):
            if station.relative_water_level() >tol:
                ret.append[(station, station.relative_water_level())]
        else:
            return None
    return ret.sort(key = lambda a:a[1], reverse = True)

