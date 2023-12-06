import time
from main.utils.toggle.toggle import LightToggler

def filed_data(field, iteration):
    return {
        'filed': field,
        'iteration': iteration + 1
    }

class DeepFirstSearch:
    step_by_step_solution = []
    
    def __init__(self, size_row, size_column, input_field,event_bus):
        self.input_field = input_field
        self.size_row = size_row
        self.size_column = size_column
        self.cells_count = size_row * size_column
        self.eventBus = event_bus

    def is_solved(self, field):
        for i in range(len(self.input_field)):
            if self.input_field[i] != field[i]:
                return False
        return True


    def solve(self):
        toggler = LightToggler(self.size_row, self.size_column)
        toggle_combination = []

        # start time
        start_time = time.time()

        combinations = []
        stack = [(0, [0] * self.cells_count, False)]

        n=0
        while stack:
            idx, current, visited = stack.pop()

            # When at the end of the array, if we have set a 1, add to combinations
            if idx == self.cells_count:
                if visited:
                    combinations.append(current)
                continue

            # Continue without setting the current index
            stack.append((idx + 1, current.copy(), visited))

            # Set the current index and continue
            new_current = current.copy()
            new_current[idx] = 1
            stack.append((idx + 1, new_current, True))

            # Check if combination solve problem
            init_field = ([0] * self.cells_count)
            for cell_index in range(self.cells_count):
                if new_current[cell_index] == 1:    
                    init_field = toggler.on_toggle(cell_index, init_field.copy())
                    self.eventBus.publish('test',init_field)

            # Save combination to solve
            if self.is_solved(init_field):
                toggle_combination.append(new_current)
                # print("solved")
                break
            n=n+1

        print(f"Iteration of solution (node): {n}")


        # End measuring time
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Execution Time:               {execution_time} seconds")

        return execution_time, toggle_combination, combinations


