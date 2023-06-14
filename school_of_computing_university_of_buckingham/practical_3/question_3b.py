from question_3a import X, y, results
y_pred = results.predict(X)
residuals = y_pred - y
R_empf = (residuals ** 2).mean()

print("Empirical Risk (R_empf):", R_empf)
