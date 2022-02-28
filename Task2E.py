import datetime
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_highest_rel_level
import floodsystem.plot as plot
from floodsystem.datafetcher import fetch_measure_levels
import matplotlib.pyplot as plt

def run():
    # Build list of stations
    stations = build_station_list()
    # Update latest level data for all stations
    update_water_levels(stations)

    #N stations with greatest current water level
    N =5
    stationlist = stations_highest_rel_level(stations, N)
    #list of names only
    stationlistName = []
    for i in stationlist:
        stationlistName.append(i[0])
  
    dt = 10
    for station in stations:
        #for the top N stations, get the "whole" station info, inc measure_id
        if station.name in stationlistName:
            dates, levels = fetch_measure_levels(
                station.measure_id, dt=datetime.timedelta(days=dt))

            # Plot water levels against time for each station.
            plot.plot_water_levels(station, dates, levels)
            plt.tight_layout()  # so that all data labels are shown
            print("Plot Water Level")
            #plt.show()

    

run()

    

