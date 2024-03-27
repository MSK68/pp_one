import sys
sys.path.append('../')

import unittest
from pp_one.src.main import summarize_text, min_leght
from unittest.mock import patch
from io import StringIO


class Test_Summ(unittest.TestCase):

    def test_summarize_text_short(self):
        result = summarize_text("Маленькая статья", 100, 200)
        self.assertEqual(result, f'Минимальное количество символов в статье {min_leght}')

    def test_summarize_text_long(self):
        with patch('sys.stdout', new=StringIO()) as fake_output:
            result = summarize_text("Очень очень очень очень очень очень очень очень очень очень очень очень очень очень очень очень очень очень Очень очень очень очень очень очень очень очень очень большая статья", 50,
                          200)
            self.assertEqual(result, f'Минимальное количество символов в статье {min_leght}')
            self.assertEqual(fake_output.getvalue(), '')

    def test_summarize_text_invalid_min_length(self):
        result = summarize_text("Проверка некорректно заданной минимальной длины",2000, 300)
        self.assertEqual(result, f'Минимальное количество символов в статье {min_leght}')

    def test_summarize_text_invalid_max_length(self):
        with patch('sys.stdout', new=StringIO()) as fake_output:
            result = summarize_text("Проверка некорректно заданной максимальной длины", 50,5000)
            self.assertEqual(result, f'Минимальное количество символов в статье {min_leght}')
            self.assertEqual(fake_output.getvalue(), '')


if __name__ == '__main__':
    unittest.main()