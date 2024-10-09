import sys


def counter(number: int) -> int:
    counter = number < 0
    length = int.bit_length(number)
    for i in range(length):
        if number - (number >> 1 << 1) == 1: counter += 1
        number >>= 1
    return counter

number = int(input("Enter a number: "))
t = counter(number)
print(t)
