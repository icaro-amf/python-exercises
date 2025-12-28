#Exercicio do curso de python 3 na udemy
#Fatiamento e funcao len

name = str(input("Insira seu nome: "))
age = int(input("Insira sua idade: "))

if name and age:
    print(f"Seu nome é {name}")
    print(f"Seu nome invertido é {name[::-1]}")
    
    if " " in name:
        print("Seu nome contém espacos!")
    else:
        print("Seu nome não contém espacos!")
    
    print(f"Seu nome tem {len(name)} letras")
    print(f"A primeira letra do seu nome é {name[0]}")
    print(f"A ultima letra do seu nome é {name[-1]}")

else:
    print("Desculpe, você deixou campos vazios.")