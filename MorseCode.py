# ----------------------Morse Code----------------------

def encryptMorseCode(text):
    text = text.lower().strip()
    morseCode = {
        'a': '._',
        'b': '_...',
        'c': '_._.',
        'd': '_..',
        'e': '.',
        'f': '.._.',
        'g': '__.',
        'h': '....',
        'i': '..',
        'j': '.___',
        'k': '_._',
        'l': '._..',
        'm': '__',
        'n': '_.',
        'o': '___',
        'p': '.__.',
        'q': '__._',
        'r': '._.',
        's': '...',
        't': '_',
        'u': '.._',
        'v': '..._',
        'w': '.__',
        'x': '_.._',
        'y': '_.__',
        'z': '__..'
    }
    result = ""
    arrofchars = text.split(" ")
    for c in range(len(arrofchars)):
        for i in arrofchars[c]:
            result = result + morseCode[i] + " "
    return result.strip()


def decryptMorseCode(text):
    text = text.lower().strip()
    morseCode = {
        'a': '._',
        'b': '_...',
        'c': '_._.',
        'd': '_..',
        'e': '.',
        'f': '.._.',
        'g': '__.',
        'h': '....',
        'i': '..',
        'j': '.___',
        'k': '_._',
        'l': '._..',
        'm': '__',
        'n': '_.',
        'o': '___',
        'p': '.__.',
        'q': '__._',
        'r': '._.',
        's': '...',
        't': '_',
        'u': '.._',
        'v': '..._',
        'w': '.__',
        'x': '_.._',
        'y': '_.__',
        'z': '__..'
    }
    morseCode = dict((v, k) for k, v in morseCode.items())
    result = ""
    arroftext = text.strip().split(" ")

    for c in arroftext:
        result += morseCode[c] + ""
    return result
