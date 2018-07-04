import pickle
# message (input).
message = str(input("input coded message. ")).lower()
# ceasar cipher shift amount.
shift = 10
maxLen = int(input("Max length. "))
shiftPoss = 0
shiftlist = []
alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"," "]
progress = 1
# how far into message encryption the program is
ciMESS = 0
# message result (decoded)
mR = []
aR = []
fR = []
# replace code \/ \/ \/
for i in range(20):
    mR.extend(["","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","",])
# replace code /\ /\ /\
shiftlist = list(str(shift))
for i in range(0, len(str(shift))):
    shiftlist[i] = int(shiftlist[i])
while len(shiftlist) < maxLen:
    # regulates shift(var is shiftlist)
    shiftlist[-1] += 1
    for b in range(0, len(shiftlist)):
        if shiftlist[b] > 27 and b > 0:
            shiftlist[b - 1] += 1
            shiftlist[b] = 0
        elif shiftlist[b] > 27 and b == 0:
            shiftlist[b] = 0
            shiftlist.insert(0,0)
    # reset vars
    mR = [""]
    for i in range(20):
        mR.extend(["","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","",])
    ciMESS = 0
    # iterates through given message
    for i in range(len(message)):
        # searches alphabet for item ciMESS of message
        alphIndex = alphabet.index(message[ciMESS])
        # wraps shift around if to high or low
        if alphIndex + shiftlist[shiftPoss] > 27:
            alphIndex = alphIndex - 27
        if alphIndex + shift < 0:
            alphIndex = alphIndex + 27
        # implements shift calculated above
        mR[ciMESS] = alphabet[alphIndex + shiftlist[shiftPoss] - 1]
        ciMESS += 1
        shiftPoss += 1
        # resets shift possition if to high
        if shiftPoss > len(shiftlist)-1:
            shiftPoss = 0
    # writes result to all results list (var is aR)
    mR = "".join(mR)
    aR.append(str(shift)+"."+str(shiftlist)+". "+ mR)
    shift += 1
    if shift == 50000*progress:
        print(progress)
        print(shift)
        print("shiftlist len ",len(shiftlist))
        progress += 1
# searches results for possible matches
for a in range(0, 10**maxLen):
    if aR[a].find("the") > -1:
        fR.append(a)
    elif aR[a].find("in ") > -1:
        fR.append(a)
    elif aR[a].find("is ") > -1:
        fR.append(a)
    elif aR[a].find("and ") > -1:
        fR.append(a)
    elif aR[a].find("be ") > -1:
        fR.append(a)
    elif aR[a].find("as ") > -1:
        fR.append(a)
    elif aR[a].find("of ") > -1:
        fR.append(a)
    elif aR[a].find("at ") > -1:
        fR.append(a)
    elif aR[a].find("by ") > -1:
        fR.append(a)
    elif aR[a].find(" or ") > -1:
        fR.append(a)
    elif aR[a].find(" an ") > -1:
        fR.append(a)
    elif aR[a].find("hello ") > -1:
        fR.append(a)
    elif aR[a].find("there ") > -1:
        fR.append(a)
    elif aR[a].find("have ") > -1:
        fR.append(a)
    elif aR[a].find("that ") > -1:
        fR.append(a)

# prints possible indexes
print("possible indexes: ")
print(fR)
print(" ")
if str(input("print results? Y/N ")).lower() == "y":
    for i in range(0,len(fR)):
        print(aR[fR[i]])
# export results
if str(input("export possible results? Y/N ")).lower() == "y":
    outName = str(input("out name. "))
    sR = []
    for i in range(0,len(fR)):
        sR.append(aR[fR[i]])
        pickle.dump(sR, open(outName+".p","wb"))
if str(input("export results? Y/N ")).lower() == "y":
    outName = str(input("out name. "))
    open(outName+".txt","w").write("".join(aR)+"\n \n \n possible answers  "+str(fR))

    
