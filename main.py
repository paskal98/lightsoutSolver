from algorithmus.dfs import DeepFirstSearch
from toggle import LightToggler


def print_filed(row_size, field):
    for i in range(len(field)):
        print(field[i], end="")
        if (i + 1) % row_size == 0:
            print()
    print('-------------\n')





def start(name):


    row_size = 3
    toggler = LightToggler(row_size, row_size)

    field = [
        1, 0, 0,
        1, 1, 0,
        0, 0, 1
    ]

    dfs = DeepFirstSearch(row_size,row_size,field)
    dfs.start_solve()

    # toggled_field = toggler.on_toggle(4, field)
    # print_filed(row_size, toggled_field)

    # for i in range(row_size ** 2):
    #     field = [0] * row_size ** 2
    #     toggled_field = toggler.on_toggle(i, field)
    #
    #     print_filed(row_size, toggled_field)


if __name__ == '__main__':
    start('DFS')
