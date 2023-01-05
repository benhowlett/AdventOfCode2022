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

print(min_x, max_x)

count_of_within_range = 0
test_row = 2000000

for x in range(min_x, max_x + 1):
    is_within_range = False
    is_a_beacon = False
    for sensor in range(len(sensors)):
        if calculate_manhattan_distance(sensors[sensor][0], sensors[sensor][1], x, test_row) <= beacon_distances[sensor]:
            # print("X Position: ", x, calculate_manhattan_distance(sensors[sensor][0], sensors[sensor][1], x, test_row), beacon_distances[sensor])
            is_within_range = True
        if beacons[sensor][0] == x and beacons[sensor][1] == test_row: is_a_beacon = True
    if is_within_range and not is_a_beacon:
        count_of_within_range += 1
            

print(count_of_within_range)