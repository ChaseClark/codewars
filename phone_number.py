def create_phone_number(numbers):
    return f'({"".join(map(str,numbers[0:3]))}) {"".join(map(str,numbers[3:6]))}-{"".join(map(str,numbers[6:10]))}'


print(create_phone_number([3, 0, 1, 5, 5, 5, 1, 2, 3, 4]))
