from functions.number_theory import *
from functions.uteis import *

base = 5000

def encriptar(msg: str, n: int, e: int, simple=False):
    global base
    tabela = toTable(msg)
    M = lambda m: pow(m, e, n)
    tabelaEncriptada = list(map(M, tabela))
    if simple:
        textoEncriptado = " ".join(map(str, tabelaEncriptada))
    else:
        textoEncriptado = chr(base + 1).join(map(lambda x: tenToBaseN(x, base), tabelaEncriptada))
    with open("mensagem_encriptada.txt", "wb") as file:
        file.write(textoEncriptado.encode('utf-8'))
    return textoEncriptado

def desencriptar(msg:str, p: int, q: int, e: int, simple=False):
    global base
    #calculando d:
    tot = totienteEuler(p, q)
    d = inversoModulo(e, tot)
    n = p * q
    m = lambda M: pow(M, d, n)
    textoEncriptado = msg
    if simple:
        tabelaEncriptada = list(map(lambda x: toBaseTen(x, base), textoEncriptado.split(chr(base + 1))))
    else:
        tabelaEncriptada = list(map(int, textoEncriptado.split(' ')))
    tabelaDesencriptada = list(map(m, tabelaEncriptada))
    textoDesencriptado = toText(tabelaDesencriptada)
    with open("mensagem_desencriptada.txt", "wb") as file:
        file.write(textoDesencriptado.encode('utf-8'))
    
    return textoDesencriptado