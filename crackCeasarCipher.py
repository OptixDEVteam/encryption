# message (input).
message = str(input("input coded message. ")).lower()
# ceasar cipher shift amount.
shift = 0
alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"," "]
# how far into message encryption the program is
ciMESS = 0
# message result (decoded)
mR = []
aR = []
fR = []
for i in range(20):
    mR.extend(["","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","",])
for s in range(26):
    mR = [""]
    for i in range(20):
        mR.extend(["","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","",])
    ciMESS = 0
    for i in range(len(message)):
        alphIndex = alphabet.index(message[ciMESS])
        if alphIndex + shift > 26:
            alphIndex = alphIndex - 27
        if alphIndex + shift < 0:
            alphIndex = alphIndex + 27
        mR[ciMESS] = alphabet[alphIndex + shift]
        ciMESS += 1
    mR = "".join(mR)
    print (shift,".", mR)
    aR.append(str(shift)+". "+ mR)
    shift += 1
for a in range(0, 25):
    if aR[a].find("the") > -1:
        fR.append(a)
    elif aR[a].find("in") > -1:
        fR.append(a)
    elif aR[a].find("is") > -1:
        fR.append(a)
    elif aR[a].find("and") > -1:
        fR.append(a)
    elif aR[a].find("be") > -1:
        fR.append(a)
    elif aR[a].find("as") > -1:
        fR.append(a)
    elif aR[a].find("of") > -1:
        fR.append(a)
print("possible indexes: ")
print(fR)
print(" ")
if str(input("print results? Y/N ")).lower() == "y":
    for i in range(0,len(fR)):
        print(aR[fR[i]])
if str(input("export results? Y/N ")).lower() == "y":
    outName = str(input("out name. "))
    open(outName+".txt","w").write("full results \n ".join(aR)+"\n \n \n possible answers".join(str(fR)))

    
