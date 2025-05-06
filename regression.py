import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

salary_df = pd.read_excel(r"D:\da\glassdooranalysis.xlsx", sheet_name="regression")
x = salary_df["avg_size"].values
y = salary_df["REV_AVG_B"].values

plt.scatter(x, y, label="Actual Data")

y_intercept = -437.064830689656
co_ef = 0.894118395977217

# Predict revenue
pred_rev = [co_ef * val + y_intercept for val in x]

# Plot predicted line
plt.plot(x, pred_rev, color='red', label="Regression Line")
plt.xlabel("Average Size")
plt.ylabel("Revenue")
plt.legend()
plt.show()

# Print first 30 predictions and errors
for i in range(30):
    diff = y[i] - pred_rev[i]
    print(f"Actual Salary = {y[i]}, Predicted Rev = {pred_rev[i]}, Diff = {diff}")
