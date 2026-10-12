input = "(a+b) * (c-d)"

counter = 0
balanced = True

for ch in input:
    if ch == "(":
        counter += 1
    elif ch == ")":
        counter -= 1
        if counter < 0:
            balanced = False
            break
if balanced and counter == 0:
    print("Balanced")
else:
    print("Not balanced")