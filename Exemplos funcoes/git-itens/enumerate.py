"""
enumerate - enumera iteráveis (índices)
"""

lista = ['Icaro', 'Alves', 'Mota']
lista.append('Fonseca')

# lista_enumerada = enumerate(lista) #tipo enumerate, retorna valor na memoria, temos q trocar o tipo.
# lista_enumerada = list(enumerate(lista))

# print(lista_enumerada)

for indice, nome in enumerate(lista):
    print(indice, nome)