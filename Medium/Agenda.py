#Objetivo: Criar um sistema simples de agenda com busca.
#Descrição: Implemente uma agenda em que o usuário possa:
# Adicionar contato (nome, telefone, e-mail)
# Buscar por nome (busca parcial)
# Listar todos os contatos ordenados por nome
# Salvar os dados em um arquivo .json

import json
import os

AGENDA_FILE = "agenda.json"     #define o nome do json

# Carrega contatos do arquivo JSON
def carregar_contatos():
    if os.path.exists(AGENDA_FILE):
        with open(AGENDA_FILE, 'r', encoding='utf-8') as f:     #Abre o json e lê os dados existentes.
            return json.load(f)
    return {}

# Salva contatos no arquivo JSON
def salvar_contatos(contatos):
    with open(AGENDA_FILE, 'w', encoding='utf-8') as f:     #Abre o json e edita ou adiciona dados.
        json.dump(contatos, f, indent=4, ensure_ascii=False)    #Garante a integridade do texto ao passar para json.

# Adiciona um novo contato
def adicionar_contato(contatos):
    nome = input("Nome: ").strip()
    telefone = input("Telefone: ").strip()
    email = input("E-mail: ").strip()
    contatos[nome] = {"telefone": telefone, "email": email}
    print(f"Contato '{nome}' adicionado com sucesso!")

# Busca contatos por nome (parcial)
def buscar_contato(contatos):
    busca = input("Digite o nome para buscar: ").lower()
    resultados = {nome: dados for nome, dados in contatos.items() if busca in nome.lower()}
    
    if resultados:
        for nome, dados in resultados.items():
            print(f"{nome} - Tel: {dados['telefone']} | E-mail: {dados['email']}")
    else:
        print("Nenhum contato encontrado.")

# Lista todos os contatos ordenados
def listar_contatos(contatos):
    if not contatos:
        print("Agenda vazia.")
        return
    for nome in sorted(contatos.keys()):
        dados = contatos[nome]
        print(f"{nome} - Tel: {dados['telefone']} | E-mail: {dados['email']}")

# Menu principal
def menu():
    contatos = carregar_contatos()
    
    while True:
        print("\n--- AGENDA ---")
        print("1. Adicionar contato")
        print("2. Buscar contato")
        print("3. Listar todos")
        print("4. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            adicionar_contato(contatos)
            salvar_contatos(contatos)
        elif opcao == "2":
            buscar_contato(contatos)
        elif opcao == "3":
            listar_contatos(contatos)
        elif opcao == "4":
            salvar_contatos(contatos)
            print("Agenda salva. Até mais!")
            break
        else:
            print("Opção inválida!")

# Inicia o programa
if __name__ == "__main__":
    menu()
