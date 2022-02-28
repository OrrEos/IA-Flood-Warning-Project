from .station import MonitoringStation

def stations_level_over_threshold(stations, tol):
    ret = []
    for station in stations:
        #if station has consistent low/high data 
       if station.typical_range_consistent() != False:
            #print("typical range correct")
            #if there is a value for the relative water level
            if  type(station.relative_water_level()) == float:
                #print("type correct")
                #if the latest relative water level is over tol:
                if station.relative_water_level() > tol:
                    #print("adding station", station.relative_water_level())
                    #add this tuple of station & the relative level to the output list 
                    ret.append((station.name, station.relative_water_level()))
    ret = sorted(ret, key=lambda x:-x[1])
    return ret

#task 2C - *stations most at risk* - same as b except no specific threshold, just a number of top stations
def stations_highest_rel_level(stations, N):
    ret = []
    #if relative water level is not none & it's consistent
    for station in stations:
        if station.typical_range_consistent() != False:
            if  type(station.relative_water_level()) == float:
                ret.append((station.name, station.relative_water_level()))
    ret = sorted(ret, key=lambda x:-x[1])
    top_N = ret[:N]
    return top_N
