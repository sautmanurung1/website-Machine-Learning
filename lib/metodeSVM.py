import pandas as pd
import numpy as np
import pickle
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

dataset = pd.read_csv('../dataset/output-IP.csv', sep=',')
dataset_new = pd.read_csv('../dataset/output-FP-data.csv', sep=',')

x = dataset_new[['Output']]
y = dataset['count']

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=0)
model = SVC()
model.fit(x_train, y_train)
y_pred = model.predict(x_train)
model_accuracy = accuracy_score(y_train, y_pred)
print('Model Accuracy Score: ', model_accuracy)
y_pred_test = model.predict(x_test)
training_set_accuracy = accuracy_score(y_test, y_pred_test)
print('Training-Set Accuracy Score: ', training_set_accuracy)

pickle.dump(model, open('model.pkl', 'wb'))
pickle.dump(model_accuracy, open('model_accuracy.pkl', 'wb'))
pickled_model = pickle.load(open('model.pkl', 'rb'))
pickled_model_accuracy = pickle.load(open('model_accuracy.pkl', 'rb'))
pickled_model.predict(x_test)