message = str(input("message plz. no caps, no punctuation, no numbers. "))
# message input.
strShiftKey = str(input("letter shift word plz. no numbers. "))
# ceasar cipher shift amount.
alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"," "]
lShiftWord = []
# Number equivelents for strShiftKey
iShiftWordNum = 0
iAlphNum = 0
# helps find letter from alphabet
iAlphShiftNum = 0
# alphabet assist for encryption adds shift in
iMessageData = 0
# how far into message encryption the program is
strResult = " "
strResult1 = " "
# message result (encoded)
while iMessageData < len(strShiftKey):
    if alphabet[iAlphNum] in strShiftKey[iMessageData]:
        print (" ")
        while iAlphNum > 26:
            iAlphNum = iAlphNum - 27
            # checks if the alph num is over string length
        lShiftWord.append (iAlphNum)
        # adds number to shift word list
        iMessageData = iMessageData + 1
        iAlphNum = 0
    else:
        iAlphNum = iAlphNum + 1
        # if the letter tried does not come out true a differnt letter is tried
print(lShiftWord)
iMessageData = 0
while iMessageData < len(message):
    if alphabet[iAlphNum] in message[iMessageData]:
        print (" ")
        iAlphShiftNum = iAlphNum + lShiftWord[iShiftWordNum]
        while iAlphShiftNum > 26:
            iAlphShiftNum = iAlphShiftNum - 27
        strResult1 = alphabet[iAlphShiftNum]
        strResult = strResult + strResult1
        # renders answer
        iMessageData = iMessageData + 1
        # changes what letter program is evaluated 
        iAlphNum = 0
        if iShiftWordNum == (len(lShiftWord) - 1):
            iShiftWordNum = 0
            # siplifies expression if over allowed amount
        else:
            iShiftWordNum = iShiftWordNum + 1
        # if the letter tried does not come out true a differnt letter is tried


#       if messrec == len(shiftword)-1:
#            messloop = 0
    else:
        iAlphNum = iAlphNum + 1
print (strResult)
