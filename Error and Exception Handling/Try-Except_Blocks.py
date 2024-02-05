while True:
    while True:
        num1 = input("Enter first number: ")
        try:
            num1 = float(num1)
            break
        except ValueError:
            print(f"'{num1}' is not a number")

    while True:
        num2 = input("Enter second number: ")
        try:
            num2 = float(num2)
            break
        except ValueError:
            print(f"'{num2}' is not a number")

    try:
        div = num1 / num2
        print(f"{num1} / {num2} = {round(div, 2)}")
        break
    except ZeroDivisionError:
        print("Cannot Divide by zero")