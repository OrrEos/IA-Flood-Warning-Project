import matplotlib
from .station import MonitoringStation
import numpy as np


def polyfit(dates, levels,p):
    # Using shifted x values, find coefficient of best-fit
    # polynomial f(x) of degree p

    #dates into a list of floats
    numbered_dates = matplotlib.dates.date2num(dates)
    
    #date shift is the first date
    shift = numbered_dates[0]
    #shifted dates to use for polynomial
    time = numbered_dates - shift

    #coeffs of bestfit polynomial
    p_coeff = np.polyfit(time, levels, p)

    # Convert coefficient into a polynomial that can be evaluated
    poly = np.poly1d(p_coeff)

    return poly, shift
