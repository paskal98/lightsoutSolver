import time

from main.utils.toggle.toggle import LightToggler


def filed_data(field, iteration):
    return {
        'filed': field,
        'iteration': iteration + 1
    }

class GreedySearch:
    step_by_step_solution = []

    def __init__(self, size_row, size_column, input_field):
        self.input_field = input_field
        self.size_row = size_row
        self.size_column = size_column
        self.cells_count = size_row * size_column

    def is_solved(self, field):
        return all(cell == 0 for cell in field)

    def heuristic(self, current_field, target_field):
        mismatch_count = 0
        for current, target in zip(current_field, target_field):
            if current != target:
                mismatch_count += 1
        return mismatch_count

    def solve(self):
        toggler = LightToggler(self.size_row, self.size_column)
        toggle_combination = [(0,self.input_field.copy(),0)]
        stack = [(0,self.input_field.copy(),0)]

        # Start measuring time
        start_time = time.time()

        m=0
        escape = False
        while True:

            idx, current, price = stack.pop()



            temp_stack = []
            for cell_index in range(self.cells_count):
                init_field = toggler.on_toggle(cell_index, current.copy())

                cells_triggered =0
                for i in range(self.cells_count):
                    if init_field[i] == 1:
                        cells_triggered = cells_triggered + 1

                temp_stack.append((idx+1, init_field, cells_triggered+price))

                if cells_triggered==0:
                    escape=True
                    break


            ordered = sorted(temp_stack, key=lambda x: x[-1], reverse=True)
            for item in ordered:
                stack.append(item)
                if self.is_solved(item[1]):
                    break

            for i in range(len(stack)):
                if stack[i][0]==(idx):
                    if stack[i][2]<=stack[-1][2]:
                        stack.pop(i)
                        stack.append(stack[i])
                        toggle_combination.append(stack[i])
                        break

            if escape:
                break


            m=m+1






        # End measuring time
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Execution Time: {execution_time} seconds")

        return execution_time, toggle_combination, None
