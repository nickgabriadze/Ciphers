
# ----------------------Caesar Cipher----------------------

def encryptCaesarCipher(text, key1, key2):
    textArr = list(text)
    i = 0
    textArrI = 0

    while i < len(textArr):
        forKey1 = ord(textArr[textArrI]) + (key1 % 26)
        forKey2 = ord(textArr[textArrI]) + (key2 % 26)

        if i % 2 == 0:

            if textArr[textArrI].isdigit():
                forKey1 = ord(textArr[textArrI]) + (key1 % 10)
                if forKey1 > ord("9"):
                    forKey1 = (forKey1 - ord("9")) + (ord("0") - 1)
                    textArr[textArrI] = chr(forKey1)

                else:
                    textArr[textArrI] = chr(forKey1)
            else:
                if textArr[textArrI].isalpha():
                    if textArr[textArrI].isupper():
                        if forKey1 > ord("Z"):
                            forKey1 = (forKey1 - ord("z")) + (ord("a") - 1)
                            textArr[textArrI] = chr(forKey1).upper()
                        else:
                            textArr[textArrI] = chr(forKey1).upper()
                    else:
                        if forKey1 > ord("z"):
                            forKey1 = (forKey1 - ord("z")) + (ord("a") - 1)
                            textArr[textArrI] = chr(forKey1)

                        else:
                            textArr[textArrI] = chr(forKey1)

        else:
            if textArr[textArrI].isdigit():
                forKey2 = ord(textArr[textArrI]) + (key2 % 10)
                if forKey2 > ord("9"):
                    forKey2 = (forKey2 - ord("9")) + (ord("0") - 1)
                    textArr[textArrI] = chr(forKey2)
                else:
                    textArr[textArrI] = chr(forKey2)
            else:
                if textArr[textArrI].isalpha():
                    if textArr[textArrI].isupper():
                        if forKey2 > ord("z"):

                            forKey2 = (forKey2 - ord("z")) + (ord("a") - 1)
                            textArr[textArrI] = chr(forKey2).upper()

                        else:
                            textArr[textArrI] = chr(forKey2).upper()
                    else:
                        if forKey2 > ord("z"):
                            forKey2 = (forKey2 - ord("z")) + (ord("a") - 1)

                            textArr[textArrI] = chr(forKey2)

                        else:
                            textArr[textArrI] = chr(forKey2)

        i = i + 1
        textArrI = textArrI + 1

    return "".join(textArr)


def decryptCaesarCipher(text, key1, key2):
    textArr = list(text)
    i = 0
    textArrI = 0

    while i < len(textArr):
        forKey1 = ord(textArr[textArrI]) - (key1 % 26)
        forKey2 = ord(textArr[textArrI]) - (key2 % 26)

        if i % 2 == 0:
            if textArr[textArrI].isdigit():
                forKey1 = ord(textArr[textArrI]) - (key1 % 10)
                if forKey1 < ord("0"):
                    forKey1 = ord("9") + 1 - (ord("0") - forKey1)
                    textArr[textArrI] = chr(forKey1)
                else:
                    textArr[textArrI] = chr(forKey1)
            else:
                if textArr[textArrI].isalpha():
                    if textArr[textArrI].isupper():
                        if forKey1 < ord("A"):
                            forKey1 = ord("Z") + 1 - (ord("A") - forKey1)
                            textArr[textArrI] = chr(forKey1).upper()
                        else:
                            textArr[textArrI] = chr(forKey1).upper()
                    else:
                        if forKey1 < ord("a"):
                            forKey1 = ord("z") + 1 - (ord("a") - forKey1)
                            textArr[textArrI] = chr(forKey1)
                        else:
                            textArr[textArrI] = chr(forKey1)
        else:
            if textArr[textArrI].isdigit():
                forKey2 = ord(textArr[textArrI]) - (key2 % 10)
                if forKey2 < ord("0"):
                    forKey2 = ord("9") + 1 - (ord("0") - forKey2)
                    textArr[textArrI] = chr(forKey2)
                else:
                    textArr[textArrI] = chr(forKey2)
            else:
                if textArr[textArrI].isalpha():
                    if textArr[textArrI].isupper():
                        if forKey2 < ord("A"):
                            forKey2 = ord("Z") + 1 - (ord("A") - forKey2)
                            textArr[textArrI] = chr(forKey2).upper()
                        else:
                            textArr[textArrI] = chr(forKey2).upper()
                    else:
                        if forKey2 < ord("a"):
                            forKey2 = ord("z") + 1 - (ord("a") - forKey2)
                            textArr[textArrI] = chr(forKey2)
                        else:
                            textArr[textArrI] = chr(forKey2)
        i = i + 1
        textArrI = textArrI + 1

    return "".join(textArr)
