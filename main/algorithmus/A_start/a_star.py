import heapq
import time

from main.algorithmus.heuristic.gaus import get_heuristic_solution
from main.utils.toggle.toggle import LightToggler


class AStar:
    step_by_step_solution = []

    def __init__(self, size_row, size_column, input_field, event_bus):
        self.input_field = input_field
        self.size_row = size_row
        self.size_column = size_column
        self.cells_count = size_row * size_column
        self.eventBus = event_bus


    def is_solved(self, field):
        return all(cell == 0 for cell in field)

    def solve(self):
        toggler = LightToggler(self.size_row, self.size_column)

        heap = []

        priority = ((get_heuristic_solution(self.input_field.copy(), self.size_row, self.size_column)) == 1).sum()

        heapq.heappush(heap, (0, priority, self.input_field.copy(), ([0] * self.cells_count)))

        # Start measuring time
        start_time = time.time()

        pre_solved = []

        m = 0
        escape = False
        while True:

            price, idx, current, toggled = heapq.heappop(heap)

            for cell_index in range(self.cells_count):
                init_field = toggler.on_toggle(cell_index, current.copy())

                init_toggled = toggled.copy()
                init_toggled[cell_index] = 1

                priority = ((get_heuristic_solution(init_field, self.size_row, self.size_column)) == 1).sum()

                heapq.heappush(heap, (priority, idx + 1, init_field, init_toggled))
                m = m + 1
                self.eventBus.publish('test',init_field)
                if self.is_solved(init_field):
                    escape = True
                    break



            if escape:
                break

        print(f"Iteration of solution: {m}")



        price, idx, current, toggled = heapq.heappop(heap)

        # End measuring time
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Execution Time:        {execution_time} seconds")

        return execution_time, toggled, None
