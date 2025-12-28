# Manipulando chaves e valores em dicionarios
"""
pessoa = {}

chave = 'nome' #Key dinamica, consigo mudar o valor que retorna no dicionario dinamicamente, alterando somente o valor dessa chave dinamica

pessoa[chave] = "Icaro"
pessoa['sobrenome'] = "Fonseca"

print(pessoa[chave])

pessoa[chave] = "Igor"
print(pessoa)

#posso deletar um element da biblioteca cm o comando del

del pessoa['sobrenome']
print(pessoa)

#para "pular" uma excessao no dicionario, podemos usar o .get


if pessoa.get('sobrenome') is None:
    print('nao existe sobrenome')

else:
    print(pessoa['sobrenome'])

print("Vai passar ou nao?")
"""
# Métodos úteis dos dicionários em Python
# len - quantas chaves
# keys - iterável com as chaves
# values - iterável com os valores
# items - iterável com chaves e valores
# setdefault - adiciona valor se a chave não existe
# copy - retorna uma cópia rasa (shallow copy)
# get - obtém uma chave
# pop - Apaga um item com a chave especificada (del)
# popitem - Apaga o último item adicionado
# update - Atualiza um dicionário com outro
pessoa = {
    'nome': 'Icaro',
    'sobrenome': 'Fonseca',
    'idade': 22,
}

d2 = pessoa.copy()
d2['idade'] = 32
print(pessoa)
print(d2)
#d2 = pessoa
#d2['idade'] = 32

#print(pessoa) #ira retornar o novo valor atribuido a d2, porque ao usar o sinal de igual para atribuir valores do dict, estamos nao apenas puxando os dados de pessoa, mas sim, direcionando o valor da nova variavel.
#copy nao funciona com subniveis! Listas dentro de dict ainda serao alteradas no dicionario primario mesm usando .copy()

#pessoa.setdefault('idade', 0)
#print(pessoa['idade'])
#print(len(pessoa))
#print(list(pessoa.keys()))
#print(list(pessoa.values()))
#print(list(pessoa.items()))

for valor in pessoa.values():
   print(valor)

#for chave, valor in pessoa.items():
#    print(chave,":", valor)
# pessoa.update(nome = "Ana", idade = "23", sexo = "feminino")
# print(pessoa)