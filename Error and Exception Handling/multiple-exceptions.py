# try:
#     with open("file.txt", "r") as file:
#         print(file.read())
# except (FileNotFoundError, PermissionError) as e:
#     print(e)

try:
    with open("file.txt", "r") as file:
        print(file.read())
except FileNotFoundError:
    print("The file was not found.")
except PermissionError:
    print("You do not have permission to read the file.")
