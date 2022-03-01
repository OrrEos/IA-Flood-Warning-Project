
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

from sklearn.tree import plot_tree
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
    poly, shift = polyfit(dates, levels, p)
    numbered_dates = matplotlib.dates.date2num(dates)
    dates = np.linspace(numbered_dates[0],numbered_dates[-1],50)
    #Typical Low and High Levels
    low_level = station.typical_range[0]
    high_level = station.typical_range[1]

#trying to account for different list lengths in plotting
    plt.plot(dates, np.linspace(low_level, low_level,50), label = 'Typical Minimum')
    plt.plot(dates, np.linspace(high_level, high_level,50), label = 'Typical Maximum')
#    plt.plot(dates, levels, label = 'Actual data')
    plt.plot(dates, poly(dates), label = 'Polynomial model')


"""
    for station in stations:
        if station.typical_range_consistent() != False:
            typical_min.append(station.typical_range[0])
            typical_max.append(station.typical_range[1])
"""