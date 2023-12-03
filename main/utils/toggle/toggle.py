
class LightToggler:
    def __init__(self, size_row, size_column):
        self.size_row = size_row
        self.size_column = size_column

    def xor(self, cell):
        return cell ^ 1


    def get_indxs(self, cell_index):
        indxs = []

        if cell_index - self.size_column >= 0:
            indxs.append(cell_index - self.size_column)

        if cell_index + self.size_column < self.size_row * self.size_column:
            indxs.append(cell_index + self.size_column)

        if cell_index % self.size_column != 0:
            indxs.append(cell_index - 1)

        if (cell_index + 1) % self.size_column != 0:
            indxs.append(cell_index + 1)
        return indxs

    def on_toggle(self, cell_index, field):

        field[cell_index] = self.xor(field[cell_index])

        for fit_indx in self.get_indxs(cell_index):
            field[fit_indx] = self.xor(field[fit_indx])
        return field