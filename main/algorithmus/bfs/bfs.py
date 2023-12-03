import time
from main.utils.toggle.toggle import LightToggler


def filed_data(field, iteration):
    return {
        'filed': field,
        'iteration': iteration + 1
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

        #  stack of stacks
        main_stack = {
            'stack': [({'filed': [0] * self.cells_count, 'iteration': 0}, set())],
            'combos': []
        }

        escape_loop = False
        toggle_combination = []

        # Start measuring time
        start_time = time.time()

        numbers =0

        # ended by reach the all nodes of tree
        while main_stack['stack']:


            # prev step
            visited = main_stack['stack'][-1][1]

            # get combo for iteration onto
            combo = main_stack['stack'].pop()[0]

            #  current filed toggled position
            state = combo['filed']

            # used to creation combination in node order
            iterator_indx = combo['iteration']

            # while dont reach max of lenght of field matrix
            if iterator_indx < self.cells_count:

                #  check if can be iterated and go to next leaf
                if tuple(state) not in visited:

                    visited.add(tuple(state))

                    main_stack['combos'].append(state.copy())

                    #  main of creation combos in tree like set
                    for i in range(self.cells_count - 1, iterator_indx - 1, -1):
                        new_states = state.copy()
                        new_states[i] = 1

                        main_stack['stack'].append(
                            (
                                filed_data(new_states, i),
                                visited.copy()
                            )
                        )

                        # Check if combination solve problem
                        init_field = ([0] * self.cells_count)
                        for cell_index in range(self.cells_count):
                            if new_states[cell_index] == 1:
                                init_field = toggler.on_toggle(cell_index, init_field.copy())

                        # Save combination to solve
                        if self.is_solved(init_field):
                            toggle_combination.append(new_states)
                            # print("solved")
                            escape_loop = True
                            break

                        numbers = numbers + 1
                        # if numbers % 250000 == 0:
                        #     print(f"{numbers} {main_stack['combos'][-1]}")

            # go through next branch
            elif tuple(state) not in visited:
                main_stack['combos'].append(state)

                # Check if combination solve problem
                init_field = ([0] * self.cells_count)
                for cell_index in range(self.cells_count):
                    if new_states[cell_index] == 1:
                        init_field = toggler.on_toggle(cell_index, init_field.copy())

                # Save combination to solve
                if self.is_solved(init_field):
                    toggle_combination.append(new_states)
                    # print("solved")
                    break
                numbers = numbers + 1
                # if numbers % 250000 == 0:
                #     print(f"{numbers} {main_stack['combos'][-1]}")

            if escape_loop:
                break

        print(f"Iteration of solution (node): {numbers}")

        # End measuring time
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Execution Time:               {execution_time} seconds")

        return execution_time, toggle_combination, main_stack['combos']
