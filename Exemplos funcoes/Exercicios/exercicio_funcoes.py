# Exercícios
# Crie funções que duplicam, triplicam e quadruplicam
# o número recebido como parâmetro.
 
def dup(num): #definindo a funcao "dup" para duplicar o parametro "num" por 2.
    return num * 2

def trip(num):
    return num * 3

def quad(num):
    return num * 4

def multiplicador(termo): #definindo a funcao para implementar o multiplicador (2,3,4,..., x) para podermos fazer a multiplicao desejada.
    def multiplicar(numero): #adquirimos o multiplicador e aqui pegamos o numero que o usuario deseja multiplicar pelo multiplicador.
        return numero * termo
    return multiplicar

duplicar = multiplicador(2)
triplicar = multiplicador(3)
quadriplicar = multiplicador(4)

print(quadriplicar(4))