import pandas as pd
import matplotlib.pyplot as plt

# Load Airbnb data
airbnb = pd.read_csv('Cleaned_Airbnb.csv').drop('Unnamed: 0', axis=1)

# Function to create scatter plots for different feature combinations
def create_scatter_plots(data, condition, feature_name):
    fig, axs = plt.subplots(3, 3, figsize=(25, 25))

    x = 0
    y = 0

    for i in data.columns:
        if i != feature_name:
            continue

        for j in data.columns:
            if i == j:
                continue
            if data[j].map(type).eq(str).any() or j == 'id' or j == 'host id':
                continue

            axs[x, y].scatter(data[i], data[j], s=1)
            temp = " and "
            title = f"{i}{temp}{j}"
            axs[x, y].set_title(title, fontsize=7)

            y += 1
            if y > 2:
                x += 1
                y = 0

    plt.suptitle(f'Scatter Plots for {feature_name} in {condition}', fontsize=20)
    plt.show()

# Scatter plots for 'price', 'noise.dB.', and 'floor'
create_scatter_plots(airbnb, 'All Listings', 'price')
create_scatter_plots(airbnb, 'All Listings', 'noise.dB.')
create_scatter_plots(airbnb, 'All Listings', 'floor')

# Filter data for Brooklyn listings
brooklyn = airbnb.loc[airbnb['neighbourhood group'] == 'Brooklyn']

# Scatter plots for 'price' in Brooklyn
create_scatter_plots(brooklyn, 'Brooklyn Listings', 'price')
