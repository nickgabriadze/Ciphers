
# ----------------------Affine Cipher----------------------

def encryptAffineCipher(text, a, b):
    text = text.lower().strip()
    alpnums = {
        'a': 0,
        'b': 1,
        'c': 2,
        'd': 3,
        'e': 4,
        'f': 5,
        'g': 6,
        'h': 7,
        'i': 8,
        'j': 9,
        'k': 10,
        'l': 11,
        'm': 12,
        'n': 13,
        'o': 14,
        'p': 15,
        'q': 16,
        'r': 17,
        's': 18,
        't': 19,
        'u': 20,
        'v': 21,
        'w': 22,
        'x': 23,
        'y': 24,
        'z': 25
    }
    reversealpnums = dict((v, k) for k, v in alpnums.items())

    result = "".join(str(i) for i in list(map(lambda c: reversealpnums[(((a * alpnums[c]) + b) % 26)], text)))

    return result.strip()


def decryptAffineCipher(text, a, b):
    text = text.lower().strip()
    alpnums = {
        'a': 0,
        'b': 1,
        'c': 2,
        'd': 3,
        'e': 4,
        'f': 5,
        'g': 6,
        'h': 7,
        'i': 8,
        'j': 9,
        'k': 10,
        'l': 11,
        'm': 12,
        'n': 13,
        'o': 14,
        'p': 15,
        'q': 16,
        'r': 17,
        's': 18,
        't': 19,
        'u': 20,
        'v': 21,
        'w': 22,
        'x': 23,
        'y': 24,
        'z': 25
    }
    reversealpnums = dict((v, k) for k, v in alpnums.items())

    result = "".join(
        str(i) for i in list(map(lambda c: reversealpnums[((pow(a, -1, 26) * (alpnums[c] - b)) % 26)], text)))

    return result.strip()
