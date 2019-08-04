import numpy as np


def get_train_data(array, window=5, 
                   n_days_forward=7):
    """
    Функция, преобразующая временной ряд в двумерный массив для линейной регрессии.

    :param array: одномерный массив, содержащий значения временного ряда
    :param window: длина скользящего окна
    :param n_days_forward: число дней, значения в которые мы предсказываем
    :return: numpy.array с .shape = (n_days_forward, window)
    """
    length = len(array)
    if not length:
        raise ValueError('Empty array')
    # if # проверка на window:
    #     raise ValueError('Incorrect window size')
    # if # проверка на n_days_forward:
    #     raise ValueError('Incorrest n_days_forward')
    # вставить условие проверки на удовлетворение размеров окна и n_days_forward
    new_array = np.zeros((n_days_forward, window))
    
    for row in range(n_days_forward):
        start = length - n_days_forward + row - window + 1
        stop = start + window
        new_array[row, :] = array[start:stop]
    return new_array
        

