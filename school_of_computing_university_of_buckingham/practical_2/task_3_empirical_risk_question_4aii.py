"""
Question 4aii.
Similarly, consider the first 60 rows
and find parameters for the following
non-linear regression with the described feature map, 
where we consider the loss function to be the square of
residuals phi([x1, x2]) = [1, x1, x2, x1x2]
"""
# Import basic modules
from basic_modules import df
from basic_modules import np
from basic_modules import sm

# Extract the relevant columns for the first 60 rows
age = df.iloc[:60, 1]
water_temp = df.iloc[:60, 2]
length = df.iloc[:60, 3]

# Define the feature map
def phi(age, water_temp):
    return [1, age, water_temp, age*water_temp]

# Apply the feature map to the input data
X = [phi(age[i], water_temp[i]) for i in range(len(age))]

# Fit the non-linear regression model
model = sm.OLS(length, X)
results = model.fit()

# Print the results
print(results.summary())

# Compute the predicted values
y_pred = results.predict(X)

# Compute the MSE
mse = np.mean((y_pred - length)**2)

# Print the MSE
print("MSE:", mse)

# Define the regression function
def regression_function(age, water_temp):
    return results.params[0] + results.params[1]*age + results.params[2]*water_temp + results.params[3]*age*water_temp

# Print the regression function with the computed parameters
print("Regression function:", regression_function.__name__, "=", regression_function.__doc__)
