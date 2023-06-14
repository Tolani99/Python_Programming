from basic_modules import df, sm
# Extract the relevant columns
X = df.iloc[:60, :-1].values  # Input features (first four columns)
y = df.iloc[:60, -1].values   # Output variable (last column)

import numpy as np

# Add a column of ones to X
#X = np.c_[np.ones(X.shape[0]), X]

#theta_mle = np.linalg.inv(X.T @ X) @ X.T @ y

X = sm.add_constant(X)
model = sm.OLS(y, X)
results = model.fit()
print(results.summary())

#print("Optimal Parameters (θMLE):", theta_mle)
