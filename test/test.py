import sys
import unittest
import numpy as np

from model.preprocessor import get_train_data


sys.path.append('../')


class GetTrainDataTests(unittest.TestCase):
    def setUp(self):
        self.array = np.array([0, 5, 3, 10, 4, 14,
                               7, 9, 30, 53, 42, 44])

    def test_get_train_data_1(self):
        """
        Проверка функции с параметрами window=2, n_days_forward=5
        """
        train = get_train_data(self.array, window=2, n_days_forward=5)
        answer = np.array([[7, 9],
                           [9, 30],
                           [30, 53],
                           [53, 42],
                           [42, 44]])
        self.assertEqual(train, answer)

    def test_get_train_data_2(self):
        """
        Проверка функции с параметрами window=1, n_days_forward=7
        """
        train = get_train_data(self.array, window=1, n_days_forward=7)
        answer = np.array([[14], [7], [9], [30], [53], [42], [44]])
        self.assertEqual(train, answer)

    def test_get_train_data_3(self):
        """
        Проверка функции с пустым массивом на входе
        """
        array = np.array([])
        train = get_train_data(array)
        self.assertEqual(train, array)

    def test_get_train_data_4(self):
        """
        Проверка поведения функции при завышенном window_size (параметр превышает размер массива)
        """
        array = np.array([0, 5, 10, 4])
        train = get_train_data(array, window=5, n_days_forward=3)
        answer = np.array([[]])
        self.assertEqual(train, answer)

    def test_get_train_data_5(self):
        """
        Проверка поведения функции при завышенном n_days_forward 
        (с заданным window_size не получается нагенерить нужное количество строк в матрице)
        """
        array = np.array([0, 5, 10, 4])
        train = get_train_data(array, window=1, n_days_forward=7)
        answer = np.array([[]])
        self.assertEqual(train, answer)

    def test_get_train_data_6(self):
        """
        Проверка функции с window_size=4, n_days_forward=5
        """
        train = get_train_data(self.array, window=4, n_days_forward=5)
        answer = np.array([[10, 4, 14, 7, 9],
                           [4, 14, 7, 9, 30],
                           [14, 7, 9, 30, 53],
                           [7, 9, 30, 53, 42],
                           [9, 30, 53, 42, 44]])
        self.assertEqual(train, answer)



if __name__ == '__main__':
    unittest.main()