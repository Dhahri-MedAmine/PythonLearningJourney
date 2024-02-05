file = None
try:
    file = open("file.txt", "w+")
    user_input = input()
    file.write(user_input)
except (FileNotFoundError, PermissionError) as e:
    print(e)
finally:
    if file is not None:
        print(f"{file.read()}")
        file.close()