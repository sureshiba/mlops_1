# Задание
Простой конвейер для автоматизации работы с моделью машинного обучения. Отдельные этапы конвейера машинного обучения описываются в разных python–скриптах, которые соединяются с помощью bash-скрипта.


Этапы
Создан python-скрипт (data_creation.py), который создает различные наборы данных, описывающий процесс изменение дневной температуры. Таких наборов несколько, включены аномалии и шумы. 
Часть наборов данных сохранена в папке «train», другая часть — в папке «test».
Создан python-скрипт (model_preprocessing.py), который выполняет предобработку данных с помощью sklearn.preprocessing.StandardScaler.
Создайн python-скрипт (model_preparation.py), который создает и обучает модель машинного обучения на построенных данных из папки «train».
Создан python-скрипт (model_testing.py), проверяющий модель машинного обучения на построенных данных из папки «test».
Написан bash-скрипт (pipeline.sh), последовательно запускающий все python-скрипты.
