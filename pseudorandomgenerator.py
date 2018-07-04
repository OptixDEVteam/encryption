key = str(input("key: "))
repeats = int(input("repeats: "))
keyEdit = int(key[0]+key[1]+key[2])
randomStr = []
finalStr = 0
for i in range(repeats):
    randomStr.append(str(keyEdit*keyEdit))
    keyEdit = int(str(keyEdit*keyEdit)[1]+str(keyEdit*keyEdit)[2]+str(keyEdit*keyEdit)[3])
print(int("".join(randomStr)))