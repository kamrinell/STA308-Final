# -*- coding: utf-8 -*-
"""
Created on Sat Dec  9 12:59:00 2023
@author: Camryn

Within the four census regions 
computing percentage decrease of flu-pneumonia mortality
the standard deviation
and coefficient of variation
from 2018-2021
"""

import pandas as pd

mortality_2018 = pd.read_csv("https://tjfisher19.github.io/data/fluPneumonia_2018.csv")
mortality_2021 = pd.read_csv("https://tjfisher19.github.io/data/fluPneumonia_2021.csv")
state_codes = pd.read_csv("https://tjfisher19.github.io/data/state_abb_codes.csv")
census_regions = pd.read_csv("https://tjfisher19.github.io/data/censusRegions.csv")

##mortality_2021 now has the state name code that matches 2018 and census regions set up##
mortality_2021 = mortality_2021.merge(state_codes, on="State")
mortality_2021 = mortality_2021.drop(columns = ['State','Abbrev'])
mortality_2021 = mortality_2021.rename(columns={'Code':'State'})


##drop Hawaii and Alaska##
mortality_2018 = mortality_2018[mortality_2018.State != 'HI']
mortality_2018 = mortality_2018[mortality_2018.State != 'AK']

mortality_2021 = mortality_2021[mortality_2021.State != 'HI']
mortality_2021 = mortality_2021[mortality_2021.State != 'AK']


## merge regions to each mortality data yr ##
mortality_2018 = mortality_2018.merge(census_regions, on = "State")
mortality_2021 = mortality_2021.merge(census_regions, on = "State")

## merge 2018 and 2021 together on region##
mortality_compare = mortality_2018.merge(mortality_2021, on = ["State","Region"])

## Percentage Diff ##
mortality_compare = mortality_compare.assign(
    Percentage = (mortality_compare.Rate_x - mortality_compare.Rate_y)/(mortality_compare.Rate_x)*100)

# https://www.marsja.se/coefficient-of-variation-in-python-with-pandas-numpy/ 
# Calculate coefficient of variation for each group
cv_data = mortality_compare.groupby('Region')['Percentage'].agg(lambda x: x.std() / 
                                                      x.mean() * 100).reset_index(name='cv %')
##stdev ##
std_data = mortality_compare.groupby('Region')['Percentage'].agg(lambda x: x.std()
                                                                 ).reset_index(name='std')

sd_cv_data = cv_data.merge(std_data, on="Region")

## mean percentage diff ##
mean_diff = mortality_compare.groupby('Region')['Percentage'].agg(lambda x: x.mean()
                                                                  ).reset_index(name='mean percent diff')

mortality_all_data = sd_cv_data.merge(mean_diff, on ="Region")

print(mortality_all_data)
