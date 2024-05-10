from sklearn.preprocessing import StandardScaler
import pandas as pd

#загрузка данных из папки треин
data = pd.read_csv('train/dataset0.csv')

#предобработка данных
scaler = StandardScaler()
data['temperature'] = scaler.fit_transform(data['temperature'].values.reshape(-1, 1))

#сохранение данных
data.to_csv('train/dataset0_preprocessed.csv', index=False)
