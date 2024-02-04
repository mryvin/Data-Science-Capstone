library(dplyr)

# Set the working directory to the location of the dataset
setwd()

# Read the cleaned Airbnb dataset from a CSV file
airbnb <- read.csv("Cleaned_Airbnb.csv")

# Perform a linear regression to analyze the relationship between price, floor, neighbourhood group, and noise levels
summary(lm(price ~ floor + neighbourhood.group + noise.dB., data = airbnb))

# Initialize an empty dataframe to store combined neighborhood predictions
airbnb2 = NA

# Loop through unique neighborhood groups to perform individual linear regressions

for (i in unique(airbnb$neighbourhood.group)) {
  # Subset the dataset for each neighborhood group
  neigh = subset(airbnb, neighbourhood.group == i)
  
  # Add a prediction column to the subset based on a linear regression model
  neigh$prediction <- predict(lm(price ~ noise.dB. + floor, data = neigh), neigh)
  
  # Combine the subsets into a new dataframe
  airbnb2 = rbind(airbnb2, neigh)
  
  # Display summary statistics for each neighborhood's linear regression model
  test = lm(price ~ noise.dB. + floor, data = neigh)
  print(summary(test))
}

# Display the summary of a linear regression model using the combined predictions
summary(lm(price ~ prediction, data = airbnb2))
