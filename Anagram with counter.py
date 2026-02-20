from collections import Counter

word1 = input("Enter first word: ")
word2 = input("Enter second word: ")

if Counter(word1) == Counter(word2):
    print("Anagram")
else:
    print("Not anagram")

