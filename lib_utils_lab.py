"""
Library Features:

Name:          lib_utils_lab
Author(s):     Fabio Delogu (fabio.delogu@cimafoundation.org)
Date:          '20220320'
Version:       '1.0.0'
"""

# -------------------------------------------------------------------------------------
# Libraries
import logging
import pickle
import os

import pandas as pd
# -------------------------------------------------------------------------------------

# -------------------------------------------------------------------------------------
# Method to read an ascii point file
def read_file_point(file_name, file_delimiter=';', file_header=0, file_columns_remap=None):

    if file_columns_remap is None:
        file_columns_remap = \
            {'ID': 'point_id', 'Station_Name': 'point_name', 'Station_Code': 'point_code',
             'Longitude': 'point_longitude', 'Latitude': 'point_latitude', 'VWCUnits': 'point_vwc_units',
             'DepthValue': 'point_depth_value', 'DepthUnits': 'point_depth_units', 'Porosity': 'point_porosity'}

    df_point = pd.read_csv(file_name, delimiter=file_delimiter, header=file_header)
    df_point.columns = df_point.columns.str.replace(' ', '')

    df_point_remap = df_point.rename(columns=file_columns_remap)

    df_point_remap['point_name'] = df_point_remap['point_name'].str.strip()
    df_point_remap['point_code'] = df_point_remap['point_code'].str.strip()
    df_point_remap['point_vwc_units'] = df_point_remap['point_vwc_units'].str.strip()
    df_point_remap['point_depth_units'] = df_point_remap['point_depth_units'].str.strip()

    return df_point_remap
# -------------------------------------------------------------------------------------



# -------------------------------------------------------------------------------------
# Method to read data obj
def read_obj(file_name):
    data = None
    if os.path.exists(file_name):
        data = pickle.load(open(file_name, "rb"))
    return data
# -------------------------------------------------------------------------------------
