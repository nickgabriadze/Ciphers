
# ----------------------Transposition Cipher----------------------

def encryptTranspositionCipher(text, key):
    ourArr = list(text)
    ourArr = [ourArr[index:index + key] for index in range(0, len(ourArr), key)]
    string = ""
    scrambledArr = []
    elementExistence = 0
    arrElemC = 0

    while arrElemC < len(ourArr[0]):
        for i in range(0, len(ourArr)):
            if elementExistence < len(ourArr[i]):
                string += ourArr[i][elementExistence]

        scrambledArr.append(string)
        string = ""
        arrElemC += 1
        elementExistence += 1

    return "".join(scrambledArr)


def decryptTranspositionCipher(text, key):
    ourArr = list(text)
    q, r = divmod(len(ourArr), key)
    slicedArr = list((ourArr[index * q + min(index, r):(index + 1) * q + min(index + 1, r)] for index in range(key)))

    string = ""
    elementExistence = 0
    arrElemC = 0
    decryptedArr = []
    while arrElemC < len(slicedArr[0]):
        for i in range(0, len(slicedArr)):
            if elementExistence < len(slicedArr[i]):
                string += slicedArr[i][elementExistence]

        decryptedArr.append(string)
        string = ""
        arrElemC += 1
        elementExistence += 1

    return "".join(decryptedArr)
