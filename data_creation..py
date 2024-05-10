import numpy as np
import pandas as pd

#создание набора данных 5 шт
num_datasets = 5
datasets = []
for i in range(num_datasets):
    #случайные данные температуры
    temperature = np.random.normal(20, 5, 1000)

    #добавление аномалий в некоторые наборы данных
    if i % 2 == 0:
        temperature[np.random.randint(0, 1000, 10)] = 40

    #добавление  шума в некоторые наборы данных
    if i % 3 == 0:
        temperature += np.random.normal(0, 1, 1000)

    # Создаем датафрейм
    dataset = pd.DataFrame({
        'temperature': temperature
    })

    #сохранение в папки треин и тест
    if i < num_datasets // 2:
        dataset.to_csv('train/dataset0.csv'.format(i), index=False)
    else:
        dataset.to_csv('test/dataset1.csv'.format(i), index=False)
