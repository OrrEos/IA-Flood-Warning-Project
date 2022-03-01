
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

from floodsystem.analysis import polyfit
from floodsystem.stationdata import build_station_list
from floodsystem.station import MonitoringStation
import numpy as np
import matplotlib

def plot_water_levels(station, dates, levels):
    # Plot
    plt.plot(dates, levels)

    # Add axis labels, rotate date labels and add plot title
    plt.xlabel('Date')
    plt.ylabel('Water Level /m')
    plt.xticks(rotation=45);
    plt.title(station)

    #Typical Low and High Levels
    lowLevel = station.typical_range[0]
    highLevel = station.typical_range[1]
    plt.axhline(y=lowLevel,color='r', linestyle=':')
    plt.axhline(y=highLevel, color='r',  linestyle='--')
   

    # Display plot
    plt.tight_layout()  # This makes sure plot does not cut off date labels

    plt.show()

def plot_water_level_with_fit(station, dates, levels, p):
    #is there any data?
    if len(dates) == 0 or len(levels) == 0:
        pass #ignore polyfit if there is no data

    else:
        poly, shift = polyfit(dates, levels, p)

        #update dates to be shifted
        dates = matplotlib.dates.date2num(dates) - shift
        #get 50 data points between first and last date for x axis, time
        time = np.linspace(dates[0], dates[-1], 50)

        #Plotting those graphs
        plt.plot(dates, levels, '-', label = "Original Data")
        plt.plot(time, poly(time), label = "Polyfit")

        low_level = station.typical_range[0]
        high_level = station.typical_range[1]

        plt.axhline(y=low_level,color='r', linestyle=':')
        plt.axhline(y=high_level, color='r',  linestyle='--')
    
        plt.tight_layout()  # This makes sure plot does not cut off date labels
        plt.ylabel("Relative Water Level")
        plt.xlabel("Days before now")

        plt.show()
    
    
"""
    for station in stations:
        if station.typical_range_consistent() != False:
            typical_min.append(station.typical_range[0])
            typical_max.append(station.typical_range[1])
"""