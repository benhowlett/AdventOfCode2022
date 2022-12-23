import json

def compare_signals(left_signal, right_signal):

    for index in range(len(left_signal)):
        if index == len(right_signal): return False
        
        if type(left_signal[index]) is int and type(right_signal[index]) is int:
            if left_signal[index] < right_signal[index]: return True
            elif left_signal[index] > right_signal[index]: return False
        else:
            if type(left_signal[index]) is int: left_signal[index] = [left_signal[index]]
            if type(right_signal[index]) is int: right_signal[index] = [right_signal[index]]
            return compare_signals(left_signal[index], right_signal[index])
    return True



signals = []
sum_of_indices = 0
index = 1

for line in open('input.txt', 'r'):
    if line != '\n':
        signals.append(json.loads(line.strip()))
        if len(signals) == 2:
            print(signals[0])
            print(signals[1])
            if compare_signals(signals[0], signals[1]):
                print("Correct order")
                sum_of_indices += index
            index += 1
            signals = []

print(str(sum_of_indices))
