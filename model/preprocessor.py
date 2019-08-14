import numpy as np


def get_prediction_data(array, window=5, 
                   n_days_forward=7):
    """
    Функция, преобразующая данные для предсказания на проде

    :param array: одномерный массив, содержащий значения временного ряда
    :param window: длина скользящего окна
    :param n_days_forward: число дней, значения в которые мы предсказываем
    :return: numpy.array с .shape = (n_days_forward, window)
    """
    length = len(array)
    if not length:
        raise ValueError('Empty array')
    if window > length:
        raise ValueError('Window size must be lesser than size of an array')
    if n_days_forward > length:
        raise ValueError('n_days_forward must be lesser than size of an array')
    
    new_array = np.zeros((n_days_forward, window))
    
    for row in range(n_days_forward):
        start = length - n_days_forward + row - window + 1
        stop = start + window
        new_array[row, :] = array[start:stop]
    return new_array


def parse_json(json):
    """
    Функция, возвращающая список datetime и np.array с четырьмя значениями построчно
    :param json: json, возвращенный alpha_vantage
    :return: 
    days, - список дней в формате datetime.datetime
    data - np.array с shape (x, 4) (low, high, open, close)
    """
    days = sorted(json.keys())
    n_days = len(days)
    high_ = []
    low_ = []
    close_ = []
    open_ = []
    volume_ = []

    for day in days:
        open_.append(float(json[day]['1. open']))
        high_.append(float(json[day]['2. high']))
        low_.append(float(json[day]['3. low']))
        close_.append(float(json[day]['4. close']))
        volume_.append(float(json[day]['5. volume']))
    
    data = np.zeros((n_days, 4))
    data[:, 0] = low_
    data[:, 1] = high_
    data[:, 2] = open_
    data[:, 3] = close_
    return data


