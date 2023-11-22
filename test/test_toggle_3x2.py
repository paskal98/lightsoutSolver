# test_your_code.py

import unittest

from main.utils.toggle import LightToggler


class TestOnToggle(unittest.TestCase):

    def test_left_top_edge(self):
        size_row = 2
        size_column = 3
        initial_field = [0] * 6

        expected = [
            1, 1, 0,
            1, 0, 0
        ]

        toggler = LightToggler(size_row, size_column)
        result = toggler.on_toggle(0, initial_field)
        self.assertEqual(result, expected)

    def test_right_top_edge(self):
        size_row = 2
        size_column = 3
        initial_field = [0] * 6

        expected = [
            0, 1, 1,
            0, 0, 1
        ]

        toggler = LightToggler(size_row, size_column)
        result = toggler.on_toggle(2, initial_field)
        self.assertEqual(result, expected)

    def test_right_bottom_edge(self):
        size_row = 2
        size_column = 3
        initial_field = [0] * 6

        expected = [
            0, 0, 1,
            0, 1, 1
        ]

        toggler = LightToggler(size_row, size_column)
        result = toggler.on_toggle(5, initial_field)
        self.assertEqual(result, expected)

    def test_left_bottom_edge(self):
        size_row = 2
        size_column = 3
        initial_field = [0] * 6

        expected = [
            1, 0, 0,
            1, 1, 0
        ]

        toggler = LightToggler(size_row, size_column)
        result = toggler.on_toggle(3, initial_field)
        self.assertEqual(result, expected)

    def test_middle_top(self):
        size_row = 2
        size_column = 3
        initial_field = [0] * 6

        expected = [
            1, 1, 1,
            0, 1, 0
        ]

        toggler = LightToggler(size_row, size_column)
        result = toggler.on_toggle(1, initial_field)
        self.assertEqual(result, expected)

    def test_middle_bottom(self):
        size_row = 2
        size_column = 3
        initial_field = [0] * 6

        expected = [
            0, 1, 0,
            1, 1, 1
        ]

        toggler = LightToggler(size_row, size_column)
        result = toggler.on_toggle(4, initial_field)
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
