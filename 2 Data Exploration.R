library(BSDA)

setwd()

# Read the cleaned Airbnb dataset from a CSV file
airbnb <- read.csv("Cleaned_Airbnb.csv")

# Create subsets for each neighborhood group: Queens, Brooklyn, Bronx, Manhattan
queens = subset(airbnb, neighbourhood.group == 'Queens')
brooklyn = subset(airbnb, neighbourhood.group == 'Brooklyn')
bronx = subset(airbnb, neighbourhood.group == 'Bronx')
manhattan = subset(airbnb, neighbourhood.group == 'Manhattan')

########################################################################################### 
# Proportion Z-test of Neighbourhood group vs floor
########################################################################################### 

# Display the frequency table of the overall neighborhood groups
table(airbnb$neighbourhood.group)

# Display the frequency table of floors in Queens
table(queens$floor)

# Display the frequency table of floors in Brooklyn
table(brooklyn$floor)

# Proportion Z-test comparing the proportion of floors in Queens to the overall dataset
prop.test(c(4530, 4), c(4533, 16084), p = NULL, alternative = "greater",
          correct = TRUE)

########################################################################################### 
# Sample Z-test comparing the average noise levels between Manhattan and Bronx
########################################################################################### 

# Calculate mean and standard deviation of noise levels in Manhattan
mean(manhattan$noise.dB.)
sd(manhattan$noise.dB.)

# Calculate mean and standard deviation of noise levels in Bronx
mean(bronx$noise.dB.)
sd(bronx$noise.dB.)

# Perform a Z-test comparing noise levels in Manhattan and Bronx
z.test(manhattan$noise.dB., bronx$noise.dB.,
       alternative = "less",
       sigma.x = sd(manhattan$noise.dB.),
       sigma.y = sd(bronx$noise.dB.),
       conf.level = 0.95
)
