

username = str(input("Insira um nome de usuário com até 12 dígitos: "))


if len(username) > 11:
    print(f"{username} não é válido, pois excedeu o limite de dígitos!")
elif not username.find(" ") == -1:
    print("O nome de usuário não pode conter espaço!")
elif not username.isalpha():
    print("O nome de usuário não pode conder números!")
else:
    print(f"Bem-vindo(a), {username}!")