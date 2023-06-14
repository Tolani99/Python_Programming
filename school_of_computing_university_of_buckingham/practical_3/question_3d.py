from question_3a import X
from question_3c import theta_map
from basic_modules import np

# Add a column of ones to X
X = np.c_[np.ones(X.shape[0]), X]

theta_map = np.array([0, theta_map[1], theta_map[2], theta_map[3]])
y_pred = X @ theta_map

squared_diff = (y_pred - y) ** 2

R_empf = np.mean(squared_diff)

print("Empirical Risk (R_empf):", R_empf)

