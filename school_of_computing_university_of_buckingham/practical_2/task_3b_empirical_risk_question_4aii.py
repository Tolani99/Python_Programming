"""
Similarly, consider the first 60 rows and find parameters for
the following non-linear regression with the described feature
map, where we consider the loss function to be the square of
residuals
ϕ([x1 x2]) = [1 x1 x2 x1x2]
Compute the empirical risk. Provide the parameters and the
empirical risk in the pdf file.
"""
# Import basic modules
import pandas as pd
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression

# Load the data
data = pd.read_csv('fish_data.csv')

# Extract the first 60 rows and the relevant variables
X = data.iloc[:60, [1, 2]].values
y = data.iloc[:60, 3].values

# Apply the feature map to X
poly = PolynomialFeatures(degree=2, include_bias=True)
X_phi = poly.fit_transform(X)

# Fit a linear regression model to the transformed data
model = LinearRegression()
model.fit(X_phi, y)

# Print the model coefficients
print(model.intercept_, model.coef_)

# Compute the empirical risk
y_pred = model.predict(X_phi)
R_emp = ((y - y_pred) ** 2).mean()
print('Empirical risk:', R_emp)

