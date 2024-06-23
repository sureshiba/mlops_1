from sklearn.linear_model import LinearRegression
import joblib
import pandas as pd


#агрузка предобработанных файлов
data = pd.read_csv('train/dataset0_preprocessed.csv')

#создание модели
model = LinearRegression()
#собучение модели
model.fit(data['temperature'].values.reshape(-1, 1), data['temperature'].values)

#сохранение модели
joblib.dump(model, 'model.joblib')
