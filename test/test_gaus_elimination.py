import unittest

from main.algorithmus.heuristic.gaus import get_heuristic_solution
from main.utils.toggle import LightToggler


class TestOnToggle(unittest.TestCase):

    def test_gauss_eliminator_3x3_1(self):
        init_field = [
            1, 1, 1,
            1, 0, 0,
            1, 0, 0
        ]
        size_row = 3
        size_column = 3

        expected = [0] * size_row * size_column
        solution_combination = get_heuristic_solution(init_field, size_row, size_column)

        toggler = LightToggler(size_row, size_column)
        for i in range(len(solution_combination)):
            if solution_combination[i] == 1:
                init_field = toggler.on_toggle(i, init_field.copy())

        self.assertEqual(init_field, expected)

    def test_gauss_eliminator_5x5_1(self):
        init_field= [
            1, 1, 0, 1, 1,
            1, 0, 1, 0, 1,
            0, 1, 1, 1, 0,
            1, 0, 1, 0, 1,
            1, 1, 0, 1, 1
        ]
        size_row = 5
        size_column = 5

        expected = [0] * size_row * size_column
        solution_combination = get_heuristic_solution(init_field, size_row, size_column)

        toggler = LightToggler(size_row, size_column)
        for i in range(len(solution_combination)):
            if solution_combination[i] == 1:
                init_field = toggler.on_toggle(i, init_field.copy())

        self.assertEqual(init_field, expected)

    def test_gauss_eliminator_5x5_2(self):
        init_field = [
            1, 1, 1, 1, 1,
            1, 1, 1, 1, 0,
            1, 0, 1, 0, 0,
            0, 1, 1, 0, 1,
            0, 0, 0, 0, 1
        ]
        size_row = 5
        size_column = 5

        expected = [0] * size_row * size_column
        solution_combination = get_heuristic_solution(init_field, size_row, size_column)

        toggler = LightToggler(size_row, size_column)
        for i in range(len(solution_combination)):
            if solution_combination[i] == 1:
                init_field = toggler.on_toggle(i, init_field.copy())

        self.assertEqual(init_field, expected)

    def test_gauss_eliminator_7x7_1(self):
        init_field= [
            1, 1, 0, 1, 1, 0, 0,
            1, 0, 1, 0, 1, 0, 0,
            0, 1, 1, 1, 0, 0, 0,
            1, 0, 1, 0, 1, 0, 0,
            1, 1, 0, 1, 1, 0, 0,
            0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0
        ]
        size_row = 7
        size_column = 7

        expected = [0] * size_row * size_column
        solution_combination = get_heuristic_solution(init_field, size_row, size_column)

        toggler = LightToggler(size_row, size_column)
        for i in range(len(solution_combination)):
            if solution_combination[i] == 1:
                init_field = toggler.on_toggle(i, init_field.copy())

        self.assertEqual(init_field, expected)

    def test_gauss_eliminator_3x2_1(self):
        init_field = [
            1, 0, 1,
            1, 0, 1
        ]
        size_row = 3
        size_column = 2

        expected = [0] * size_row * size_column
        solution_combination = get_heuristic_solution(init_field, size_row, size_column)

        toggler = LightToggler(size_row, size_column)
        for i in range(len(solution_combination)):
            if solution_combination[i] == 1:
                init_field = toggler.on_toggle(i, init_field.copy())

        self.assertEqual(init_field, expected)