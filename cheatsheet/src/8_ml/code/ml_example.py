#read data
import pandas as pd
data = pd.read_csv('data.csv')

#split data into input and result set
y = data["diagnosis"]
X = data.drop(columns=["diagnosis"])

#split data into test and train set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y,
test_size=0.3, random_state= 42) #30% of data used for validation

#choose and train model
from sklearn import linear_model
model = linear_model.LinearRegression()
model.fit(X_train,y_train)

#validate and test model
from sklearn.metrics import accuracy_score
y_pred = model.predict(X_test)
score = accuracy_score(y_test, y_pred)

#CodeExpert grading based on y.final
X_final = pd.read_csv("X_final.csv")
y_final = model.predict(X_final)
return y_final