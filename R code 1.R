# Load necessary libraries
library(ggplot2)

# Read the data
# Correcting the file path for Windows
df <- read.csv("C:/Users/vemul/OneDrive/Desktop/T3/data_ted_talks.csv")

# Clean the data by removing rows with NaN values in 'views' or 'comments'
df_cleaned <- na.omit(df[, c("views", "comments")])

# Define the feature (X) and target variable (y)
X <- df_cleaned$views
y <- df_cleaned$comments

# Create a linear regression model
model <- lm(y ~ X)

# Make predictions
y_pred <- predict(model)

# Plot the data and the regression line
ggplot(data = df_cleaned, aes(x = X, y = y)) +
  geom_point(color = "blue") +               # Scatter plot of actual data
  geom_line(aes(y = y_pred), color = "red") + # Regression line
  labs(x = "Views", y = "Comments", title = "Linear Regression") +
  theme_minimal()

