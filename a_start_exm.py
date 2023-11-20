class Node:
    def __init__(self, data):
        self.data = data
        self.children = []


    def add_child(self, child_node, price):
        self.children.append(
            {
                'child': child_node,
                'price': price
            }
        )

    def print_graph(self, visited=None):
        if visited is None:
            visited = set()

        # Print the current node and its children
        connections = ', '.join([f"{child['child'].data} (price: {child['price']})" for child in self.children])
        print(f"{self.data} -> {connections}")

        # Mark this node as visited
        visited.add(self)

        # Recursive call for each unvisited child
        for child in self.children:
            if child['child'] not in visited:
                child['child'].print_graph(visited)

    def is_neighbor(self, other_node):
        for child in self.children:
            if child['child'].data == other_node.data:
                return True
        return False



def are_neighbors(node1, node2):
    return node1.is_neighbor(node2)

def is_present(node,stack):
    exists = False
    for s in stack:
        if node == s:
            exists = True
    return exists

def get_neighbours(current_node):
    neighbour = []
    for node in current_node.children:
        neighbour.append(node['child'])


# Create nodes
a_node = Node("A")
b_node = Node("B")
c_node = Node("C")
g_node = Node("G")
f_node = Node("F")
e_node = Node("E")

# Add children
a_node.add_child(b_node, 1)
b_node.add_child(a_node, 1)

a_node.add_child(c_node, 2)
c_node.add_child(a_node, 2)

b_node.add_child(c_node, 3)
c_node.add_child(b_node, 3)

c_node.add_child(g_node, 2)
g_node.add_child(c_node, 2)

b_node.add_child(g_node, 4)
g_node.add_child(b_node, 4)

b_node.add_child(f_node, 2)
f_node.add_child(b_node, 2)

b_node.add_child(e_node, 4)
e_node.add_child(b_node, 4)

f_node.add_child(e_node, 1)
e_node.add_child(f_node, 1)

g_node.add_child(e_node, 2)
e_node.add_child(g_node, 2)

nodes = [a_node, b_node, c_node, e_node, g_node, f_node]

a_node.print_graph()



def get_price(start_node, destination_node):
    node = start_node
    stack = []












ways = []


price = get_price(a_node, e_node)
print(price)


























def print_data(stack):

    for item in stack:
        print(item.data, end=" ")
    print()



def get_price1(start_node, dest_node):
    stack = [start_node]
    price = 0
    last_popped = []
    print(len(last_popped))
    all_possible = False
    while True:



        if stack[-1].data == dest_node.data or all_possible == True:

            if stack[-1].data == dest_node.data:
                path =[]
                for s in stack:
                    path.append(s.data)
                ways.append(path)
                stack.pop()
            print_data(stack)

            any_neighbour = None
            for n in stack[-1].children:
                if not is_present(n['child'],stack) and n['child'].data != dest_node.data and not is_present(n['child'],last_popped) :
                    any_neighbour = n
                    stack.append(n['child'])
                    break

            if any_neighbour == None:
                last_popped.append(stack.pop())
                print_data(stack)

            if len(last_popped)>1:
                last_popped.pop(0)



        all_possible = True
        for node in nodes:
            if stack[-1].data == dest_node.data:
                all_possible = False
                break
            if are_neighbors(stack[-1], node) and node not in stack:
                if len(last_popped) == 0:
                    stack.append(node)
                    all_possible = False
                elif not is_present(node,last_popped):
                    stack.append(node)
                    all_possible = False



    return price



