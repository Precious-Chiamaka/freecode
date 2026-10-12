matrix = [[2, 4, 6], [1, 3, 5], [10, 20, 30]]
row_number = 1

for row in matrix:
    total = 0
    for num in row:
        total += num

    print("Row", row_number, "Total:", total)
    row_number =+ 1