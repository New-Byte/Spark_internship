#Prasad Mukund Joshi
#Student at Government College of Engineering, Jalgaon.
#Marks prediction system

#Import libraries
import pandas as pd
from sklearn.linear_model import LinearRegression

#Get user input
time = float(input("Enter duration of study: "))

#Load dataset
dataset = pd.read_csv("data.csv")

#Get x and y vectors
x = dataset.iloc[:,:-1].values
y = dataset.iloc[:,1].values

#Train the model
model = LinearRegression()    
model.fit(x, y) 

#Predict the result
result = model.predict([[time]])

#Display output
print("Predicted marks: ", round(result[0],2))