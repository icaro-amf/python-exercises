# Objetivo:
# Criar um sistema de votação em que usuários podem votar em candidatos e o sistema mostra os resultados.

# Funcionalidades:
# Votar em um candidato
# Mostrar resultados com contagem de votos
# Salvar e carregar os votos de um arquivo .json

import json
import os

CANDIDATOS_FILE = "candidatos.json"

candidatos_iniciais = {

    "Ana": { 
        "idade": "32" ,
        "naturalidade": "Minas Gerais",
        "votos": 0
        },
    "João": { 
        "idade": "32" ,
        "naturalidade": "Minas Gerais",
        "votos": 0
        },
    "Carlos": { 
        "idade": "32" ,
        "naturalidade": "Minas Gerais",
        "votos": 0
        }
    
}

def inicializar_votacao():
    if not os.path.exists(CANDIDATOS_FILE):
        with open(CANDIDATOS_FILE, 'w', encoding='utf-8') as f:
            json.dump(candidatos_iniciais, f, indent=4, ensure_ascii=False)
        print("Arquivo de votação criado com candidatos iniciais.")

def ver_candidatos(candidatos):
    if not candidatos:
        print("Não há candidatos disponíveis para votação.")
    for nome in sorted(candidatos.keys()):
        dados = candidatos[nome]
        print(f"{nome} - Idade: {dados["idade"]} - Naturalidade: {dados["naturalidade"]}")

def votar():
    pass

def resultado():
    pass

inicializar_votacao()