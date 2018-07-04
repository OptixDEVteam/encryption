import pickle
if str(input("open file? Y/N ")).lower() == "y":
    inName = str(input("filename? "))
    message = pickle.load(open(inName+".txt", "rb"))[0]
    if str(input("use recorded shift? Y/N ")).lower() == "y":
        shift = pickle.load(open(inName+".txt", "rb"))[1]
        
else:
# message (input).
    message = str(input("message plz. no caps, no punctuation, no numbers. ")).lower()
# ceasar cipher shift amount.
    shift = int(input("letter shift plz no decimials. "))
if shift > 26:
    print("number to high try again!")
    shift = int(input("letter shift plz no decimials. "))
alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"," "]
ciMESS = 0
# how far into message encryption the program is
mR = ["","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","",]
# message result (encoded)
for i in range(len(message)):
    print("i =",i)
    alphIndex = alphabet.index(message[ciMESS])
    print(alphIndex)
    if alphIndex + shift > 26:
        alphIndex = alphIndex - 27
        print("new alphindex",alphIndex)
    if alphIndex + shift < 0:
        alphIndex = alphIndex + 27
        print("new alphindex",alphIndex)
    mR[ciMESS] = alphabet[alphIndex + shift]
    ciMESS += 1
mR = "".join(mR)
print (mR)
if str(input("export results? Y/N ")).lower() == "y":
    if str(input("export key? Y/N ")).lower() == "y":
        outName = str(input("out name. "))
        pickle.dump([mR, -shift], open(outName+".txt","wb"))
    else:
        outName = str(input("out name. "))
        pickle.dump([mR, 0], open(outName+".txt","w"))

    
