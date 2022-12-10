library(dplyr)
library(Metrics)
library(lmvar)
library(randomForest)
library(MASS)
library(e1071)

setwd("/Users/mryvi/Documents/Data Capstone")

airbnb <- read.csv("playoffs_train.csv")

summary(lm(price~neighbourhood_group+floor+room_type,data=airbnb))


test <- read.csv("playoffs_test.csv")

svm_fit3 <- svm(price~neighbourhood_group+floor+room_type, data=airbnb)
svm_training_predictions3 <- predict(svm_fit3, newdata=airbnb)
svm_testing_predictions3 <- predict(svm_fit3, newdata = test)

test$price = svm_testing_predictions3

data <- data.frame(matrix(c(1:11858),    # Create empty data frame
                          nrow = 11858,
                          ncol = 1))

data$price = svm_testing_predictions3
write.csv(data, 'HW4Submission.csv', row.names=FALSE)
