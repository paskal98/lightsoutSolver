import time

from toggle import LightToggler


def tree_solution_data(iterator, deep, field,toggle_cells):
    return {
        "iterator": iterator,
        "deep": deep,
        "field": field.copy(),
        "toggle_cells":toggle_cells.copy()
    }


class DeepFirstSearch:
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


    def start_solve(self):
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

        # End measuring time
        end_time = time.time()

        execution_time = end_time - start_time
        print(f"Execution Time: {execution_time} seconds")
        return execution_time, toggle_combination, queue_solution

























        # def start_solve(self):
    #     toggler = LightToggler(self.size_row, self.size_column)
    #     initial_field = [0] * (self.size_row * self.size_column)
    #
    #     deep_step = 0
    #     index_cell_toggle = 0
    #     queue = []
    #     toggled_cells = []
    #
    #     state = {
    #         "deep": -1,
    #         "field": initial_field.copy(),
    #         "toggle": -1
    #     }
    #
    #     queue.append(state)
    #     self.step_by_step_solution.append(state)
    #
    #     hard_index = 0
    #
    #     toggled_field = initial_field.copy()
    #     while True:
    #
    #
    #         # Set deep and reset toggle index of cell that can be toggled once
    #         if index_cell_toggle == ((self.size_row * self.size_column) - 1):
    #             toggled_field = toggler.on_toggle(hard_index, queue[-1]['field'].copy())
    #             toggled_cells.append(hard_index)
    #
    #             # Create State of field for stat
    #             state = {
    #                 "deep": deep_step,
    #                 "field": toggled_field.copy(),
    #                 "toggle": hard_index
    #             }
    #
    #             # Add to solver queue
    #             queue.append(state)
    #             self.step_by_step_solution.append(state)
    #             hard_index = hard_index + 1
    #
    #             if hard_index == ((self.size_row * self.size_column) - 1):
    #                 hard_index = 0
    #
    #             index_cell_toggle = 0
    #             deep_step = deep_step + 1
    #
    #         # Check if cell hasn't been toggled yet
    #         is_toggle_permit = True
    #         for i in toggled_cells:
    #             if i == index_cell_toggle:
    #                 is_toggle_permit = False
    #                 break
    #
    #         if is_toggle_permit:
    #             # toggle cell in field
    #             toggled_field = toggler.on_toggle(index_cell_toggle, queue[-1]['field'].copy())
    #             toggled_cells.append(index_cell_toggle)
    #
    #             # Create State of field for stat
    #             state = {
    #                 "deep": deep_step,
    #                 "field": toggled_field.copy(),
    #                 "toggle": index_cell_toggle
    #             }
    #
    #             # Add to solver queue
    #             queue.append(state)
    #             self.step_by_step_solution.append(state)
    #
    #             # Check if solved
    #             if self.is_solved(toggled_field) == False:
    #                 queue.pop(-1)
    #                 toggled_cells.pop(-1)
    #             else:
    #                 print("Solved")
    #                 print(queue)
    #                 return queue
    #
    #         index_cell_toggle = index_cell_toggle + 1
