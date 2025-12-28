#Primeiro programa com py

#Para introduzir string, temos que colocar todo o texto entre aspas simples, ou duplas. ('string' ou "string").
name = 'Icaro'
food = "pizza"
#print(food, name)

#Para introduzir string ao decorrer de um comando print, temos que adicionar a letra F ou f, que representa a f-string. Fazendo nosso comando reconhecer a diferenca por meio de colchetes {}.

#print(f"hello, {name}!")

#Para introduzir os integers, ou inteiros, temos apenas que definir o valor a ser usado.
age = 22
price = 5
num_of_food = 8

#print(f"Hello, {name}! Do you like {food}? If you like, and want, the price is {price} dolars, for {num_of_food} slice")

#Quanto aos float, são os numeros acompanhados dos decimais. Nada muda em relacao aos inteiros na questao de representar.
height = 1.80

#print(f"My heigth is {height} meters")

#O boolean funciona apenas com 2 comandos, falso ou verdadeiro, muito util para ferramentas de repeticoes.
boy = True

# if boy:
#     print(f"He is a boy")
# else:
#     print(f"She is a girl")

#Agora, iremos aprender a converter as variaveis em cada um dos tipos apresentados.
# print(type(age))
# print(type(height))
# print(type(boy))

age = float(age)
height = int(height)
boy = str(boy)
name = bool(name)           #Parte muito interessante, caso nao tenha nenhum caractere utilizado na string name, a ferramente retorna falso. Podemos usar isso para identificar posteriormente variaveis nao preenchidas pelo usuario para retornar msg de erro.
# print(type(age))
# print(type(height))
# print(type(boy))

# print(age)
# print(height)
# print(boy)
