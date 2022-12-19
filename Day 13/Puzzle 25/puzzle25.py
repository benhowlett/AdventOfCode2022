import json

def compare_signals(left_signal, right_signal):
    correct_order = True
    right_is_shorter = False

    if len(left_signal) > len(right_signal):
        items = len(right_signal)
        right_is_shorter = True
    else:
        items = len(left_signal)

    for index in range(items):
        if type(left_signal[index]) is int and type(right_signal[index]) is int:
            if left_signal[index] < right_signal[index]:
                break
            elif left_signal[index] > right_signal[index]:
                return False  

            if index + 1 == items:
                if right_is_shorter:
                    return False           

        elif type(left_signal[index]) is list and type(right_signal[index]) is list:
            if compare_signals(left_signal[index], right_signal[index]):
                if len(right_signal[index]) < len(left_signal[index]):
                    correct_order = False
            else:
                correct_order = False
        else:
            if type(left_signal[index]) is int:
                correct_order = compare_signals([left_signal[index]], right_signal[index])
            else:
                temp_list = [right_signal[index]]
                correct_order = compare_signals(left_signal[index], [right_signal[index]])

    return correct_order

signals = []
sum_of_indices = 0
index = 1

for line in open('input.txt', 'r'):
    if line != '\n':
        signals.append(json.loads(line.strip()))
        if len(signals) == 2:
            if compare_signals(signals[0], signals[1]):
                sum_of_indices += index
            index += 1
            signals = []

print(str(sum_of_indices))
