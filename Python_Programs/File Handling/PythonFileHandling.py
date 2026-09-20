file_name = input("Enter file name: ")
with open(file_name, "a", encoding="utf-8") as file:
    file.write("")
print("File is ready:", file_name)
