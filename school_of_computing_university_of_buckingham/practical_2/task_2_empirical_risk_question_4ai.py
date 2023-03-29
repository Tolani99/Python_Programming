"""
Question 4ai(continuation).
To compute the empirical risk for the
linear regression and provide the final value
in the pdf file.
"""

# Import from basic modules
from basic_modules import np
from basic_modules import df

# Extract the relevant columns
age = df.iloc[:60, 1]
water_temp = df.iloc[:60, 2]
length = df.iloc[:60, 3]

# Compute the predicted values of length
# using the regression function
length_pred = 2988.86 + 22.5290 * age + (-87.0169) * water_temp

# Compute the mean squared error
mse = np.mean((length - length_pred)**2)

# Print the empirical risk
print("Empirical risk Rempf: ", mse)
