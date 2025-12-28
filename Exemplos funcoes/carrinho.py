# Exercicio 2 - Criar um carrinho de compra

item = str(input("O que voce deseja comprar? "))
preco = float(input("Qual o valor do item? "))
quantidade = int(input("Quantas unidades deseja? "))
total = preco * quantidade

print(f"Voce pediu {quantidade} unidades de {item}.")
print(f"O valor da compra sera de R${total}")