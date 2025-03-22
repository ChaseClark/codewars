# 0 1 2 3 4 5 6 7 8 9 A B C D E F
#


def base16_letter(num):
    if num <= 9:
        return str(num)
    elif num == 10:
        return "A"
    elif num == 11:
        return "B"
    elif num == 12:
        return "C"
    elif num == 13:
        return "D"
    elif num == 14:
        return "E"
    elif num == 15:
        return "F"
    else:
        exit(0)  # should be impossible


def rgb_to_hex(num):
    if num < 0:
        num = 0
    if num > 255:
        num = 255
    big = num // 16
    small = num % 16
    return f"{base16_letter(big)}{base16_letter(small)}"


def rgb(r, g, b):
    return f"{rgb_to_hex(r)}{rgb_to_hex(g)}{rgb_to_hex(b)}"


# 255, 255, 255 --> "FFFFFF"
# 255, 255, 300 --> "FFFFFF"
# 0, 0, 0       --> "000000"
# 148, 0, 211   --> "9400D3"

assert rgb(0, 0, 0) == "000000"
assert rgb(148, 0, 211) == "9400D3"
assert rgb(255, 255, 255) == "FFFFFF"
assert rgb(255, 255, 300) == "FFFFFF"
