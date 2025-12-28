# Crie uma função chamada media() que receba 3 notas e retorne a média.
# Crie uma função eh_primo(n) que diga se um número é primo ou não.
# Crie uma função que receba uma string e retorne quantas vogais ela tem.

def media(x,y,z):
    return print(((x+y+z)/3))

def primo(x):
    if x <= 1:
        return print("Não é primo!")
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            return print("Não é primo!")
    return print("É um número primo!")

def leitor(text):
    text = text.lower()
    vogais = [letra for letra in text if letra in "aeiouáéíóúâêôãõ"]
    return print(len(vogais))

# med1 = float(input("Digite um número para ser calculada a média: "))
# med2 = float(input("Digite um número para ser calculada a média: "))
# med3 = float(input("Digite um número para ser calculada a média: "))
# media(med1, med2, med3)

# num = int(input("Digite um número para saber se ele é primo ou não: "))
# primo(num)

#leitor("Ícaro")