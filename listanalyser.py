numbers = [12, 5, 27, 8, 14]

smallest = numbers[0]
largest = numbers[0]
total = 0

for n in numbers:
    if n < smallest:
        smallest = n
    if n > largest:
        largest = n
    total += n

average = total / len(numbers)

print("Smallest:", smallest)
print("Largest:", largest)
print("Total:", total)
print("Average:", average)