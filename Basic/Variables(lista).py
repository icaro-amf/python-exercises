# Crie um programa que peça seu nome, idade e cidade
# Crie um conversor de temperaturas (Celsius ↔ Fahrenheit).
# Peça dois números e mostre a soma, subtração, multiplicação e divisão.

while True:
    dados = [] #Irei criar uma lista parar depositar as informacoes necessarias para q possa puxar com base no indice posteriormente

    dados.append(input("Qual seu nome?\n")) #.append para o usuario adicionar o dado no primeiro lugar vago da lista. [0]
    dados.append(input("Quantos anos você tem?\n")) #[1]
    dados.append(input("Onde você mora?\n")) #[2]

    confirmacao = (input(f"Olá, {dados[0]}!\nVocê tem {dados[1]} anos e mora em {dados[2]}, certo?\n[S/N]:\n")) #Nesse momento achei legal a criacao de um "sistema" para confirmar os dados (foi nessa hora que implementei o while)
    confirmacao = confirmacao.upper() #para deixar pratica a identificacao da resposta, deixei em maiusculo a confirmacao do usuario

    if confirmacao == "S":
        print("Você está cadastrado na plataforma!")
        break

    elif confirmacao == "N":
        print("Dados incorretos, favor, refaça o questionário!")
        continue

    else:
        print("Selecione uma das opções, por favor!\n") # MELHORIA: fazer esse else retornar na parte do input da variavel "confirmacao".
        continue

