import string

def CaesarCipher(text, value):  # шифр Цезаря
    text = text.lower()
    encryptedstring = ""

    for char in text:
        if char.isalpha():
            encryptedstring += chr(ord("a") + (ord(char) - ord("a") + value) % (ord("z") - ord("a") + 1))
        else:
            encryptedstring += char

    return encryptedstring


def main():
    text = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
    print(text)
    print(CaesarCipher(text, 2))
    print(CaesarCipher("map", 2))

    text = """g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr
    ... amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q
     ... ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb.
    ... lmu ynnjw ml rfc spj."""
    table = str.maketrans(
        string.ascii_lowercase,
        string.ascii_lowercase[2:] + string.ascii_lowercase[:2])
    print(str.translate(text, table))
    print(str.translate("map", table))


if __name__ == "__main__":
    main()
