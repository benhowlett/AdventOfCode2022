class Item:
    def __init__(self, worry_level, monkey_number):
        self.worry_level = int(worry_level)
        self.monkey_number = int(monkey_number)

    def setWorryLevel(self, new_worry_level):
        self.worry_level = int(new_worry_level)
    
    def getWorryLevel(self):
        return int(self.worry_level)

    def setMonkey(self, new_monkey_number):
        self.monkey_number = int(new_monkey_number)
    
    def getMonkey(self):
        return int(self.monkey_number)

class Monkey:
    def __init__(self, starting_items, inspection_operation, inspection_modifier, test_divisor, true_monkey_number, false_monkey_number):
        self.items = starting_items
        self.inspection_operation = inspection_operation
        self.inspection_modifier = inspection_modifier
        self.test_divisor = test_divisor
        self.true_monkey_number = true_monkey_number
        self.false_monkey_number = false_monkey_number
        self.items_inspected = 0
    
    def getItemCount(self):
        return len(self.items)

    def getItemsInspected(self):
        return self.items_inspected

    def inspectItem(self, factor):
        if self.getItemCount() == 0:
            return None
        else:
            self.items_inspected += 1
            item = self.items[0]
            item_worry_level = item.getWorryLevel()

            if self.inspection_operation == "*":
                if self.inspection_modifier == "old":
                    item_worry_level = (item_worry_level * item_worry_level) % factor
                else:
                    item_worry_level *= int(self.inspection_modifier)
            else:
                item_worry_level += int(self.inspection_modifier)
            
            if item_worry_level % self.test_divisor == 0:
                item.setMonkey(self.true_monkey_number)
            else:
                item.setMonkey(self.false_monkey_number)

            item.setWorryLevel(item_worry_level)

            del self.items[0]

            return item
        
    def addItem(self, new_item):
        self.items.append(new_item)

temp_monkey_data = []
monkeys = []
factor = 1

# Create the monkeys!
with open('input.txt', 'a') as input:
    input.write("\n")
    input.close()

for line in open('input.txt', 'r'):
    if line != "\n":
        temp_monkey_data.append(line.strip().split())
    else:
        temp_items = []
        temp_operation = ""
        temp_modifier = ""
        temp_test_divisor = 0
        temp_true_monkey_number = 0
        temp_false_monkey_number = 0
        for row in temp_monkey_data:
            if row[0] == "Starting":
                for item in range(2, len(row)):
                    temp_items.append(Item(int(row[item].replace(",", "")), len(monkeys)))
            elif row[0] == "Operation:":
                temp_operation = row[4]
                temp_modifier = row[5]
            elif row[0] == "Test:":
                temp_test_divisor = int(row[3])
                factor *= temp_test_divisor
            elif row[0] == "If":
                if row[1] == "true:":
                    temp_true_monkey_number = int(row[5])
                elif row[1] == "false:":
                    temp_false_monkey_number = int(row[5])
        monkeys.append(Monkey(temp_items, temp_operation, temp_modifier, temp_test_divisor, temp_true_monkey_number, temp_false_monkey_number))
        temp_monkey_data = []

# Run 10000 rounds of simulation
for round in range(10000):
    print("Round " + str(round))
    for monkey in monkeys:
        while len(monkey.items) > 0:
            current_item = monkey.inspectItem(factor)
            monkeys[current_item.getMonkey()].addItem(current_item)

monkey_activity = []

for monkey in monkeys:
    monkey_activity.append(monkey.getItemsInspected())
#print(monkey_activity)
monkey_activity.sort(reverse=True)

print(monkey_activity[0]*monkey_activity[1])