from combos import toggler

cells_count = 25
state = [1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0, 0, 1, 1, 1, 1, 0]

init_field = ([0] * cells_count)

for cell_index in range(cells_count):
    if state[cell_index] == 1:
        init_field = toggler.on_toggle(cell_index, init_field.copy())

print(init_field)
print("asdas")