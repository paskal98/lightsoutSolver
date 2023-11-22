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


    def test_gauss_eliminator_8x8_1(self):
        init_field = [
            1, 1, 0, 1, 1, 0, 0, 0,
            1, 0, 1, 0, 1, 0, 0, 0,
            0, 1, 1, 1, 0, 0, 0, 0,
            1, 0, 1, 0, 1, 0, 0, 0,
            1, 1, 0, 1, 1, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0

        ]
        size_row = 8
        size_column = 8

        expected = [0] * size_row * size_column
        solution_combination = get_heuristic_solution(init_field, size_row, size_column)

        toggler = LightToggler(size_row, size_column)
        for i in range(len(solution_combination)):
            if solution_combination[i] == 1:
                init_field = toggler.on_toggle(i, init_field.copy())

        self.assertEqual(init_field, expected)


    def test_gauss_eliminator_10x10_1(self):
        init_field = [
            1, 1, 0, 0, 0, 0, 0, 0, 0, 0,
            1, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            1, 1, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0

        ]
        size_row = 10
        size_column = 10
        expected = [0] * size_row * size_column
        solution_combination = get_heuristic_solution(init_field, size_row, size_column)

        toggler = LightToggler(size_row, size_column)
        for i in range(len(solution_combination)):
            if solution_combination[i] == 1:
                init_field = toggler.on_toggle(i, init_field.copy())

        self.assertEqual(init_field, expected)


    def test_gauss_eliminator_20x20_1(self):
        size_row = 25
        size_column = 25
        init_field = [0] * size_row * size_column
        init_field[0] = 1
        init_field[20] = 1
        init_field[30] = 1
        init_field[31] = 1

        expected = [0] * size_row * size_column
        solution_combination = get_heuristic_solution(init_field, size_row, size_column)

        toggler = LightToggler(size_row, size_column)
        for i in range(len(solution_combination)):
            if solution_combination[i] == 1:
                init_field = toggler.on_toggle(i, init_field.copy())

        self.assertEqual(init_field, expected)

    def test_gauss_eliminator_9x9_1(self):
        size_row = 9
        size_column = 9
        init_field = [0] * size_row * size_column
        init_field[30] = 1
        init_field[31] = 1
        init_field[32] = 1

        init_field[39] = 1
        init_field[40] = 1
        init_field[41] = 1

        init_field[48] = 1
        init_field[49] = 1
        init_field[50] = 1

        expected = [0] * size_row * size_column
        solution_combination = get_heuristic_solution(init_field, size_row, size_column)

        toggler = LightToggler(size_row, size_column)
        for i in range(len(solution_combination)):
            if solution_combination[i] == 1:
                init_field = toggler.on_toggle(i, init_field.copy())

        self.assertEqual(init_field, expected)

    def test_gauss_eliminator_2x3_1(self):
        init_field = [
            1, 0, 1,
            1, 0, 1
        ]
        size_row = 2
        size_column = 3

        expected = [0] * size_row * size_column
        solution_combination = get_heuristic_solution(init_field, size_row, size_column)

        toggler = LightToggler(size_row, size_column)
        for i in range(len(solution_combination)):
            if solution_combination[i] == 1:
                init_field = toggler.on_toggle(i, init_field.copy())

        self.assertEqual(init_field, expected)

    def test_gauss_eliminator_2x3_2(self):
        init_field = [
            1, 0, 1,
            0, 0, 0
        ]
        size_row = 2
        size_column = 3

        expected = [0] * size_row * size_column
        solution_combination = get_heuristic_solution(init_field, size_row, size_column)

        toggler = LightToggler(size_row, size_column)
        for i in range(len(solution_combination)):
            if solution_combination[i] == 1:
                init_field = toggler.on_toggle(i, init_field.copy())

        self.assertEqual(init_field, expected)

    def test_gauss_eliminator_2x3_3(self):
        init_field = [
            1, 1, 0,
            0, 0, 1
        ]
        size_row = 2
        size_column = 3

        expected = [0] * size_row * size_column
        solution_combination = get_heuristic_solution(init_field, size_row, size_column)

        toggler = LightToggler(size_row, size_column)
        for i in range(len(solution_combination)):
            if solution_combination[i] == 1:
                init_field = toggler.on_toggle(i, init_field.copy())

        self.assertEqual(init_field, expected)

    def test_gauss_eliminator_2x3_4(self):
        init_field = [
            0, 1, 0,
            0, 1, 0
        ]
        size_row = 2
        size_column = 3

        expected = [0] * size_row * size_column
        solution_combination = get_heuristic_solution(init_field, size_row, size_column)

        toggler = LightToggler(size_row, size_column)
        for i in range(len(solution_combination)):
            if solution_combination[i] == 1:
                init_field = toggler.on_toggle(i, init_field.copy())

        self.assertEqual(init_field, expected)

    def test_gauss_eliminator_2x3_5(self):
        init_field = [
            1, 1, 1,
            1, 1, 1
        ]
        size_row = 2
        size_column = 3

        expected = [0] * size_row * size_column
        solution_combination = get_heuristic_solution(init_field, size_row, size_column)

        toggler = LightToggler(size_row, size_column)
        for i in range(len(solution_combination)):
            if solution_combination[i] == 1:
                init_field = toggler.on_toggle(i, init_field.copy())

        self.assertEqual(init_field, expected)