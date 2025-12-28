from wordlist import palavras
import random

forca = {0: ("  ",
             "  ",
             "  "),
        1:  (" o ",
             "   ",
             "   "),
        2:  (" o ",
             " |  ",
             "   "),
        3:  (" o ",
             "/|  ",
             "   "),
        4:  (" o ",
             "/|\\ ",
             "   "),
        5:  (" o ",
             "/|\\ ",
             "/  "),
        6:  (" o ",
             "/|\\ ",
             "/ \\ ")}

def display_forca(entrada_incorreta):
    print("********")
    for linha in forca[entrada_incorreta]:
        print(linha)
    print("********")

def display_tentativa(tentativa):
    print(" ".join(tentativa))

def display_resposta(resposta):
     print(" ".join(resposta))


def main():
    resposta = random.choice(palavras)
    tentativa = ["_"] * len(resposta)
    entrada_incorreta = 0
    letra_enviada = set()
    is_running = True

    while is_running:
          display_forca(entrada_incorreta)
          display_tentativa(tentativa)
          letra = input("Entre com uma letra: ").lower()

          if len(letra) != 1 or not letra.isalpha():
               print("Entrada invalida")
               continue

          if letra in letra_enviada:
               print(f"{letra} já foi enviada!")
               continue
          
          letra_enviada.add(letra)

          if letra in resposta:
               for i in range(len(resposta)):
                    if resposta[i] == letra:
                         tentativa[i] = letra
          else:
               entrada_incorreta +=1

          if "_" not in tentativa:
               display_forca(entrada_incorreta)
               display_resposta(resposta)
               print("Voce ganhou!")
               is_running = False
          elif entrada_incorreta >= len(forca) -1:
               display_forca(entrada_incorreta)
               display_resposta(resposta)
               print("Voce perdeu!")     
               is_running = False
                   
if __name__ == "__main__":
    main()