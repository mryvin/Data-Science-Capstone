install.packages("BSDA")
library(BSDA)

setwd("/Users/mryvi/Documents/Data Capstone")

airbnb <- read.csv("Cleaned_Airbnb.csv")

airbnb

queens = subset(airbnb, neighbourhood.group == 'Queens')
brooklyn = subset(airbnb, neighbourhood.group == 'Brooklyn')
bronx = subset(airbnb, neighbourhood.group == 'Bronx')
manhattan = subset(airbnb, neighbourhood.group == 'Manhattan')


## Proportion Z-test of Neighbourhood group vs floor
table(airbnb$neighbourhood.group)
table(queens$floor)
table(brooklyn$floor)

4530/4533

4/16084

prop.test(c(4530,4), c(4533,16084), p = NULL, alternative = "greater",
          correct = TRUE)


#Sample Z-test of average noise vs neighbourhood group

mean(manhattan$noise.dB.)
sd(manhattan$noise.dB.)

mean(bronx$noise.dB.)
sd(bronx$noise.dB.)

z.test(manhattan$noise.dB.,bronx$noise.dB.,
       alternative = "less",
       sigma.x = sd(manhattan$noise.dB.),
       sigma.y = sd(bronx$noise.dB.),
       conf.level = 0.95
)
