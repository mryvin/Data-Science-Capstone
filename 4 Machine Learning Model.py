import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Read the dataset
airbnb = pd.read_csv('playoffs_train.csv')

############################################################################################################
# Displaying a Scatterplot for each numeric feature
############################################################################################################

fig, axs = plt.subplots(3, 3, figsize=(25, 25))

x = 0
y = 0

for i in airbnb.columns:
    if i != 'price':
        continue

    for j in airbnb.columns:
        if i == j or airbnb[j].map(type).eq(str).any() or j in ['id', 'host_id']:
            continue

        # Scatter plot
        axs[x, y].scatter(airbnb[i], airbnb[j], s=1)

        # Customize the plot
        axs[x, y].set_title(f"{i} and {j}", fontsize=7)

        y += 1
        if y > 2:
            x += 1
            y = 0

############################################################################################################
# Displaying Boxplots for 'price' across different neighborhood groups
############################################################################################################

fig, axs = plt.subplots(2, 4, figsize=(20, 10))

x = 0
y = 0

for i in airbnb.columns:
    if i != 'price':
        continue

    # Filter data based on neighborhood groups
    Brooklyn = airbnb.loc[(airbnb['neighbourhood_group'] == 'Brooklyn')]
    Bronx = airbnb.loc[(airbnb['neighbourhood_group'] == 'Bronx')]
    Manhattan = airbnb.loc[(airbnb['neighbourhood_group'] == 'Manhattan')]
    Queens = airbnb.loc[(airbnb['neighbourhood_group'] == 'Queens')]
    Staten = airbnb.loc[(airbnb['neighbourhood_group'] == 'Staten Island')]

    # Boxplot
    axs[x, y].boxplot([Brooklyn[i], Bronx[i], Manhattan[i], Queens[i], Staten[i]])

    # Customize the plot
    axs[x, y].set_title(f'{i} across Neighborhoods')
    ticks = ['Brooklyn', 'Bronx', 'Manhattan', 'Queens', 'Staten Island']
    axs[x, y].set_xticklabels(np.repeat(ticks, 1), rotation=45, fontsize=8)

    y += 1
    if y > 3:
        y = 0
        x += 1

############################################################################################################
# Displaying Boxplots for 'price' across different room types
############################################################################################################

fig, axs = plt.subplots(2, 4, figsize=(20, 10))

x = 0
y = 0

for i in airbnb.columns:
    if i != 'price':
        continue

    # Filter data based on room types
    Priv = airbnb.loc[(airbnb['room_type'] == 'Private room')]
    Entire = airbnb.loc[(airbnb['room_type'] == 'Entire home/apt')]
    Shared = airbnb.loc[(airbnb['room_type'] == 'Shared room')]

    # Boxplot
    axs[x, y].boxplot([Priv[i], Entire[i], Shared[i]])

    # Customize the plot
    axs[x, y].set_title(f'{i} across Room Types')
    ticks = ['Private Room', 'Entire Home/Apartment', 'Shared Room']
    axs[x, y].set_xticklabels(np.repeat(ticks, 1), rotation=45, fontsize=8)

    y += 1
    if y > 3:
        y = 0
        x += 1

plt.show()

