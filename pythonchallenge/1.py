#!/usr/bin/python


def solve_message(message):
    """Solve 2nd python challenge."""
    translated = ""
    for symbol in message:
        if symbol.isalpha:
            num = ord(symbol)
            num += 2
            if num > ord('z'):
                num -= 26
            elif num < ord('a'):
                num += 26
            translated += chr(num)
        else:
            translated += symbol
    return translated

#solution is www.pythonchallenge.com/pc/def/ocr.html

print solve_message("g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.")
