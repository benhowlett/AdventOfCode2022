from tqdm import tqdm

def calculate_manhattan_distance(source_x, source_y, target_x, target_y) -> int:
    return abs(source_x - target_x) + abs(source_y - target_y)

sensors = []
beacons = []

for line in open("input.txt", "r"):
    sensors.append((int(line.strip().split()[2].split("=")[1].replace(",", "")), int(line.strip().split()[3].split("=")[1].replace(":", ""))))
    beacons.append((int(line.strip().split()[8].split("=")[1].replace(",", "")), int(line.strip().split()[9].split("=")[1])))

beacon_distances = []
min_x = 10000000
max_x = 0

for i in range(len(sensors)):
    beacon_distances.append(calculate_manhattan_distance(sensors[i][0], sensors[i][1], beacons[i][0], beacons[i][1]))
    if sensors[i][0] - beacon_distances[i] < min_x: min_x = sensors[i][0] - beacon_distances[i]
    if sensors[i][0] + beacon_distances[i] > max_x: max_x = sensors[i][0] + beacon_distances[i]

# print(min_x, max_x)

max_coordinate = 4000000

for i in tqdm(range(len(sensors))):
    for x in tqdm(range(sensors[i][0] - beacon_distances[i] - 1, sensors[i][0] + beacon_distances[i] + 2)):
        top_is_covered = False
        bottom_is_covered = False
        x_is_in_range = False
        top_y_is_in_range = False
        bottom_y_is_in_range = False

        if x == sensors[i][0] - beacon_distances[i] - 1 or x == sensors[i][0] + beacon_distances[i] + 1: 
            top_y = sensors[i][1]
            bottom_y = sensors[i][1]
        else:
            top_y = sensors[i][1] - ((beacon_distances[i] - abs(sensors[i][0] - x)) + 1)
            bottom_y = sensors[i][1] + (beacon_distances[i] - abs(sensors[i][0] - x)) + 1
        
        # print("Top - x:", x, ", y:", top_y)
        # print("Bottom - x:", x, ", y:", bottom_y)

        if x >= 0 and x <= max_coordinate:
            x_is_in_range = True
            if top_y >= 0 and top_y <= max_coordinate:
                top_y_is_in_range = True
                for j in range(len(sensors)):
                    if sensors[i] != sensors[j]:
                        if calculate_manhattan_distance(sensors[j][0], sensors[j][1], x, top_y) <= beacon_distances[j]: 
                            top_is_covered = True
                            # print(x, top_y, calculate_manhattan_distance(sensors[j][0], sensors[j][1], x, top_y), beacon_distances[j])
                        
            if bottom_y >= 0 and bottom_y <= max_coordinate:
                bottom_y_is_in_range = True
                for j in range(len(sensors)):
                    if sensors[i] != sensors[j]:
                        if calculate_manhattan_distance(sensors[j][0], sensors[j][1], x, bottom_y) <= beacon_distances[j]: 
                            bottom_is_covered = True          
                            # print(x, bottom_y, calculate_manhattan_distance(sensors[j][0], sensors[j][1], x, bottom_y), beacon_distances[j])
                        
        if not top_is_covered and x_is_in_range and top_y_is_in_range: print("Found coordinates:" + str(x) + ", " + str(top_y) + ". Tuning frequency: " + str((x * 4000000) + top_y))
        elif not bottom_is_covered and x_is_in_range and bottom_is_covered: print("Found coordinates:" + str(x) + ", " + str(bottom_y) + ". Tuning frequency: " + str((x * 4000000) + bottom_y))


# count_of_within_range = 0
# found_x = 0
# found_y = 0

# for test_row in tqdm(range(max_coordinate + 1)):
#     coordinates_found = False
#     for x in tqdm(range(max_coordinate + 1)):
#         # if test_row % 10000 == 0 and x % 10000 == 0:
#         #     print("Row:", test_row, "Column:", x)
#         is_within_range = False
#         for sensor in range(len(sensors)):
#             if abs(test_row - sensors[sensor][1]) <= beacon_distances[sensor]:
#                 if calculate_manhattan_distance(sensors[sensor][0], sensors[sensor][1], x, test_row) <= beacon_distances[sensor]:
#                     # print("X Position: ", x, calculate_manhattan_distance(sensors[sensor][0], sensors[sensor][1], x, test_row), beacon_distances[sensor])
#                     is_within_range = True
#                     break
#         if not is_within_range:
#             found_x = x
#             found_y = test_row
#             coordinates_found = True
#             break
#     if coordinates_found: break
                

# print("Found coordinates: " + str(found_x) + ", " + str(found_y) + ". Tuning frequency: " + str((found_x * 4000000) + found_y))