def is_even(number):
    if (number % 2) == 0:
        result = "True"
    else:
        result = "False"
    return result


print(is_even(4))
print(is_even(7))
print(is_even(0))
print(is_even(-3))
print(is_even(10))