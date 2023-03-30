from basic_modules import np
from basic_modules import df
from basic_modules import sm

# Extract the relevant columns for training and testing
age_train = df.iloc[:60, 1].values
water_temp_train = df.iloc[:60, 2].values
length_train = df.iloc[:60, 3].values
age_test = df.iloc[60:70, 1].values
water_temp_test = df.iloc[60:70, 2].values
length_test = df.iloc[60:70, 3].values

# Define the feature map for the non-linear regression
def feature_map(x1, x2):
    return np.array([1, x1, x2, x1 * x2])

# Linear regression
X_train_linear = np.array([age_train, water_temp_train]).T
X_train_linear = sm.add_constant(X_train_linear)
X_test_linear = np.array([age_test, water_temp_test]).T
X_test_linear = sm.add_constant(X_test_linear)
model_linear = sm.OLS(length_train, X_train_linear)
results_linear = model_linear.fit()
y_pred_linear = results_linear.predict(X_test_linear)
mse_linear = np.mean((length_test - y_pred_linear)**2)
print("Linear regression MSE:", mse_linear)

# Non-linear regression
X_train_nonlinear = np.array([feature_map(x1, x2) for x1, x2 in zip(age_train, water_temp_train)])
X_test_nonlinear = np.array([feature_map(x1, x2) for x1, x2 in zip(age_test, water_temp_test)])
theta_nonlinear = np.linalg.inv(X_train_nonlinear.T @ X_train_nonlinear) @ X_train_nonlinear.T @ length_train
y_pred_nonlinear = X_test_nonlinear @ theta_nonlinear
mse_nonlinear = np.mean((length_test - y_pred_nonlinear)**2)
print("Non-linear regression MSE:", mse_nonlinear)

