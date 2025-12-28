#While é uma ferramenta de repeticao que continua no loop imposto até que a afirmacao se torne falsa.

"""
contador = 0

while contador <= 100: 
    contador += 1

    if contador == 10 or contador == 20:
        print("Numero oculto")
        continue

    print(f"Ainda nao chegamos no valor desejado, valor atual: {contador}")

    if contador == 50:
        print("O valor 50 está programado para finalizar o programa!")
        break    

print("Saimos do loop")
"""
"""
qtd_linhas = 5
qtd_colunas = 5

linha = 1
while linha <= qtd_linhas:
    coluna = 1

    while coluna <= qtd_colunas:
        print(f"{linha = } {coluna = }")
        coluna += 1

    linha += 1


print("Saindo do laco")
"""
#Exercicio de while
#Iterando strings com while

"""
nome = "Icaro Fonseca" #Iteráveis

indice = 0
novo_nome = ""

while indice < len(nome):
    letra = (nome[indice])
    novo_nome += f"*{letra}"
    indice += 1

novo_nome += "*"

print(novo_nome)
"""

#Exercicio calculadora com while

"""
while True:
    numero1 = input("Digite o primeiro número: ")
    numero2 = input("Digite o segundo número: ")
    operador = input("Digite o sinal da operacao desejada [+ = / *]: ")

    numeros_validos = None
    try:
        num1_float = float(numero1)
        num2_float = float(numero2)
        numeros_validos = True
    except:
        numeros_validos = None

    if numeros_validos is None:
        print("Um ou ambos os numeros digitados, sao invalidos!")
        continue
    
    operadores_validos = '+-/*'

    if operador not in operadores_validos:
        print("Operador inválido!")
        continue

    if len(operador) > 1:
        print("Digite apenas 1 operador!")
        continue

    if operador == "+":
        print(f"O resultado da soma é: {num1_float + num2_float} ")

    elif operador == "-":
        print(f"O resultado da subtracão é: {num1_float - num2_float} ")
    
    elif operador == "*":
        print(f"O resultado da multiplicacão é: {num1_float * num2_float} ")
    
    else:
        print(f"O resultado da divisão é: {num1_float / num2_float} ")


    sair = input("Deseja sair da calculadora? [S/N]: ").lower().startswith("s")

    if sair is True:
        break
    """
#Podemos usar o else juntamente ao while, quando quisermos adicionar alguma informacao ao fazer a leitura completa do laco while.
"""
string = 'Valor qualquer'

i = 0
while i < len(string):
    letra = string[i]

    if letra == ' ':
        break

    print(letra)
    i += 1
else:
    print('Não encontrei um espaço na string.')
print('Fora do while.')
"""

frase = "O rato roeu a roupa do rei de roma"

i = 0
qtd_letras = 0
letra_maisrep = "" 

while i < len(frase):
    letra = frase[i]

    if letra == " ":
        i += 1

        continue

    rep = frase.count(letra)
    
    if qtd_letras < rep:
        qtd_letras = rep
        letra_maisrep = letra

    i += 1

print(f"A letra que se repetiu mais vezes foi {letra_maisrep}, que apareceu {qtd_letras}.")