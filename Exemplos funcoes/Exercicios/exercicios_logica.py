"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""
import os

palavra_secreta = "ombros"
letras_acertadas = ""
tentativas = 0

while True:
    letra_digitada = input("Digite apenas uma letra: ").lower()
    tentativas += 1
    if len(letra_digitada) > 1:
        print("Voce digitou mais de uma letra! Digite apenas uma letra para continuar o jogo.")
        continue

    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada

    palavra_formada = ""

    for letra_secreta in palavra_secreta:
       if letra_secreta in letras_acertadas:
           palavra_formada += letra_secreta

       else:
           palavra_formada += "*"

    print("Palavra formada: ", palavra_formada)

    if palavra_formada == palavra_secreta:
        os.system("cls")
        print(f"Voce acertou a palavra secreta! Parabens.\nA palavra era: {palavra_secreta}.\nVoce usou {tentativas} tentativas para acertar.")
        break