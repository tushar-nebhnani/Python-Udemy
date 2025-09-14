import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression


df = pd.read_csv("experience_salary.csv")

X = df[["YearsOfExperience"]]
Y = df[["Salary"]]

model = LinearRegression()
model.fit(X, Y)

df["PredictedSalary"] = model.predict(X)
print("Model Co-Efficeint(slope): ", round(model.coef_[0][0], 2))
print("Model Intercept(base salary): ", round(model.intercept_[0], 2))

plt.scatter(X, Y, color="blue")
plt.plot(X, df["PredictedSalary"], color="red")
plt.xlabel("Years Of Experience")
plt.ylabel("Salay")
plt.title("Salary VS Experience")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()