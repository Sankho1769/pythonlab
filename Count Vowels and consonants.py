# 13. Count vowels and consonants
s = input("Enter a string: ").lower()
vowels = "aeiou"
v, c = 0, 0
for ch in s:
    if ch.isalpha():
        if ch in vowels:
            v += 1
        else:
            c += 1
print("Vowels:", v, "Consonants:", c)