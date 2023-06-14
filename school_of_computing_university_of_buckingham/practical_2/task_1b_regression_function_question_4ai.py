"""
In the code above, we are selecting the first 60 rows
and columns 1, 2, and 3 (age, water temperature, and length)
from the data set and storing them in the variables X and y.

Next, we can use scikit-learn library to perform
linear regression on the data. Specifically,
we will use the LinearRegression class to fit a
linear model to the data and compute the coefficients of the model.

Here's the Python code to perform linear regression
and compute the coefficients:
"""
# Import basic modules
from sklearn.linear_model import LinearRegression
from basic_modules import df

# Extract the necessary columns for regression analysis
X = df.iloc[:60, [1, 2]].values
y = df.iloc[:60, 3].values

# Fit a linear regression model to the data
regressor = LinearRegression()
regressor.fit(X, y)

# Compute the coefficients of the model
coef_age, coef_temp = regressor.coef_
intercept = regressor.intercept_

# Print the regression function
print(f"Length = {intercept:.2f} + {coef_age:.2f}*age + {coef_temp:.2f}*temperature")
