# Load necessary libraries
library(ggplot2)

# Read the dataset
df <- read.csv("C:/Users/vemul/OneDrive/Desktop/T3/data_ted_talks.csv")


# Remove rows with NA values in 'duration' or 'comments'
df <- na.omit(df[, c("duration", "comments")])

# Define X and y
X <- df$duration
y <- df$comments

# Create a linear regression model
model <- lm(y ~ X)

# Predict the values
y_pred <- predict(model)

# Create a scatter plot with regression line
ggplot(df, aes(x = X, y = y)) +
  geom_point(color = "blue") +               # Data points
  geom_line(aes(y = y_pred), color = "red") + # Regression line
  labs(x = "Duration", y = "Comments", title = "Linear Regression of Duration vs Comments")
