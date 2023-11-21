import time

from main.utils.toggle import LightToggler


def tree_solution_data(iterator, deep, field,toggle_cells):
    return {
        "iterator": iterator,
        "deep": deep,
        "field": field.copy(),
        "toggle_cells":toggle_cells.copy()
    }


class BreathFirstSearch:
    step_by_step_solution = []

    def __init__(self, size_row, size_column, input_field):
        self.input_field = input_field
        self.size_row = size_row
        self.size_column = size_column
        self.cells_count = size_row * size_column

    def is_solved(self, field):
        for i in range(len(self.input_field)):
            if self.input_field[i] != field[i]:
                return False
        return True


    def solve(self):
        toggler = LightToggler(self.size_row, self.size_column)

        toggle_combination = []
        queue_solution = [
            ([0] * self.cells_count)
        ]
        combinations = []

        # Start measuring time
        start_time = time.time()

        for number in range(1, 2 ** self.cells_count):
            # Combination step-by-step generator
            combination = [0] * self.cells_count
            for i in range(self.cells_count):
                if number & (1 << i):
                    combination[i] = 1
            combinations.append(combination)

            # Check if combination solve problem
            init_field = ([0] * self.cells_count)
            for cell_index in range(self.cells_count):
                if combinations[-1][cell_index] == 1:
                    init_field = toggler.on_toggle(cell_index, init_field.copy())
                    queue_solution.append(init_field)

            # Save combination to solve
            if self.is_solved(init_field):
                toggle_combination.append(combinations[-1])
                print("solved")
                break


            # if number % 250000 == 0:
            #     print(f"{number} {combinations[-1]}")

        # End measuring time
        end_time = time.time()

        execution_time = end_time - start_time
        print(f"Execution Time: {execution_time} seconds")
        return execution_time, toggle_combination, queue_solution