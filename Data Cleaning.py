import re
import pandas as pd
import numpy as np
from datetime import datetime

# Read CSV file
airbnb = pd.read_csv('airbnb_v1.csv', skiprows=1, dtype='str')
airbnb = airbnb.drop('Unnamed: 15', axis=1)

# Numerical Columns

# Clean 'id' column
airbnb['id'] = [re.sub('[^0-9]', '', str(x)) for x in airbnb['id']]
airbnb['id'] = airbnb['id'].astype(int)

# Clean 'host id' column
airbnb['host id'] = [re.sub('[^0-9]', '', str(x)) for x in airbnb['host id']]
airbnb['host id'] = airbnb['host id'].astype(int)

# Clean 'minimum nights' column
airbnb['minimum nights'] = [re.sub('[^0-9]', '', str(x)) for x in airbnb['minimum nights']]
airbnb['minimum nights'] = airbnb['minimum nights'].astype(int)

# Clean 'number of reviews (total)' column
airbnb['number of reviews (total)'] = [re.sub('[^0-9]', '', str(x)) for x in airbnb['number of reviews (total)']]
airbnb['number of reviews (total)'] = airbnb['number of reviews (total)'].astype(int)

# Clean 'reviews per month' column
airbnb['reviews per month'] = [re.sub('nan|NaN', '0', str(x)) for x in airbnb['reviews per month']]
airbnb['reviews per month'] = [re.sub('[^0-9.]', '', str(x)) for x in airbnb['reviews per month']]
airbnb['reviews per month'] = airbnb['reviews per month'].astype(float)

# Clean 'noise.dB.' column
airbnb['noise.dB.'] = [re.sub('[^0-9.]', '', str(x)) for x in airbnb['noise.dB.']]
airbnb['noise.dB.'] = airbnb['noise.dB.'].astype(float)

# Clean 'price' column
airbnb['price'] = [re.sub('[^0-9.]', '', str(x)) for x in airbnb['price']]
airbnb['price'] = airbnb['price'].astype(int)

# Clean 'latitude' column
airbnb['latitude'] = [re.sub('[^0-9.]', '', str(x)) for x in airbnb['latitude']]
airbnb['latitude'] = airbnb['latitude'].astype(float)

# Clean 'longitude' column
airbnb['longitude'] = [re.sub('[^0-9.-]', '', str(x)) for x in airbnb['longitude']]
airbnb['longitude'] = airbnb['longitude'].astype(float)

# Categorical Columns

# Clean 'floor' column
floor_mapping = {
    'Lower Level': '0',
    'First Floor|1st-floor': '1',
    'Second Floor': '2',
    'Third Floor': '3',
    'Fourth Floor': '4',
    'Fifth Floor|5th floor|5th Floor': '5',
    'Sixth Floor': '6',
    'Seventh Floor': '7',
    'Eighth Floor': '8',
    'Ninth Floor': '9',
    'Tenth Floor': '10',
    'Eleventh Floor': '11',
    'Thirteenth Floor': '13',
    'Sixteenth Floor': '16',
    'Seventeenth Floor': '17',
    'Twentieth Floor': '20',
    'Hundreth Floor': '100',
}

airbnb['floor'] = [re.sub('|'.join(floor_mapping.keys()), lambda x: floor_mapping[x.group()], str(x)) for x in airbnb['floor']]
airbnb['floor'] = airbnb['floor'].astype(int)

## Clean 'room type' column
airbnb['room and type'] = [re.sub('Room Type Private|Privatè-Room','Private room',str(x)) for x in airbnb['room and type']]

## Clean 'neighbourhood group' column
airbnb['neighbourhood group'] = [re.sub('Brooklyn - \*\*Borough\*\*|Brooklyn Borough|brklyn','Brooklyn',str(x)) for x in airbnb['neighbourhood group']]
airbnb['neighbourhood group'] = [re.sub('broxn|  bronx_borugh|B-r-0-n-x|Bronx   ','Bronx',str(x)) for x in airbnb['neighbourhood group']]

## Clean 'neighbourhood' column
airbnb['neighbourhood'] = [re.sub('Brooklyn - \*\*Borough\*\*-Brooklyn - \*\*Borough\*\*|Brooklyn-Brooklyn|Brooklyn Borough-Brooklyn Borough|brklyn-brklyn','',str(x)) for x in airbnb['neighbourhood']]
airbnb['neighbourhood'] = [re.sub('Manhattan-Manhattan','',str(x)) for x in airbnb['neighbourhood']]
airbnb['neighbourhood'] = [re.sub('Bronx-Bronx|broxn   -broxn   ','',str(x)) for x in airbnb['neighbourhood']]
airbnb['neighbourhood'] = [re.sub('Queens-Queens','',str(x)) for x in airbnb['neighbourhood']]
airbnb['neighbourhood'] = [re.sub('Staten Island-Staten Island|, Staten Island','',str(x)) for x in airbnb['neighbourhood']]
airbnb['neighbourhood'] = airbnb['neighbourhood'].replace('nan',np.nan,regex=True)

# Date Column

## Clean 'last review (date)' column
airbnb['last review (date)'] = [re.sub('nan','3000-01-01',str(x)) for x in airbnb['last review (date)']]
airbnb['last review (date)'].str[7:11].unique()
airbnb['last review (date)']=airbnb['last review (date)'].apply(lambda x:datetime.strptime(x,"%Y-%m-%d"))
airbnb['last review (date)']=airbnb['last review (date)'].apply(lambda x:datetime.strftime(x,"%Y-%m-%d"))
airbnb = airbnb.replace('3000-01-01',np.nan,regex=True)

# Exporting CSV

airbnb.to_csv("Cleaned_Airbnb.csv")
