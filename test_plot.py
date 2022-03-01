import random
import datetime
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_highest_rel_level
import floodsystem.plot as plot
from floodsystem.datafetcher import fetch_measure_levels
import matplotlib.pyplot as plt
import numpy as np

def test_plot_water_levels():
#asserting that the plot itself is not shown if the dates and level list are empty.
    stations = build_station_list()
    update_water_levels(stations)
    dates = np.empty(5, dtype=object)
    levels = np.empty(5, dtype=object)
    dt = 10
    for i in range(5):
        dates[i], levels[i] = fetch_measure_levels(stations[i].measure_id, dt=datetime.timedelta(days=dt))

        plot.plot_water_levels(stations[i], dates[i], levels[i])

    assert plt.show() == None

test_plot_water_levels()

#task 2Fb
def test_plot_water_level_with_fit():
    stations = build_station_list()
    update_water_levels(stations)
    dates = np.empty(5, dtype=object)
    levels = np.empty(5, dtype=object)
    dt = 10
    order = 3
    for i in range(5):
        dates[i], levels[i] = fetch_measure_levels(stations[i].measure_id, dt=datetime.timedelta(days=dt))

        plot.plot_water_level_with_fit(stations[i], dates[i], levels[i], order)

    assert plt.show() == None
test_plot_water_level_with_fit()
