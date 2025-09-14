import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import streamlit as st


df = pd.read_csv("experience_salary.csv")

X = df[["YearsOfExperience"]]
Y = df[["Salary"]]

model = LinearRegression()
model.fit(X, Y)

st.title("Salary Predictor based on experience")
st.write("Enter your years of experience to predict your salary: ")
years_input = st.number_input("Years of experience", min_value=0.0, max_value=50.0, step=0.)

if years_input:
    print(years_input)

    predicted_salary = model.predict([[years_input]])[0]
    st.success(F"Estimated Salary: {predicted_salary}")

st.subheader("Regression Line")

fig, ax = plt.subplots()
ax.scatter(X, Y, color="blue")
ax.plot(X, model.predict(X), color="red")
ax.set_xlabel("Years Of Experience")
ax.set_ylabel("Salay")
ax.set_title("Salary VS Experience")
ax.legend()
st.pyplot(fig)