total, history = 0.0, []
ops = {"+": lambda a, b: a + b, "-": lambda a, b: a - b, 
       "/": lambda a, b: a / b, "*": lambda a, b: a * b}

while True:
    parts = input("> ").split()

    if parts == ["quit"]:
        break
    elif parts == ["undo"]:
        if not history:
            print("Nothing to Undo")
            continue
        total = history.pop()
    elif len(parts) == 2 and parts[0] in ops:
        try:
            new = ops[parts[0]](total, float(parts[1]))
        except ValueError:
            print("Invalid number")
            continue
        except ZeroDivisionError:
            print("Cannot Divide by zero")
            continue
        history.append(total)
        total = new
    else:
        print("Invalid input, use: <+ - * /> <number>, undo, or quit")
        continue
    print("Result:", int(total) if total.is_integer() else total)
