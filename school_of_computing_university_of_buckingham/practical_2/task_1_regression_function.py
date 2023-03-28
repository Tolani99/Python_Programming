"""
Question 4

Consider the data set “fish_data.csv” that contains
information about two types of fish.
Rows associate with each fish and
in columns their type, the age of the fish, 
water temperature in degrees
Celsius, and the length of the fish is recorded.
(a) Let the length variable (length of the fish)
in the data set be dependent on the age and water temperature.
i. Consider the first 60 rows and find parameters 
for the linear regression where we consider the 
loss function to be the square of residuals.
Provide the regression function with the computed
parameters in the pdf file.
"""
# Import from basic modules
from basic_modules import df
from basic_modules import sm
from basic_modules import pd

# Extract the relevant columns
age = df.iloc[:60, 1]
water_temp = df.iloc[:60, 2]
length = df.iloc[:60, 3]

"""
We can use the statsmodels library to
perform linear regression with the squared residuals
loss function:
"""
# Add a constant term to the input data
X = sm.add_constant(pd.DataFrame({'age': age, 'water_temp': water_temp}))

# Fit the linear regression model
model = sm.OLS(length, X)
results = model.fit()

# Print the results
# print(results.summary())
