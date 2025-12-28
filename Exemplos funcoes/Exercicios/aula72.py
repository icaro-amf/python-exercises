# Exercícios com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.

def multiplicar(*args):
    total = 1
    for numero in args:
        total *= numero
    return total

mult = multiplicar(5,3)
print(mult)

def pair(numero):
    fator = numero % 2 == 0

    if fator:
        return f"{numero} é par"
    else:
        return f"{numero} é impar"
    
print(pair(mult))