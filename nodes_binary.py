def generate_custom_dfs_combos_recursive(cells_count):
    def dfs(combo, index):
        if index == cells_count:
            combinations.append(combo)
            return

        combinations.append(combo)
        for i in range(index, cells_count):
            new_combo = combo.copy()
            new_combo[i] = 1
            dfs(new_combo, i + 1)

    # Start with all zeros
    base_combo = [0] * cells_count
    combinations = []
    dfs(base_combo, 0)
    return combinations

# def generate_custom_dfs_combos_iterative(cells_count):
#     # Initialize the stack with the base combination and the starting index
#     stack = [([0] * cells_count, 0)]
#     combinations = []
#
#     while stack:
#         combo, index = stack.pop()
#         if index < cells_count:
#             # Add the current combination to the list
#             combinations.append(combo.copy())
#             # Iterate over the remaining cells
#             for i in range(cells_count - 1, index - 1, -1):
#                 # Create a new combination with the current cell set to 1
#                 new_combo = combo.copy()
#                 new_combo[i] = 1
#                 stack.append((new_combo, i + 1))
#         else:
#             # If all cells have been processed, add the final combination
#             combinations.append(combo)
#
#     return combinations

def dfs_node_combo(cells_count):

    main_stack = {
        'stack': [({'filed': [0] * cells_count, 'iteration': 0}, set())],
        'combos': []
    }

    numbers = 0

    while main_stack['stack']:

        combo, visited = main_stack['stack'].pop()

        state, iterator_indx = combo['filed'], combo['iteration']

        if iterator_indx < cells_count:

            if tuple(state) not in visited:

                visited.add(tuple(state))
                main_stack['combos'].append(state.copy())


                for i in range(cells_count-1, iterator_indx-1,-1):

                    new_states = state.copy()
                    new_states[i] = 1

                    main_stack['stack'].append(
                        (
                            {
                                'filed': new_states,
                                'iteration': i + 1
                            },
                            visited.copy()
                        )
                    )
                    numbers = numbers + 1
                    if numbers  == 10:
                        print(f"{numbers} {main_stack['combos'][-1]}")


        elif tuple(state) not in visited:
            main_stack['combos'].append(state)
            numbers = numbers + 1
            if numbers  == 10:
                print(f"{numbers} {main_stack['combos'][-1]}")

    return main_stack['combos']



# Example usage for cells_count = 3
cells_count = 25
custom_dfs_combinations = generate_custom_dfs_combos_recursive(cells_count)
custom_combinations_iterative = dfs_node_combo(cells_count)

for combo in custom_dfs_combinations:
    print(combo)


print(custom_combinations_iterative==custom_dfs_combinations)