#!/bin/bash

# Создаем наборы данных
python data_creation.py

# Предобрабатываем данные
python model_preprocessing.py

# Создаем и обучаем модель
python model_preparation.py

# Проверяем модель
python model_testing.py
