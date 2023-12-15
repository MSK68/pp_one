import sys
import os
sys.path.append(os.path.abspath('../'))


import unittest
from  src.main import summ, min_leght
from unittest.mock import patch
from io import StringIO


class Test_Summ(unittest.TestCase):

    def test_summ_short(self):
        result = summ("Маленькая статья", 100, 200)
        self.assertEqual(result, f'Минимальное количество символов в статье {min_leght}')

    def test_summ_long(self):
        with patch('sys.stdout', new=StringIO()) as fake_output:
            result = summ("Очень очень очень очень очень очень очень очень очень очень очень очень очень очень очень очень очень очень Очень очень очень очень очень очень очень очень очень большая статья", 50,
                          200)
            self.assertEqual(result, f'Минимальное количество символов в статье {min_leght}')
            self.assertEqual(fake_output.getvalue(), '')

    def test_summ_invalid_min_length(self):
        result = summ("Проверка некорректно заданной минимальной длины",2000, 300)
        self.assertEqual(result, f'Минимальное количество символов в статье {min_leght}')

    def test_summ_invalid_max_length(self):
        with patch('sys.stdout', new=StringIO()) as fake_output:
            result = summ("Проверка некорректно заданной максимальной длины", 50,5000)
            self.assertEqual(result, f'Минимальное количество символов в статье {min_leght}')
            self.assertEqual(fake_output.getvalue(), '')


if __name__ == '__main__':
    unittest.main()