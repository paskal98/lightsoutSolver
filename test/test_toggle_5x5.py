# test_your_code.py

import unittest

from main.utils import LightToggler


class TestOnToggle(unittest.TestCase):

    def test_left_top_edge(self):
        size_row = 5
        initial_field = [0] * size_row ** 2

        expected = [
            1, 1, 0, 0, 0,
            1, 0, 0, 0, 0,
            0, 0, 0, 0, 0,
            0, 0, 0, 0, 0,
            0, 0, 0, 0, 0
        ]

        toggler = LightToggler(size_row)
        result = toggler.on_toggle(0, initial_field)
        self.assertEqual(result, expected)

    def test_right_top_edge(self):
        size_row = 5
        initial_field = [0] * size_row ** 2

        expected = [
            0, 0, 0, 1, 1,
            0, 0, 0, 0, 1,
            0, 0, 0, 0, 0,
            0, 0, 0, 0, 0,
            0, 0, 0, 0, 0
        ]

        toggler = LightToggler(size_row)
        result = toggler.on_toggle(4, initial_field)
        self.assertEqual(result, expected)

    def test_right_bottom_edge(self):
        size_row = 5
        initial_field = [0] * size_row ** 2

        expected = [
            0, 0, 0, 0, 0,
            0, 0, 0, 0, 0,
            0, 0, 0, 0, 0,
            1, 0, 0, 0, 0,
            1, 1, 0, 0, 0
        ]

        toggler = LightToggler(size_row)
        result = toggler.on_toggle(20, initial_field)
        self.assertEqual(result, expected)

    def test_left_bottom_edge(self):
        size_row = 5
        initial_field = [0] * size_row ** 2

        expected = [
            0, 0, 0, 0, 0,
            0, 0, 0, 0, 0,
            0, 0, 0, 0, 0,
            0, 0, 0, 0, 1,
            0, 0, 0, 1, 1
        ]

        toggler = LightToggler(size_row)
        result = toggler.on_toggle(24, initial_field)
        self.assertEqual(result, expected)

    def test_center(self):
        size_row = 5
        initial_field = [0] * size_row ** 2

        expected = [
            0, 0, 0, 0, 0,
            0, 0, 1, 0, 0,
            0, 1, 1, 1, 0,
            0, 0, 1, 0, 0,
            0, 0, 0, 0, 0
        ]

        toggler = LightToggler(size_row)
        result = toggler.on_toggle(12, initial_field)
        self.assertEqual(result, expected)

    def test_middle_right(self):
        size_row = 5
        initial_field = [0] * size_row ** 2

        expected = [
            0, 0, 0, 0, 0,
            0, 0, 0, 0, 1,
            0, 0, 0, 1, 1,
            0, 0, 0, 0, 1,
            0, 0, 0, 0, 0
        ]

        toggler = LightToggler(size_row)
        result = toggler.on_toggle(14, initial_field)
        self.assertEqual(result, expected)

    def test_middle_left(self):
        size_row = 5
        initial_field = [0] * size_row ** 2

        expected = [
            0, 0, 0, 0, 0,
            1, 0, 0, 0, 0,
            1, 1, 0, 0, 0,
            1, 0, 0, 0, 0,
            0, 0, 0, 0, 0
        ]

        toggler = LightToggler(size_row)
        result = toggler.on_toggle(10, initial_field)
        self.assertEqual(result, expected)

    def test_middle_top(self):
        size_row = 5
        initial_field = [0] * size_row ** 2

        expected = [
            0, 1, 1, 1, 0,
            0, 0, 1, 0, 0,
            0, 0, 0, 0, 0,
            0, 0, 0, 0, 0,
            0, 0, 0, 0, 0
        ]

        toggler = LightToggler(size_row)
        result = toggler.on_toggle(2, initial_field)
        self.assertEqual(result, expected)

    def test_middle_bottom(self):
        size_row = 5
        initial_field = [0] * size_row ** 2

        expected = [
            0, 0, 0, 0, 0,
            0, 0, 0, 0, 0,
            0, 0, 0, 0, 0,
            0, 0, 1, 0, 0,
            0, 1, 1, 1, 0
        ]

        toggler = LightToggler(size_row)
        result = toggler.on_toggle(22, initial_field)
        self.assertEqual(result, expected)

    def test_top_before_middle(self):
        size_row = 5
        initial_field = [0] * size_row ** 2

        expected = [
            1, 1, 1, 0, 0,
            0, 1, 0, 0, 0,
            0, 0, 0, 0, 0,
            0, 0, 0, 0, 0,
            0, 0, 0, 0, 0
        ]

        toggler = LightToggler(size_row)
        result = toggler.on_toggle(1, initial_field)
        self.assertEqual(result, expected)

    def test_top_after_middle(self):
        size_row = 5
        initial_field = [0] * size_row ** 2

        expected = [
            0, 0, 1, 1, 1,
            0, 0, 0, 1, 0,
            0, 0, 0, 0, 0,
            0, 0, 0, 0, 0,
            0, 0, 0, 0, 0
        ]

        toggler = LightToggler(size_row)
        result = toggler.on_toggle(3, initial_field)
        self.assertEqual(result, expected)

    def test_bottom_after_middle(self):
        size_row = 5
        initial_field = [0] * size_row ** 2

        expected = [
            0, 0, 0, 0, 0,
            0, 0, 0, 0, 0,
            0, 0, 0, 0, 0,
            0, 0, 0, 1, 0,
            0, 0, 1, 1, 1
        ]

        toggler = LightToggler(size_row)
        result = toggler.on_toggle(23, initial_field)
        self.assertEqual(result, expected)

    def test_bottom_before_middle(self):
        size_row = 5
        initial_field = [0] * size_row ** 2

        expected = [
            0, 0, 0, 0, 0,
            0, 0, 0, 0, 0,
            0, 0, 0, 0, 0,
            0, 1, 0, 0, 0,
            1, 1, 1, 0, 0
        ]

        toggler = LightToggler(size_row)
        result = toggler.on_toggle(21, initial_field)
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
