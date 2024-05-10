from sklearn.linear_model import LinearRegression
import joblib
import pandas as pd
from sklearn.preprocessing import StandardScaler


#загрузка тестовых данных
data = pd.read_csv('test/dataset1.csv')

#предобработка тестовых данных
scaler = StandardScaler()
data['temperature'] = scaler.fit_transform(data['temperature'].values.reshape(-1, 1))

#загрузка модели
model = joblib.load('model.joblib')

#проверка модели
print(model.score(data['temperature'].values.reshape(-1, 1), data['temperature'].values))
