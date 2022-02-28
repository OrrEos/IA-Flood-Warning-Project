from .station import MonitoringStation

def stations_level_over_threshold(stations, tol):
    ret = []
    for station in stations:
        if MonitoringStation.typical_range_consistent(station) and not(MonitoringStation.relative_water_level(station) ==None):
            if MonitoringStation.relative_water_level(station) >tol:
                ret.append((station, MonitoringStation.relative_water_level(station)))
    return ret.sort(key = lambda a:a[1], reverse = True)

