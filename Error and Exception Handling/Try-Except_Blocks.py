def get_number(message):
    while True:
        num = input(message)
        try:
            return float(num)
        except ValueError:
            if num.lower() in ["q", "quit"]:
                return num
            print(f"'{num}' is not a valid number")

while True:
    num1 = get_number("Enter 1st number: ")
    if num1 in ["q", "quit"]:
        break

    num2 = get_number("Enter 2nd number: ")
    if num2 in ["q", "quit"]:
        break

    try:
        div = num1 / num2 # type: ignore
        print(f"{num1} / {num2} = {round(div, 2)}")
    except ZeroDivisionError:
        print("Cannot Divide by zero")

    if input("Do you wish to continue? (Y / N): ").lower() in ["n", "no"]:
        break
