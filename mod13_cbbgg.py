import unittest
from datetime import datetime

# Define validation functions directly within the test script

def symbol(input_symbol):
    return input_symbol.isupper() and len(input_symbol) <= 7 and input_symbol.isalpha()

def chart_type(input_chart_type):
    return input_chart_type in ["1", "2"]

def time_series(input_time_series):
    return input_time_series.isdigit() and 1 <= int(input_time_series) <= 4

def date_format(input_date):
    try:
        datetime.strptime(input_date, "%Y-%m-%d")
        return True
    except ValueError:
        return False

def date_range(start_date, end_date):
    return start_date <= end_date


class TestUserInput(unittest.TestCase):

    def test_symbol(self):
        test_symbols = ["loca", "GOOGL", "HELP", "hi", "AMZN"]
        test_result = [False, True, True, False, True]

        for input_symbol, expected_result in zip(test_symbols, test_result):
            result = symbol(input_symbol)
            self.assertEqual(result, expected_result)

    def test_chart_type(self):
        test_chart_types = ["1", "2", "0", ""]
        test_result = [True, True, False, False]

        for input_chart_type, expected_result in zip(test_chart_types, test_result):
            result = chart_type(input_chart_type)
            self.assertEqual(result, expected_result)

    def test_time_series(self):
        test_time_series_values = ["1", "2", "3", "4", "5", ""]
        test_result = [True, True, True, True, False, False]

        for input_time_series, expected_result in zip(test_time_series_values, test_result):
            result = time_series(input_time_series)
            self.assertEqual(result, expected_result)

    def test_start_date_format(self):
        start_date = "2024-01-01"
        result = date_format(start_date)
        self.assertTrue(result)

    def test_end_date_format(self):
        end_date = "2024-12-31"
        result = date_format(end_date)
        self.assertTrue(result)

    def test_date_range(self):
        start_date = datetime(2024, 1, 1)
        end_date = datetime(2024, 12, 31)
        result = date_range(start_date, end_date)
        self.assertTrue(result)

        start_date = datetime(2024, 12, 31)
        end_date = datetime(2024, 1, 1)
        result = date_range(start_date, end_date)
        self.assertFalse(result)

if __name__ == "__main__":
    unittest.main()
