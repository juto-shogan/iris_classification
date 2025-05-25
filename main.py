import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
data = pd.read_csv('data/IRIS.csv')

x=data.iloc[:,:4]
y=data.iloc[:,4]

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=0)

#model making 
model1 = LogisticRegression()
model2 = SVC() 

model1.fit(x_train, y_train)
model2.fit(x_train, y_train)

# prediction 
y_pred1 = model1.predict(x_test)
y_pred2 = model2.predict(x_test)

# evaluate prediction and model performance

print("Accuracy:", accuracy_score(y_test, y_pred1))
print("Accuracy:", accuracy_score(y_test, y_pred2))