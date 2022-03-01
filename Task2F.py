from floodsystem.plot import plot_water_level_with_fit
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.datafetcher import fetch_measure_levels
import datetime

def run():
    stations = build_station_list()
    update_water_levels(stations)
    dt = 2
    print(stations[1])
    station=stations[1]
    dates, levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=dt))
    plot_water_level_with_fit(stations[1], dates, levels,3)

run()
