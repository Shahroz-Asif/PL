LOWERCASE_A = 97
def hexASCII():
    alphabet_hex = {}

    for ascii in range(LOWERCASE_A, LOWERCASE_A + 26):
        alphabet = chr(ascii)
        hex_code = "%x" % ascii

        alphabet_hex[alphabet] = hex_code

    print("Alphabet-Hex dictionary: ", alphabet_hex)

hexASCII()