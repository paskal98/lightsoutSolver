
class LightToggler:
    def __init__(self, size_row, size_column):
        self.size_row = size_row
        self.size_column = size_column

    def xor(self, cell):
        return cell ^ 1

    def row_range(self, cell_index):
        min_range = cell_index
        while (min_range % self.size_row != 0):
            min_range -= 1

        max_range = cell_index
        while (max_range % self.size_row != 0):
            max_range += 1

        if max_range == min_range:
            min_range = cell_index
            max_range = cell_index + self.size_row

        return min_range, max_range

    def on_toggle(self, cell_index, field):
        min_range, max_range = self.row_range(cell_index)

        for i in range(self.size_column * self.size_row):
            if (i + self.size_row) == cell_index or (i - self.size_row) == cell_index:
                field[i] = self.xor(field[i])
            elif ((cell_index - 1 == i and i >= min_range) or
                  (cell_index + 1 == i and i < max_range) or
                  i == cell_index):
                field[i] = self.xor(field[i])

        return field