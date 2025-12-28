import math
#Consiga o valor de C de um triangulo retangulo sendo que o usuario possui os o valores de A e B.

a = float(input("Insira o valor de A: "))
b = float(input("Insira o valor de B: "))

c = math.sqrt(pow(a,2)+ pow(b,2))

print(f"O valor de C é: {round(c,2)}")