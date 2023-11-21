import time

from toggle import LightToggler


def get_toggled_filed(combo,size):
    init_field = [0] * size
    for i in range(len(combo)):
        if combo[i]==1:
            init_field = toggler.on_toggle(i, init_field.copy())
    return init_field

def print_filed(field, size_row):
    for i in range(len(field)):
        print(f"{field[i]} ", end="")
        if (i+1)%size_row==0:
            print()


def remove_duplicates(arr):
    seen = set()
    result = []
    for item in arr:
        # Convert unhashable items (like lists) to a hashable type (like tuple)
        hashable_item = tuple(item) if isinstance(item, list) else item

        if hashable_item not in seen:
            seen.add(hashable_item)
            result.append(item)

        if len(arr) % 250000==0:
            print(f"dup now: {len(arr)}")
    return result


def generate_combos(cells_count):
    combinations = []
    for number in range(1, 2 ** cells_count):
        # Combination step-by-step generator
        combination = [0] * cells_count
        for i in range(cells_count):
            if number & (1 << i):
                combination[i] = 1
        combinations.append(combination)
        if len(combinations) % 250000==0 and cells_count > 16:
            print(f"combos now: {len(combinations)}")
        print(combination)
    return combinations




fields = []
size_row = 3
size_column = 2

toggler = LightToggler(size_row, size_column)

start_time = time.time()
combos = generate_combos(size_row*size_column)
end_time = time.time()

execution_time = end_time - start_time
print(f"Execution Time of creation combinatios: {execution_time} seconds")


for i in combos:
    fields.append(get_toggled_filed(i,size_row*size_column))

# print(f"Lenght before remove dup {len(fields)}")
#
# start_time = time.time()
# fields = remove_duplicates(fields.copy())
# end_time = time.time()
# print(f"Execution Time of removing duplications: {execution_time} seconds")
#
# print(f"Lenght after remove dup {len(fields)}")

# for f in fields:
#     print_filed(f,size_row)
#     print()





