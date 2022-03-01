from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.analysis import polyfit
import matplotlib
import datetime
from floodsystem.datafetcher import fetch_measure_levels
import numpy as np

"""
My logic for task 2G:

1. classify stations into three categories (low, moderate and high) according to a flood factor
    (this flood factor compares relative water level to the typical range)
    this outputs a list of tuples (town & relative water level) for the high category
2. use polyfit to work out whether the water level is currently rising
    (found gradient between last two data points: if positive, then rising)
    a "severe" classification is given to towns in the high category that also have a rising water level
    this severe category is returned

"""



stations = build_station_list()
update_water_levels(stations)

def flood_factor_classification():
    inconsistent_data = []
    #severe = []
    high = []
    moderate = []
    low = []

    for station in stations:

        #if no data, put in a separate list with warning
        #lack of data doesn't mean that they're not possibly flooded
        #if relative water level is not none & it's consistent
        if station.typical_range_consistent() != False and type(station.relative_water_level()) == float:

            #find factor of relative water level compared to typical range 
            low_level = station.typical_range[0]
            high_level = station.typical_range[1]
            #how much higher is relative over typical low / typical range
            factor = (station.relative_water_level()-low_level) / (high_level - low_level)

            #divide the stations into risk categories
            #adding *town* not name, though
            #if factor >= 5:
            #    severe.append((station.town, factor))
            if factor >= 3:
                high.append((station.town, factor))
            #if relative level is around the typical high level:
            elif factor >= 1:
                moderate.append((station.town, factor))
            #if less than high level, town is probably not being flooded
            else:
                low.append((station.town, factor))

        else:
            inconsistent_data.append(station.town)

    #removing duplicates
    #severe = set(severe)
    high = set(high)
    moderate = set(moderate)
    low = set(low)
    
    #un-set the lists
    #severe = list(severe)
    high = list(high)
    moderate = list(moderate)
    low = list(low)

    #sort each risk category list from greatest factor to smallest
    #severe = sorted(severe, key=lambda x:-x[1])
    high = sorted(high, key=lambda x:-x[1])
    moderate = sorted(moderate, key=lambda x:-x[1])
    low = sorted(low, key=lambda x:-x[1])

    #print(high)
    return high


    
def mostRiskList():
    high = flood_factor_classification()
    #print("**Towns most at risk of flooding:**")
    #print(severe)
    #mostRisk = [i[0] for i in severe]
    highRisk = [i[0] for i in high]
    #print(highRisk) 
    #for i in range(len(mostRisk)):
    #    print("{}".format(mostRisk[i]))
    #print("There are {} towns at severe risk of flooding.".format(len(mostRisk)))
    #print(severe)
    #return severe
    
    #"severe" classification means that it 
    # 1)has factor greater than 3 
    #AND 2) a rising water level
    severe = []

    dt = 2
    for station in stations:
        if station.name in highRisk:
            dates, levels = fetch_measure_levels(
                station.measure_id, dt=datetime.timedelta(days=dt))
            #print(station.name)
            #print(dates)


            if len(dates) == 0 or len(levels) == 0:
                #print(station.name)
                pass #ignore polyfit if there is no data

            else:
                #print("have data")
                #print(station.name)
                poly, shift = polyfit(dates, levels, p = 4)
                #update dates to be shifted
                dates = matplotlib.dates.date2num(dates) - shift
                #get 50 data points between first and last date for x axis, time
                time = np.linspace(dates[0], dates[-1], 50)
                polyRisk = poly(time)
                #print(polyRisk)
                gradient = (polyRisk[-1] - polyRisk[-2])/(time[-1] - time[-2])
                #print(gradient)
                #a positive gradient means that the water level is rising
                if gradient > 0:
                    #print("Water level is rising at the following stations:")
                    #print(station.town)
                    severe.append(station.town)
    #print("**Water level is rising at the following stations:**")
    print("**Towns most at risk of flooding:**")
    for i in range(len(severe)):
        print("{}".format(severe[i]))
        
flood_factor_classification()
mostRiskList()