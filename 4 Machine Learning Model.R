library(dplyr)
library(Metrics)
library(lmvar)
library(randomForest)
library(MASS)
library(e1071)

# Set the working directory to the location of the dataset
setwd()

# Read the training dataset from a CSV file
airbnb <- read.csv("playoffs_train.csv")

# Display a summary of a linear regression model for price prediction based on neighborhood group, floor, and room type
summary(lm(price ~ neighbourhood_group + floor + room_type, data = airbnb))

# Read the testing dataset from a CSV file
test <- read.csv("playoffs_test.csv")

# Train a Support Vector Machine (SVM) model on the training dataset
svm_fit3 <- svm(price ~ neighbourhood_group + floor + room_type, data = airbnb)

# Generate predictions on the training dataset using the trained SVM model
svm_training_predictions3 <- predict(svm_fit3, newdata = airbnb)

# Generate predictions on the testing dataset using the trained SVM model
svm_testing_predictions3 <- predict(svm_fit3, newdata = test)

# Assign the SVM predictions to the 'price' column in the testing dataset
test$price = svm_testing_predictions3

# Create a data frame for submission with an index column and SVM predicted prices
data <- data.frame(matrix(c(1:11858), nrow = 11858, ncol = 1))
data$price = svm_testing_predictions3

# Write the submission data frame to a CSV file named 'HW4Submission.csv'
write.csv(data, 'Submission.csv', row.names = FALSE)
