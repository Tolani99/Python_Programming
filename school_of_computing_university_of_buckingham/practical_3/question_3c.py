"""
To compute the MAP (Maximum A Posteriori) parameters θMAP using the last 60 rows of the "Octane_rating.csv" dataset, with a prior Gaussian distribution N(0, bI) where b = 10, and the noise parameter equal to the average loss for the θMLE (for the last 60 data points), we can follow these steps:
"""
from basic_modules import np
from question_3a import X, y

# Add a column of ones to X
X = np.c_[np.ones(X.shape[0]), X]

#Calculate the optimal parameters θMLE using the OLS formula:
theta_mle = np.linalg.inv(X.T @ X) @ X.T @ y

# Compute the noise parameter as the average loss for the θMLE
y_pred = X @ theta_mle
loss = (y_pred - y) ** 2
noise_param = np.mean(loss)

b = 10  # Prior variance parameter
I = np.eye(X.shape[1])  # Identity matrix

theta_map = np.linalg.inv(X.T @ X + (b / noise_param) * I) @ X.T @ y

print("MAP Parameters (θMAP):", theta_map)

"""
This will give you the values of the MAP parameters θMAP using the last 60 rows of the dataset, with a prior Gaussian distribution N(0, bI) where b = 10, and the noise parameter equal to the average loss for the θMLE (for the last 60 data points).
"""

