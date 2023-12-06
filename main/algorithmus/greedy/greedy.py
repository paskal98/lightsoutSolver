import math

import numpy as np
import heapq
import time

from main.algorithmus.heuristic.gaus import get_heuristic_solution
from main.utils.toggle.toggle import LightToggler


class GreedySearch:
    def __init__(self, size_row, size_column, input_field, event_bus):
        self.input_field = input_field
        self.size_row = size_row
        self.size_column = size_column
        self.cells_count = size_row * size_column
        self.eventBus = event_bus

    def is_solved(self, field):
        return all(cell == 0 for cell in field)

    def coefficient(self, current_field, moves):
        nonzero_count = np.count_nonzero(current_field)
        return 1 + (self.cells_count / 100) + (nonzero_count / self.cells_count) + (moves / 10)

    def solve(self):
        toggler = LightToggler(self.size_row, self.size_column)

        heap = []
        priority = ((get_heuristic_solution(self.input_field.copy(), self.size_row, self.size_column)) == 1).sum()
        heapq.heappush(heap, (0, priority, self.input_field.copy(), ([0] * self.cells_count)))

        start_time = time.time()
        m = 0

        while heap:
            price, idx, current, toggled = heapq.heappop(heap)
            self.eventBus.publish('test', current)

            for cell_index in range(self.cells_count - 1, -1, -1):
                init_field = toggler.on_toggle(cell_index, current.copy())
                init_toggled = toggled.copy()
                init_toggled[cell_index] = 1

                priority = ((get_heuristic_solution(init_field, self.size_row, self.size_column)) == 1).sum()
                coefficient = self.coefficient(init_field, idx)

                heapq.heappush(heap, (priority + (price / coefficient * math.sqrt(self.size_row)), idx + 1, init_field, init_toggled))
                m += 1
                

                if self.is_solved(init_field):
                    price, idx, current, toggled = heapq.heappop(heap)
                    end_time = time.time()
                    execution_time = end_time - start_time
                    print(f"Iteration of solution: {m}")
                    print(f"Execution Time:        {execution_time} seconds")

                    return execution_time, toggled, None



