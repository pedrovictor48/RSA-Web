from functions.number_theory import *

def toTable(texto: str) -> list:
    converter = lambda x: ord(x)
    vetor = list(map(converter, texto))
    return vetor

def toText(vetor: list) -> str:
    converter = lambda x: chr(x % 0x10FFFF)
    s = ''.join(map(converter, vetor))
    return s

def tenToBaseN(x: int, n: int) -> str:
    numberStr = str()
    while 1:
        numberStr += chr((x % n) + 1)
        x = x // n
        if x == 0:
            break

    return numberStr[::-1]

def toBaseTen(number: str, n: int):
    numberTen = 0
    for i, c in enumerate(number):
        numberTen += (ord(c) - 1) * (n ** i)
    return numberTen
