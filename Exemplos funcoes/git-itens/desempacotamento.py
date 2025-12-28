"""
Introducao ao desempacotamento + tuple (tuplas) Prof Luiz Otavio
"""
#Desempacotamento ----->

"""
nomes = ["Icaro", "Alves", "Mota", "Fonseca"]
#nome1, nome2, nome3, nome4 = nomes
#print(nome1, nome2, nome3, nome4) # retorna "Icaro Alves Mota Fonseca" pois puxa cada string da lista em ordem.

#nome1, nome2, nome3 = ["Icaro", "Alves", "Mota", "Fonseca"]
#print(nome1, nome2, nome3) # retorna erro, pois não há variaveis o suficiente para portar cada item na lista, erro similar caso existam mais variaveis do que objetos na lista.

nome1, *_ = ["Icaro", "Alves", "Mota", "Fonseca"]
print(nome1) #retorna apenas o primeiro objeto da lista e "joga" o restante na variavel após o simbolo *.
#posso utilizar da mesma forma para buscar outro objeto da lista.
_, nome2, *_ = ["Icaro", "Alves", "Mota", "Fonseca"]
print(nome2)
"""

#Tupla (imutavel) ----->

nomes = ["Icaro", "Alves", "Mota", "Fonseca"] #caso defina uma "lista" sem colchetes, terá um tipo tuple
#nomes[1] = "outro" #nao funciona, pois um tuple é imutavel.
print(type(nomes))

#o comando tuple() pode ser acionado para transformar uma lista em um tipo tuple
nomes = tuple(nomes)
print(type(nomes))