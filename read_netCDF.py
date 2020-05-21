# -*- coding: utf-8 -*-
"""
@author: Tristan O'Hanlon

time indices are monthly averages
"""

import numpy as np
from netCDF4 import Dataset  # http://code.google.com/p/netcdf4-python/
import os
import numpy as np

#specify location and file name
location = 'Model Data/'
file_name = 'clcalipso_CFmon_CESM2_amip_r2i1p1f1_gn_195001-201412.nc'

with Dataset(location + file_name, 'r') as f: 
    print(f.variables.keys())
    lat = f.variables[ 'lat' ][:] / 1000
    print("Latitude:", lat)
    lon = f.variables[ 'lon' ][:] / 1000
    print("Longitude:", lon)
    time = f.variables['time'][:]
    print("Time:", time)

