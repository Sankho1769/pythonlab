file_name = input("Enter file name: ")
text = input("Enter text to write: ")
with open(file_name, "w", encoding="utf-8") as file:
    file.write(text)
print("File written successfully.")
