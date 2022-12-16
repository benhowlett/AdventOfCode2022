import sys

class Node:
    def __init__(self, row, column, value):
        self.row = row
        self.column = column
        self.value = value
    
    def get_name(self):
        return str(self.row) + "," + str(self.column)
    
    def get_value(self):
        return self.value


def can_move(current, new):
    if current == 'S':
        current = 'a'
    elif new == 'E':
        new = 'z'
    return ord(new) - ord(current) <= 1
    

def find_shortest_path(graph, start_node):
    unvisited_nodes = list(graph.keys())
    shortest_path = {}
    previous_nodes = {}

    # set all initial paths to unvisited nodes to 'infinity'
    max_value = sys.maxsize
    for node in unvisited_nodes:
        shortest_path[node] = max_value
    # manually set shortest path to starting node to 0
    shortest_path[start_node] = 0

    while unvisited_nodes:
        # Get the unvisited node with the shortest path. Initially this will be the start node
        current_min_node = None
        for node in unvisited_nodes:
            if current_min_node == None:
                current_min_node = node
            elif shortest_path[node] < shortest_path[current_min_node]:
                current_min_node = node

        neighbours = graph[current_min_node]
        for neighbour in neighbours:
            temp_value = shortest_path[current_min_node] + 1
            if temp_value < shortest_path[neighbour]:
                shortest_path[neighbour] = temp_value
                previous_nodes[neighbour] = current_min_node

        unvisited_nodes.remove(current_min_node)

    return previous_nodes, shortest_path

def get_result(previous_nodes, shortest_path, start_node, end_node):
    path = []
    node = end_node

    if previous_nodes.get(node, False) != False:
        while node != start_node:
            path.append(node)
            node = previous_nodes[node]
    
    path.append(start_node)

    return shortest_path[end_node]

map = []
temp_row = 0

# Create a 2D array of Nodes representing the height map
for line in open('input.txt', 'r'):
    row = []
    temp_column = 0
    for item in line.strip():
        row.append(Node(temp_row, temp_column, item))
        temp_column += 1
    map.append(row)
    temp_row += 1


# Create a graph to traverse to find the shortest path
graph = {}
start_nodes = []
end_node = ""

for row in range(len(map)):
    for column in range(len(map[row])):

        node = map[row][column].get_name()
        node_value = map[row][column].get_value()
        neighbours = []

        if node_value == "S" or node_value == 'a':
            start_nodes.append(node)
        elif node_value == "E":
            end_node = node

        if row == 0:
            if can_move(node_value, map[row+1][column].get_value()):
                neighbours.append(map[row+1][column].get_name())
        elif row == len(map) - 1:
            if can_move(node_value, map[row-1][column].get_value()):
                neighbours.append(map[row-1][column].get_name())
        else:
            if can_move(node_value, map[row+1][column].get_value()):
                neighbours.append(map[row+1][column].get_name())
            if can_move(node_value, map[row-1][column].get_value()):
                neighbours.append(map[row-1][column].get_name())

        if column == 0:
            if can_move(node_value, map[row][column+1].get_value()):
                neighbours.append(map[row][column+1].get_name())
        elif column == len(map[row]) - 1:
            if can_move(node_value, map[row][column-1].get_value()):
                neighbours.append(map[row][column-1].get_name())
        else:
            if can_move(node_value, map[row][column+1].get_value()):
                neighbours.append(map[row][column+1].get_name())
            if can_move(node_value, map[row][column-1].get_value()):
                neighbours.append(map[row][column-1].get_name())
        
        graph[node] = neighbours

previous_nodes_list = []
shortest_path_list =  [] 

print("Number of start nodes: {}".format(len(start_nodes)))

times = 0

for start_node in start_nodes:
    times += 1
    print("Starting pathfinding {}".format(times))
    previous_nodes, shortest_path = find_shortest_path(graph, start_node)
    previous_nodes_list.append(previous_nodes)
    shortest_path_list.append(shortest_path)

print("Number of previous_nodes: {}".format(len(previous_nodes_list)))
print("Number of shortest_path: {}".format(len(shortest_path_list)))

results = []

for result in range(len(previous_nodes_list)):
    print("Getting result " + str(result))
    results.append(get_result(previous_nodes_list[result], shortest_path_list[result], start_nodes[result], end_node))

print(sorted(results)[0])