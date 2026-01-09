s = "education"
vow = "aeiou"
vowels = 0
consonants = 0
for i in s:
    if i in vow:
        vowels += 1
    else:
        consonants += 1

print(vowels)
print(consonants)