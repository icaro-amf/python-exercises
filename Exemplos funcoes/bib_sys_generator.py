import sys

# Generator expression, Iterables e Iterators em Python
iterable = ['Eu', 'Tenho', '__iter__']
iterator = iter(iterable)  # tem __iter__ e __next__
lista = [n for n in range(1000000)]
generator = (n for n in range(1000000))

# print(sys.getsizeof(lista))
# print(sys.getsizeof(generator))

# print(generator)

for n in generator:
    print(n)

# Introdução às Generator functions em Python
# generator = (n for n in range(1000000))

def generator(n=0, maximum=10):
    while True:
        yield n
        n += 1

        if n >= maximum:
            return


gen = generator(maximum=1000000)
for n in gen:
    print(n)