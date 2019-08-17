# -*- coding: utf-8 -*-
# Author: Harsha Vardhan Jarugu


import os
from os.path import join
import pandas as pd
pd.options.mode.chained_assignment = None

Master_Location = r'./data/sentinel-2a-tile-7680x-10240y/timeseries/'

def FileName(path):
    file_identifier = os.path.split(path)[-1]
    File_Name = file_identifier.split('.')[0]
    return File_Name

col_names =  ['file_path','title_x', 'title_y', 'band','date']
file_details_df  = pd.DataFrame(columns = col_names)

file_path=[]
title_x=[]
title_y=[]
band=[]
date=[]
for r, d, f in os.walk(Master_Location):
    for file in f:
        if file.endswith(".png"):
            date_extract = file.split("-")[3]+'-'+file.split("-")[4]+'-'+file.split("-")[5]
            date_extract= date_extract.replace('.png','')
            title_x.append(file.split("-")[0])
            title_y.append(file.split("-")[1])
            band.append(file.split("-")[2])
            date.append(date_extract)
            file_path.append(join(r, file))
file_details_df['file_path']= file_path 
file_details_df['title_x']= title_x 
file_details_df['title_y']= title_y 
file_details_df['band']= band 
file_details_df['date']= date


file_details_df['date'] = pd.to_datetime(file_details_df['date'], format='%Y%m%d', errors='ignore')

#file_details_df.to_csv('ImageName.csv')

band_col_names =  ['Band','Description', 'CentralWavelength_um', 'Resolution_m']
bands_df  = pd.DataFrame(columns = band_col_names)
bands_df

import csv
band_l=[]
description_l=[]
CentralWavelength_um_l=[]
Resolution_m_l=[]

with open('data_bands.csv', 'r') as csvFile:
    reader = csv.reader(csvFile)
    for row in reader:
        band_l.append(row[0])
        description_l.append(row[1])
        CentralWavelength_um_l.append(row[2])
        Resolution_m_l.append(row[3])
        print(row)
csvFile.close()

bands_df['Band'] = band_l
bands_df['Description'] = description_l
bands_df['CentralWavelength_um'] = CentralWavelength_um_l
bands_df['Resolution_m'] = Resolution_m_l

bands_df = bands_df.iloc[1:]
