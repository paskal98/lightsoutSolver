from main.utils.toggle import LightToggler


def excluder(heuristic):

    ones = []
    for i in range(len(heuristic)):
        if heuristic[i] == 1:
            ones.append(i)

    combinations = []
    for i in ones:
        new_comb = heuristic.copy()
        new_comb[i] = 0
        combinations.append(new_comb)

    return combinations



def combinator(heuristic, field, size_row, size_column):
    toggler = LightToggler(size_row, size_column)

    near_possible_field = []
    possible_heuristics = excluder(heuristic)



    for item in possible_heuristics:
        init_field = field.copy()

        for i in range(len(item)):
            if item[i] == 1:
                init_field = toggler.on_toggle(i, init_field.copy())

        near_possible_field.append(init_field)

    return near_possible_field


def print_near_possible_field(near_possible_field, size_row, size_column):
    for field in near_possible_field:
        for i in range(size_row):
            row = field[i*size_column:(i+1)*size_column]
            print(' '.join(str(x) for x in row))
        print('-' * (size_column * 2))  # Separator line for visual clarity

#
# init_field = [
#         1, 0, 0,
#         0, 1, 1,
#         0, 0, 1]
#
# size_row = 3
# size_column = 3
#
# near_possible_field = combinator([0, 0, 0, 1, 0, 0, 1, 0, 1],init_field,size_row,size_column)
# print()
# print_near_possible_field(near_possible_field,size_row,size_column)