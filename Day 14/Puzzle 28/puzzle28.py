from enum import Enum

class LocationType(Enum):
    AIR = 0
    ROCK = 1
    SAND = 2

class Location:
    def __init__(self, type = LocationType.AIR):
        self.type = type

    def set_location_type(self, location_type):
        self.type = location_type
    
    def get_location_type(self):
        return self.type

class Scan:
    def __init__(self, max_x, max_y):
        self.grid = self.create_grid(max_x, max_y)

    def create_grid(self, max_x, max_y):
        return [[Location() for _ in range(max_x + 2)] for _ in range(max_y + 2)]
    
    def get_location_type(self, x, y):
        return self.grid[y][x].get_location_type()

    def set_location_type(self, x, y, new_type):
        self.grid[y][x].set_location_type(new_type)

    def update_grid(self, start_x, start_y, end_x, end_y):
        if start_x != end_x:
            if start_x > end_x: start_x, end_x = end_x, start_x
            for i in range(end_x - start_x + 1):
                self.set_location_type(start_x + i, start_y, LocationType.ROCK)
        else:
            if start_y > end_y: start_y, end_y = end_y, start_y
            for i in range(end_y - start_y + 1):
                self.set_location_type(start_x, start_y + i, LocationType.ROCK)

rock_formations = []
for line in open("input.txt", "r"):
    rock_formations.append(line.strip().split(" -> "))

max_x = 0
max_y = 0
for path in rock_formations:
    for node in path:
        temp_x = int(node.split(',')[0])
        temp_y = int(node.split(',')[1])
        if temp_x > max_x: max_x = temp_x
        if temp_y > max_y: max_y = temp_y

print(max_x, max_y)

scan = Scan(max_x, max_y)

print(len(scan.grid[0]), len(scan.grid))

for formation in rock_formations:
    for index in range(len(formation)-1):
        scan.update_grid(int(formation[index].split(',')[0]), int(formation[index].split(',')[1]), int(formation[index+1].split(',')[0]), int(formation[index+1].split(',')[1]))

sand_has_reached_origin = False
current_x = 500
current_y = 0

while not sand_has_reached_origin:
    # print(current_x, current_y)
    if scan.get_location_type(current_x, current_y + 1) == LocationType.AIR:
        current_y += 1
    elif scan.get_location_type(current_x - 1, current_y + 1) == LocationType.AIR:
        current_y += 1
        current_x -= 1
    elif scan.get_location_type(current_x + 1, current_y + 1) == LocationType.AIR:
        current_y += 1
        current_x += 1
    else:
        scan.set_location_type(current_x, current_y, LocationType.SAND)
        if current_x == 500 and current_y == 0: sand_has_reached_origin = True
        else:
            current_x = 500
            current_y = 0

sand_count = 0

for row in scan.grid:
    for node in row:        
        if node.type == LocationType.SAND: sand_count += 1
        
print("Sand Count: ", sand_count)

temp_f = open('temp.txt', 'a')

for row in scan.grid:
    node_str = ''
    for node in row:        
        if node.type == LocationType.AIR: node_str += '.'
        elif node.type == LocationType.ROCK: node_str += '#'
        else: node_str += 'o'
    temp_f.write(node_str)
    temp_f.write('\n')

temp_f.close()