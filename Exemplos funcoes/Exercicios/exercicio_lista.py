"""
Faça uma lista de valores com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com 
erros de índices inexistentes na lista.
"""

import os

lista = []

while   True:
    opcao = input("Selecione uma opcão:\n[i] inserir\t[a] apagar\t[l] listar\n").lower()

    if opcao == "i":
        os.system("cls")
        valor = input("Valor: ")
        lista.append(valor)

    elif opcao == "a":
        indice_str = input("Escolha o índice para apagar: ")

        try:
            indice = int(indice_str)
            del lista[indice]
        except ValueError:
            print('Por favor digite número int.')
        except IndexError:
            print('Índice não existe na lista')
        except Exception:
            print('Erro desconhecido')
            
    elif opcao == "l":
        os.system("cls")

        if len(lista) == 0:
            print("Nada para listar")

        for i, valor in enumerate(lista):
            print(i," - ", valor)
    else:
        print("Por favor, escolha i, a ou l.")