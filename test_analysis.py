from floodsystem.analysis import polyfit
from floodsystem.stationdata import build_station_list, update_water_levels
import datetime
from floodsystem.datafetcher import fetch_measure_levels
import numpy as np

#task 2Fa
def test_polyfit():
    stations = build_station_list()
    update_water_levels(stations)
    station = stations[0]
    dates, levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=2))
    poly, shift = polyfit(dates, levels, 4)

    assert type(poly) == np.poly1d
    assert shift != 0
    assert type(shift) == np.float64

test_polyfit()

