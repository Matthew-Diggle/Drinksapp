import unittest
from unittest.mock import Mock, patch

import Table_test

# def test_print_table(title, data):
#     width = get_table_width(title, data)
#     print_header(title, width)
#     for item in data:
#         print(f'| {item}')
#     print_separator(width)
#     wait()

class test_print_table1(unittest.TestCase):
    @patch("table_test.get_table_width", "table_test.print_header", "table_test.print_separator")

    def test_mock_print_table(self, mock_print_table, mock_get_table_width, mock_print_header, mock_print_separator):
        # arrange
        mock_get_table_width = "title, data"
        mock_print_header = "title1", "15"
        mock_print_separator = "15"
        mock_print_table.return_value = 1
        
        #act
        actual = mock_print_table(title)

        #assert
        self.assertEqual(actual, title)