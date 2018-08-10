from Pilha import *
from Postfix import *
from Avaliar import *

#infixa = "3+4*(2$2$3+2)"

#infixa = "((A+B)*C-(D-E))$(F+G)"

infixa = input("Digite uma expressao infixa: ")

posfixa = postfix(infixa)

print("\nExpressao infixa: {0} \nExpressao posfixa: {1}".format(infixa, posfixa))

resultado = avaliarPosfixa(posfixa)

print("Resultado: {0}\n".format(resultado))
