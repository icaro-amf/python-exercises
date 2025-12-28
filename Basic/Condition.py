# Crie um programa que peça uma nota de 0 a 10 e diga se o aluno foi:
# Aprovado (≥ 7), Recuperação (5 a 6.9), ou Reprovado (< 5).
# Faça um programa que peça um número e diga se ele é par ou ímpar.
# Peça o ano de nascimento e diga se a pessoa é maior de idade.

print("Bem-vindo ao Sistema da Escola Municipal Ciclano Fulano Beltrano!\n")

while True:
    dados = {}

    dados["nome"] = input("Qual seu nome?\n")
    dados["classe"] = input("Qual sua turma?\n")
    dados["nota"] = float(input("Qual foi sua nota?\n"))

    confirmacao = input(f"Olá, {dados["nome"]}! Você está na turma {dados['classe']} e sua nota foi {dados['nota']}, correto?\n[S/N]:\n")
    confirmacao = confirmacao.upper()
    
    if confirmacao == "S":
        if 10 >= dados["nota"] >= 7:
            print("Parabéns! Você foi aprovado, boas férias!")
        elif 5 <= dados["nota"] < 7:
            print("Poxa! Sua nota não foi muito boa, está de recuperação!")
        elif 0 <= dados["nota"] < 5: 
            print("Infelizmente você está reprovado, mais sorte da próxima vez!")
        else: 
            print("\nConfira se inseriu corretamente a informação de sua nota!\n") 
            continue
        break

    elif confirmacao == "N":
        print("Peço perdão pelo erro!\nInsira seus dados novamente!\n")
        continue

    else:
        print("Por favor, verifique a sua resposta!\nEla deve seguir o parametro! [S: sim / N: não]\n")
        continue