import sys
import unittest
import numpy as np


sys.path.append('../')
from model.preprocessor import get_prediction_data


class GetTrainDataTests(unittest.TestCase):
    def setUp(self):
        self.array_1 = np.array([0, 5, 3, 10, 4, 14,
                                 7, 9, 30, 53, 42, 44])

    def test_get_train_data_1(self):
        """
        Проверка функции с параметрами window=2, n_days_forward=5
        """
        train = get_prediction_data(self.array_1, window=2, n_days_forward=5)
        answer = np.array([[7, 9],
                           [9, 30],
                           [30, 53],
                           [53, 42],
                           [42, 44]])
        self.assertTrue((train == answer).all())

    def test_get_train_data_2(self):
        """
        Проверка функции с параметрами window=1, n_days_forward=7
        """
        train = get_prediction_data(self.array_1, window=1, n_days_forward=7)
        answer = np.array([[14], [7], [9], [30], [53], [42], [44]])
        self.assertTrue((train == answer).all())

    def test_get_train_data_3(self):
        """
        Проверка функции с пустым массивом на входе. Пусть функция возвращает ValueError
        """
        array = np.array([])
        with self.assertRaises(ValueError) as context:
            get_prediction_data(array)

        self.assertTrue('Empty array' in str(context.exception))

    def test_get_train_data_4(self):
        """
        Проверка поведения функции при завышенном window_size (параметр превышает размер массива)
        Должен падать!
        """
        array = np.array([0, 5, 10, 4])
        with self.assertRaises(ValueError) as context:
            get_prediction_data(array, window=5)

        self.assertTrue('Window size must be lesser than size of an array' in str(context.exception))

    def test_get_train_data_5(self):
        """
        Проверка поведения функции при завышенном n_days_forward 
        (с заданным window_size не получается нагенерить нужное количество строк в матрице)
        Должен падать!
        """
        array = np.array([0, 5, 10, 4])
        with self.assertRaises(ValueError) as context:
            get_prediction_data(array, n_days_forward=5)

        self.assertTrue('n_days_forward must be lesser than size of an array' in str(context.exception))

    def test_get_train_data_6(self):
        """
        Проверка функции с window_size=5, n_days_forward=5
        array_1 = np.array([0, 5, 3, 10, 4, 14,
                            7, 9, 30, 53, 42, 44])
                            12 - 5 = 7 - window = 2 + 1
                            start = 3 stop = start + 5(window)
                            start = 7 stop = start + 5(window)
        """
        train = get_prediction_data(self.array_1, window=5, n_days_forward=5)
        answer = np.array([[10, 4, 14, 7, 9],
                           [4, 14, 7, 9, 30],
                           [14, 7, 9, 30, 53],
                           [7, 9, 30, 53, 42],
                           [9, 30, 53, 42, 44]])
        self.assertTrue((train == answer).all())



if __name__ == '__main__':
    unittest.main()