from Pilha import *

def operacao(op, opnd1, opnd2):
    if op == "+":
        return opnd1 + opnd2
    elif op == "-":
        return opnd1 - opnd2
    elif op == "*":
        return opnd1 * opnd2
    elif op == "/":
        return opnd1 / opnd2
    elif op == "$":
        return opnd1 ** opnd2
    else:
        return False                # Retorna False caso o operando não seja válido

def avaliarPosfixa(expressao):
    """ Avalia uma expressao posfixa"""
    p = Pilha()
    for i in range(len(expressao)):
        c = expressao[i]
        if c >= "0" and c <= "9":
            p.push(c)
        else:
            opnd2 = p.pop()
            opnd1 = p.pop()

            valor = operacao(c, int(opnd1), int(opnd2))

            if valor:                                       # Verifica se o operando é válido   
                p.push(valor)
            else:
                return "Operador invalido"
    
    resultado = p.pop()

    if p.isEmpty():                 # Verifica se ao final a pilha está vazia
        return resultado
    else:
        return "Expressao invalida"

