import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

airbnb = pd.read_csv('Cleaned_Airbnb.csv')
airbnb = airbnb.drop('Unnamed: 0', axis=1)

##########################################################################################################################################
# Scatter Plots
##########################################################################################################################################

fig, axs = plt.subplots(8, 7, figsize=(25, 25))

x, y = 0, 0
# Create scatter plots for numerical feature pairs
for i in airbnb:
    if airbnb[i].map(type).eq(str).any() or i in ['id', 'host   id']:
        continue
    for j in airbnb:
        if i == j or airbnb[j].map(type).eq(str).any() or j in ['id', 'host   id']:
            continue
        axs[x, y].scatter(airbnb[i], airbnb[j], s=1)
        title = f"{i} and {j}"
        axs[x, y].set_title(title, fontsize=7)
        y += 1
        if y > 6:
            x += 1
            y = 0

plt.show()

##########################################################################################################################################
# Boxplots by Neighbourhood Group
##########################################################################################################################################

fig, axs = plt.subplots(2, 4, figsize=(20, 10))

x, y = 0, 0
# Create boxplots for numerical features grouped by neighbourhood
for i in airbnb:
    if airbnb[i].map(type).eq(str).any() or i in ['id', 'host   id']:
        continue
    neighborhoods = [airbnb.loc[(airbnb['neighbourhood group'] == n)][i] for n in ['Brooklyn', 'Bronx', 'Manhattan', 'Queens', 'Staten Island']]
    axs[x, y].boxplot(neighborhoods)
    axs[x, y].set_title(i)
    ticks = ['Brooklyn', 'Bronx', 'Manhattan', 'Queens', 'Staten Island']
    axs[x, y].set_xticklabels(np.repeat(ticks, 1), rotation=45, fontsize=8)
    y += 1
    if y > 3:
        y = 0
        x += 1

plt.show() 

##########################################################################################################################################
# Boxplots by Room Type
##########################################################################################################################################

fig, axs = plt.subplots(2, 4, figsize=(20, 10))

x, y = 0, 0
# Create boxplots for numerical features grouped by room type
for i in airbnb:
    if airbnb[i].map(type).eq(str).any() or i in ['id', 'host   id']:
        continue
    room_types = [airbnb.loc[(airbnb['room and type'] == t)][i] for t in ['Private room', 'Entire home/apt', 'Shared room']]
    axs[x, y].boxplot(room_types)
    axs[x, y].set_title(i)
    ticks = ['Private Room', 'Entire Home/Apartment', 'Shared Room']
    axs[x, y].set_xticklabels(np.repeat(ticks, 1), rotation=0, fontsize=8)
    y += 1
    if y > 3:
        y = 0
        x += 1

plt.show()

##########################################################################################################################################
# Boxplots for all numerical columns
##########################################################################################################################################

fig, axs = plt.subplots(2, 4, figsize=(20, 10))

x, y = 0, 0
# Create boxplots for all numerical features
for i in airbnb:
    if airbnb[i].map(type).eq(str).any() or i in ['id', 'host   id']:
        continue
    axs[x, y].boxplot(airbnb[i])
    axs[x, y].set_title(i)
    y += 1
    if y > 3:
        y = 0
        x += 1

plt.show() 

##########################################################################################################################################
# Other
##########################################################################################################################################

# Display Data Types and Unique Values
print(airbnb.dtypes)
print(airbnb['neighbourhood group'].unique())

# Bar Plot by Room Type and Neighbourhood Group
airbnb.groupby(['room and type', 'neighbourhood group']).size().unstack().plot(kind='bar', stacked=True)
plt.show()

# Crosstab Results
temp = pd.crosstab(index=airbnb["neighbourhood"], columns=airbnb["neighbourhood group"])

for borough in temp.columns:
    borough_hood = temp[temp[borough] != 0].drop(temp.columns.difference([borough]), axis=1)
    print(borough_hood)


