# logical operators - or, and e not
# or -  alguma das afirmacoes condiz
# not - inverte as condicoes 
# and - ambas afirmacoes condiz

temp = 30
is_sunny = False

if 28 <= temp < 30 and is_sunny:
    print("Está calor")
    print("Esta ensolarado")
elif temp <= 0 and is_sunny:
    print("Esta frio")
    print("Esta ensolarado")
elif temp > 20 and not is_sunny:
    print("Esta quente")
    print("Esta nublado")
elif temp > 20 or is_sunny:
     print("Esta ensolarado")