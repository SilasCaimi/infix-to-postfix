# infix-to-postfix

Programa em Python que recebe uma expressão infixa, converte para posfixa e depois avalia a expressão gerando o resultado da função com aplicação de TDA (tipos de dados abstratos).

## Arquivos

Node.py - Implementa o tipo de dados abstrato Node

Pilha.py - Implementa o tipo de dados abstrato Pilha

Postfix.py - Programa que converte a função infixa em posfixa

Avaliar.py - Avalia a expressão posfixa gerando seu resultado

Programa.py - Testa o programa

## Algoritmo

### Passo 1:
* Inicie com uma pilha vazia;
* Realize uma varredura na expressão infixa, copiando todos os operandos encontrados diretamente para a expressão de saída.

### Passo 2:
* Ao encontrar um operador:
* Enquanto a pilha não estiver vazia e houver no seu topo um operador com prioridade maior ou igual ao encontrado, desempilhe o operador e copie-o na saída.
* Empilhe o operador encontrado.

### Passo 3:
* Ao encontrar um parêntese de abertura, empilhe-o.

### Passo 4:
* Ao encontrar um parêntese de fechamento, remova um símbolo da pilha e copie-o na saída. * Repita esse passo até que seja desempilhado o parêntese de abertura correspondente.

### Passo 5:
* Ao final da varredura, esvazie a pilha, movendo os símbolos desempilhados para a saída.
* Pronto, conseguimos obter como saída a notação pósfixa para qualquer notação infixa entrada.
