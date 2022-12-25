import json

def compare_signals(left_signal, right_signal):
    if type(left_signal) is int and type(right_signal) is int:
        if left_signal < right_signal: return True
        elif right_signal < left_signal: return False
    else:
        temp_l = left_signal
        temp_r = right_signal
        if type(left_signal) is int: temp_l = [left_signal]
        if type(right_signal) is int: temp_r = [right_signal]
        if len(temp_l) == 0: return True
        for i in range(len(temp_l)):
            if i == len(temp_r): return False
            res =  compare_signals(temp_l[i], temp_r[i])
            if res in [True, False]: return res
        if len(temp_l) < len(temp_r): return True

signals = []

for line in open('input.txt', 'r'):
    if line != '\n':
        signals.append(json.loads(line.strip()))

n = len(signals)

for i in range(n):
    already_sorted = True
    for j in range(0, n-i-1):
        if not compare_signals(signals[j], signals[j+1]):
            signals[j], signals[j+1] = signals[j+1], signals[j]
            already_sorted = False
    if already_sorted: break

print(signals.index([[2]])+1)
print(signals.index([[6]])+1)

print((signals.index([[2]])+1)*(signals.index([[6]])+1))