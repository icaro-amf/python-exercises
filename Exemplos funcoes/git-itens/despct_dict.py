pessoa = {
    'nome' : 'Icaro',
    'sobrenome' : 'Fonseca',
}

dados = {
    'idade' : 22,
    'altura' : 1.8
}

pessoa_completa = { #empacotamento
    **pessoa,
    **dados,
}

print(pessoa_completa)

def exibir_args_nomeados(*args , **kwargs):
    print('nao nomeado', args)

    for x, y in kwargs.items():
        print(x,y)

exibir_args_nomeados(1, 2, nome = 'Roger', idade = 22)