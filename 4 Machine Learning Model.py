import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def visualize_data(data, x_col, category_col=None, categories=None, num_rows=3, num_cols=3, scatter=True):
    fig, axs = plt.subplots(num_rows, num_cols, figsize=(20, 10))

    x = 0
    y = 0

    for col in data.columns:
        if col != x_col:
            continue

        if scatter:
            for other_col in data.columns:
                if col == other_col or data[other_col].map(type).eq(str).any() or other_col in ['id', 'host_id']:
                    continue
                axs[x, y].scatter(data[col], data[other_col], s=1)
                axs[x, y].set_title(f"{col} and {other_col}", fontsize=7)
        else:
            if not category_col or not categories:
                continue

            filtered_data = [data.loc[data[category_col] == category][x_col] for category in categories]
            axs[x, y].boxplot(filtered_data)
            axs[x, y].set_title(f'{x_col} across {category_col}s')
            axs[x, y].set_xticklabels(categories, rotation=45, fontsize=8)

        y += 1
        if y >= num_cols:
            x += 1
            y = 0

# Read the dataset
airbnb = pd.read_csv('playoffs_train.csv')

# Visualize Scatterplots
visualize_data(airbnb, 'price', None, None)

# Visualize Boxplots for Neighborhoods
visualize_data(airbnb, 'price', 'neighbourhood_group', ['Brooklyn', 'Bronx', 'Manhattan', 'Queens', 'Staten Island'])

# Visualize Boxplots for Room Types
visualize_data(airbnb, 'price', 'room_type', ['Private room', 'Entire home/apt', 'Shared room'])

plt.show()

