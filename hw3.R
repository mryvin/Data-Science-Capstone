library(dplyr)

setwd("/Users/mryvi/Documents/Data Capstone")

airbnb <- read.csv("Cleaned_Airbnb.csv")

airbnb

summary(lm(price~floor+neighbourhood.group+noise.dB.,data=airbnb))

airbnb2 = NA

for (i in unique(airbnb$neighbourhood.group)) {
  neigh = subset(airbnb,neighbourhood.group == i)
  neigh$prediction <- predict(lm(price ~ noise.dB.+floor,data=neigh),neigh)
  airbnb2 = rbind(airbnb2,neigh)
  
  test = lm(price ~ noise.dB.+floor,data=neigh)
  print(summary(test))
  
}

summary(lm(price~prediction,data=airbnb2))
