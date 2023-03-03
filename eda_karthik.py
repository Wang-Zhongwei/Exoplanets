# -*- coding: utf-8 -*-
"""
Created on Fri Mar  3 11:24:00 2023

@author: karna
"""

import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('data/confirmed.csv', header=98)

earth_mass_comparison = data.loc[data['pl_bmassprov']=='Mass', 'pl_bmasse']
jupiter_mass_comparison = data.loc[data['pl_bmassprov']=='Mass', 'pl_bmassj']


fig = plt.figure(figsize = (10, 7))
 
fig, ax = plt.subplots()
earth_mass_comparison.plot(kind='box', ax=ax)
ax.set_title("Comparison of planet masses against earth's mass")
ax.set_xlabel('Planet masses in earth masses')
ax.set_yscale('log')
ax.set_xticks([])

fig, ax = plt.subplots()
jupiter_mass_comparison.plot(kind='box', ax=ax)
ax.set_title("Comparison of planet masses against jupiter's mass")
ax.set_xlabel('Planet masses in jupiter masses')
ax.set_yscale('log')
ax.set_xticks([])


fig, ax = plt.subplots()
data['disc_year'].value_counts().plot(kind='bar', ax=ax)
ax.set_title('Total planets discovered by year')
ax.set_xlabel('Discovery year')

fig, ax = plt.subplots()
data.isna().sum()[data.isna().sum()>len(data)//2].plot(kind='bar')
ax.set_title('Missing values (>50%) by column')
ax.set_xlabel('Column')
ax.tick_params(axis='both', which='major', labelsize=7)
