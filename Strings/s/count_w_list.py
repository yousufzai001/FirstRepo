s = "aabbcde"
char = {}
for i in s:
    char[i] = char.get(i,0) + 1

for i in s:
    if char[i] == 1:
        print(i)
        break
        


