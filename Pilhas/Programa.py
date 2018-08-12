from Pilha import *
from Postfix import *
from Avaliar import *

infixa = input("Digite uma expressao infixa: ")

posfixa = postfix(infixa)

print("\nExpressao infixa: {0} \nExpressao posfixa: {1}".format(infixa, posfixa))

resultado = avaliarPosfixa(posfixa)

print("Resultado: {0}\n".format(resultado))
