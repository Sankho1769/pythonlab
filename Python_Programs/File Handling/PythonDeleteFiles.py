import os

file_name = input("Enter file name to delete: ")
if os.path.exists(file_name):
    os.remove(file_name)
    print("File deleted.")
else:
    print("File does not exist.")
