# ----------------------Index Sub Cipher----------------------

def encryptIndexSubstitutionCipher(text):
    text = text.lower().strip()
    alpnums = {
        'a': '01',
        'b': '02',
        'c': '03',
        'd': '04',
        'e': '05',
        'f': '06',
        'g': '07',
        'h': '08',
        'i': '09',
        'j': '10',
        'k': '11',
        'l': '12',
        'm': '13',
        'n': '14',
        'o': '15',
        'p': '16',
        'q': '17',
        'r': '18',
        's': '19',
        't': '20',
        'u': '21',
        'v': '22',
        'w': '23',
        'x': '24',
        'y': '25',
        'z': '26'
    }

    def checkfor(ourtext):
        arr = []
        for i in range(len(ourtext)):
            if ourtext[i].isalpha():
                arr.append(alpnums[ourtext[i]])

        return "".join(arr)

    result = " ".join(map(checkfor, text))
    return result


def decryptIndexSubstitutionCipher(text):
    text = text.strip().split(" ")
    alpnums = dict((k, v) for v, k in {
        'a': '01',
        'b': '02',
        'c': '03',
        'd': '04',
        'e': '05',
        'f': '06',
        'g': '07',
        'h': '08',
        'i': '09',
        'j': '10',
        'k': '11',
        'l': '12',
        'm': '13',
        'n': '14',
        'o': '15',
        'p': '16',
        'q': '17',
        'r': '18',
        's': '19',
        't': '20',
        'u': '21',
        'v': '22',
        'w': '23',
        'x': '24',
        'y': '25',
        'z': '26'
    }.items())

    result = "".join(str(i) for i in list(map(lambda c: alpnums[c], text)))
    return result