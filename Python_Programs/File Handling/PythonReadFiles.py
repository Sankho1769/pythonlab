file_name = input("Enter file name: ")
try:
    with open(file_name, "r", encoding="utf-8") as file:
        print(file.read())
except FileNotFoundError:
    print("File not found.")
