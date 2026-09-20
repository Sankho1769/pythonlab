import re

text = input("Enter text to search: ")
pattern = input("Enter a word or pattern to find: ")
match = re.search(pattern, text)
print("Found:", bool(match))
