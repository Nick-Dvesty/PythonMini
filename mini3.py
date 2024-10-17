from operator import length_hint
from sys import flags

from tomlkit import float_


def matrix(str1: str) -> list:
    a = str.split(str1, '|')
    ansList = []
    length = -1
    for i in range(len(a)):
        ansList.append([])
        a[i] = str.strip(a[i])
        b = str.split(a[i], ' ')
        if length == -1:
            length = len(b)
        else:
            if len(b) != length:
                raise ValueError()
        for j in b:
            ansList[i].append(float_(j))
    return ansList


a = "12 3 32 42 | 23 3 43 32"
matrix(a)