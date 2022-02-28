import matplotlib
from .station import MonitoringStation
import numpy as np


def polyfit(dates, levels,p):
    # Using shifted x values, find coefficient of best-fit
    # polynomial f(x) of degree p
    numbered_dates = matplotlib.dates.date2num(dates)
    p_coeff = np.polyfit(numbered_dates - numbered_dates[0], levels, p)
    # Convert coefficient into a polynomial that can be evaluated
    # e.g. poly(0.3)
    poly = np.poly1d(p_coeff)
    return (poly,numbered_dates[0])
