import numpy as np


def get_train_data(array, window=5, 
                   n_days_forward=5):
    """
    Функция, подготавливающая данные для обучения модели
    """
    length = len(array)
    alist = []
    target = []
    
    i = 0
    while i <= length - n_days_forward - window:
        alist.append(array[i:i + window])
        target.append(array[i + window + n_days_forward - 1])
        i += 1
        
    alist = np.array(alist)
    alen = len(alist)
    arr = np.zeros((alen, window + 1))
    arr[:, :-1] = alist
    arr[:, -1] = target
    return arr


    
def train_test_split(X, y, test_size=0.3):
    """
    Функция, разделяющая выборку на train и на test.
    :param X: массив с фичами
    :param y: одномерный массив с целевой переменной
    :param array: массив со значениями временного ряда
    :param test_size: доля значений в test'е
    :return: (train, test) кортеж из двух массивов numpy.array
    """
    n_objects = len(y)
    threshold = round(n_objects * (1 - test_size))
    X_train = X[:threshold]
    X_test = X[threshold:]
    y_train = y[:threshold]
    y_test = y[threshold:]
    return X_train, X_test, y_train, y_test

