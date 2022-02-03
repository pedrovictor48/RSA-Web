from functions.number_theory import *
from functions.uteis import *

base = 5000

def encriptar(msg: str, n: int, e: int):
    global base
    tabela = toTable(msg)
    M = lambda m: pow(m, e, n)
    tabelaEncriptada = list(map(M, tabela))
    textoEncriptado = chr(base + 1).join(map(lambda x: tenToBaseN(x, base), tabelaEncriptada))
    with open("mensagem_encriptada.txt", "wb") as file:
        file.write(textoEncriptado.encode('utf-8'))
    return textoEncriptado

def desencriptar(msg:str, p: int, q: int, e: int):
    global base
    #calculando d:
    tot = totienteEuler(p, q)
    d = inversoModulo(e, tot)
    n = p * q
    m = lambda M: pow(M, d, n)
    textoEncriptado = msg
    tabelaEncriptada = list(map(lambda x: toBaseTen(x, base), textoEncriptado.split(chr(base + 1))))
    tabelaDesencriptada = list(map(m, tabelaEncriptada))
    textoDesencriptado = toText(tabelaDesencriptada)
    with open("mensagem_desencriptada.txt", "wb") as file:
        file.write(textoDesencriptado.encode('utf-8'))
    
    return textoDesencriptado