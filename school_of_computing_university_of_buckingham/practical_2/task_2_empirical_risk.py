#Import from basic modules
from basic_modules import np
from basic_modules import df

# Extract the relevant columns
age = df.iloc[:60, 1]
water_temp = df.iloc[:60, 2]
length = df.iloc[:60, 3]

# Compute the predicted values of length using the regression function
length_pred = -5.9249 + 0.1396 * age + 0.4229 * water_temp

# Compute the mean squared error
mse = np.mean((length - length_pred)**2)

# Print the empirical risk
print("Empirical risk Rempf: ", mse)
