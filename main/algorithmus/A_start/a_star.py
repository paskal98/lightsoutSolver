import time

from main.utils.toggle.toggle import LightToggler


def filed_data(field, iteration):
    return {
        'filed': field,
        'iteration': iteration + 1
    }

class AStar:
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

        # Start measuring time
        start_time = time.time()









        # End measuring time
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Execution Time: {execution_time} seconds")

        return execution_time, toggle_combination, None
