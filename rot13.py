def rot13(message):
    encoded = ""

    for c in message:
        val = ord(c)
        if val >= ord("A") and val <= ord("Z"):
            new_val = val + 13
            if new_val > ord("Z"):
                new_val -= 26
            encoded += chr(new_val)
        elif val >= ord("a") and val <= ord("z"):
            new_val = val + 13
            if new_val > ord("z"):
                new_val -= 26
            encoded += chr(new_val)
        else:
            encoded += c
    return encoded


print(ord("A"), ord("Z"))
print(f"test->{rot13('test')}:{rot13('test')=='grfg'}")
print(f"Test->{rot13('Test')}:{rot13('Test')=='Grfg'}")
print(f"TEST->{rot13('TEST')}:{rot13('TEST')=='GRFG'}")
print(
    f"aA bB zZ 1234 *!?%->{rot13('aA bB zZ 1234 *!?%')}:{rot13('aA bB zZ 1234 *!?%')=='nN oO mM 1234 *!?%'}"
)
