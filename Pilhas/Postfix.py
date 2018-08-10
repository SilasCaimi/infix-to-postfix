from Pilha import *

def isOperador(s):
    if s == "+" or s == "-" or s == "*" or s == "/" or s == "$":
        return True
    else:
        return False

def prioridade(c, t):
    """Verifica a prioridade entre os operandos"""
    if c == '$':
        pc = 4
    elif c == '*' or c == '/':
        pc = 2
    elif c == '+' or c == '-':
        pc = 1
    else:
        pc = 4
 
    if t == '$':
        pt = 3
    elif t == '*' or t == '/':
        pt = 2
    elif t == '+' or t == '-':
        pt = 1
    else:
        pt = 0

    return pc <= pt

def postfix(infix):
    """Converte uma expressao infixa em posfixa"""

    p = Pilha()
    posfixa = []

    for i in range(len(infix)):
        c = infix[i]
        if c >= '0' and c <= '9' or c.lower() >= 'a' and c.lower() <= 'z':
            posfixa.append(c)
        elif isOperador(c):
            while not p.isEmpty() and prioridade(c, p.stacktop()):
                t = p.pop()
                posfixa.append(t)
            p.push(c)
        elif c == '(':
            p.push(c)
        elif c == ')':
            while True:
                t = p.pop()
                if t != '(':
                    posfixa.append(t)
                else:
                    break
    while not p.isEmpty():
        posfixa.append(p.pop())

    posfixa = "".join(posfixa)

    return posfixa



#Passo 1:
#Inicie com uma pilha vazia;
#Realize uma varredura na expressão infixa, copiando todos os operandos encontrados diretamente para a expressão de saída.

#Passo 2:
#Ao encontrar um operador:
#Enquanto a pilha não estiver vazia e houver no seu topo um operador com prioridade maior ou igual ao encontrado, desempilhe o operador e copie-o na saída
#Empilhe o operador encontrado

#Passo 3:
#Ao encontrar um parêntese de abertura, empilhe-o

#Passo 4:
#Ao encontrar um parêntese de fechamento, remova um símbolo da pilha e copie-o na saída. Repita esse passo até que seja desempilhado o parêntese de abertura correspondente

#Passo 5:
#Ao final da varredura, esvazie a pilha, movendo os símbolos desempilhados para a saída. Pronto, conseguimos obter como saída a notação pósfixa para qualquer notação infixa entrada.
#Estrutura de Dados