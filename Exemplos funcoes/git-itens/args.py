x, y, *resto = 1, 2, 3, 4

#def soma(x,y):
#   return x + y

def soma(*args): #EMPACOTAMENTO
    total = 0
    for numero in args:
        total += numero
    return total

soma_1 = soma(1, 4)
print(soma_1)

desempac = 1,2,3,4,5,6,7,8,9,10 #DESEMPACOTAMENTO
print(*desempac)