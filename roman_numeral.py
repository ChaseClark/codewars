# +--------+-------+
# | Symbol | Value |
# +--------+-------+
# |    M   |  1000 |
# |   CM   |   900 |
# |    D   |   500 |
# |   CD   |   400 |
# |    C   |   100 |
# |   XC   |    90 |
# |    L   |    50 |
# |   XL   |    40 |
# |    X   |    10 |
# |   IX   |     9 |
# |    V   |     5 |
# |   IV   |     4 |
# |    I   |     1 |
# +--------+-------+

symbols = {}
symbols["M"] = 1000
symbols["CM"] = 900
symbols["D"] = 500
symbols["CD"] = 400
symbols["C"] = 100
symbols["XC"] = 90
symbols["L"] = 50
symbols["XL"] = 40
symbols["X"] = 10
symbols["IX"] = 9
symbols["V"] = 5
symbols["IV"] = 4
symbols["I"] = 1


class RomanNumerals:
    @staticmethod
    def to_roman(val: int) -> str:
        result = []
        for symbol, digit in symbols.items():
            while val >= digit:
                result.append(symbol)
                val -= digit
        return "".join(result)

    @staticmethod
    def get_front_char_count(source: str, target: str) -> int:
        cnt = 0
        for char in source:
            if char is not target:
                break
            cnt += 1
        return cnt

    @staticmethod
    def from_roman(roman_num: str) -> int:
        total = 0
        if roman_num.startswith("M"):
            cnt = RomanNumerals.get_front_char_count(roman_num, "M")
            total += cnt * symbols["M"]
            roman_num = roman_num[cnt:]
        if roman_num.startswith("CM"):
            total += symbols["CM"]
            roman_num = roman_num.replace("CM", "")
        if roman_num.startswith("D"):
            cnt = RomanNumerals.get_front_char_count(roman_num, "D")
            total += cnt * symbols["D"]
            roman_num = roman_num[cnt:]
        if roman_num.startswith("CD"):
            total += symbols["CD"]
            roman_num = roman_num.replace("CD", "")
        if roman_num.startswith("C"):
            cnt = RomanNumerals.get_front_char_count(roman_num, "C")
            total += cnt * symbols["C"]
            roman_num = roman_num[cnt:]
        if roman_num.startswith("XC"):
            total += symbols["XC"]
            roman_num = roman_num.replace("XC", "")
        if roman_num.startswith("L"):
            cnt = RomanNumerals.get_front_char_count(roman_num, "L")
            total += cnt * symbols["L"]
            roman_num = roman_num[cnt:]
        if roman_num.startswith("XL"):
            total += symbols["XL"]
            roman_num = roman_num.replace("XL", "")
        if roman_num.startswith("X"):
            cnt = RomanNumerals.get_front_char_count(roman_num, "X")
            total += cnt * symbols["X"]
            roman_num = roman_num[cnt:]
        if roman_num.startswith("IX"):
            total += symbols["IX"]
            roman_num = roman_num.replace("IX", "")
        if roman_num.startswith("V"):
            cnt = RomanNumerals.get_front_char_count(roman_num, "V")
            total += cnt * symbols["V"]
            roman_num = roman_num[cnt:]
        if roman_num.startswith("IV"):
            total += symbols["IV"]
            roman_num = roman_num.replace("IV", "")
        if roman_num.startswith("I"):
            cnt = RomanNumerals.get_front_char_count(roman_num, "I")
            total += cnt * symbols["I"]
            roman_num = roman_num[cnt:]
        return total


assert RomanNumerals.to_roman(2000) == "MM"
assert RomanNumerals.to_roman(1666) == "MDCLXVI"
assert RomanNumerals.to_roman(86) == "LXXXVI"
assert RomanNumerals.to_roman(1) == "I"
assert RomanNumerals.to_roman(1990) == "MCMXC"

assert RomanNumerals.from_roman("MM") == 2000
assert RomanNumerals.from_roman("MDCLXVI") == 1666
assert RomanNumerals.from_roman("LXXXVI") == 86
assert RomanNumerals.from_roman("I") == 1
assert RomanNumerals.from_roman("XXIX") == 29
