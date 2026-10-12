values = [14, 7, 22, 9, 7, 31]
target = 14

found = 0

for i in range(len(values)):
    if values[i] == target:
        print("Found at index", i)
        found = 1
        break
if found == 0:
        print("Target not found")