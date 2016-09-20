#!/usr/bin/env python3
from baralho import Baralho

b = Baralho()
len(b)
print(b[:3])

from random import choice, shuffle

for i in range(5):
    print(choice(b))

print('\nbaralho novinho (na caixa!)')
for carta in b:
    print(carta)

print('\nbaralho embaralhado')
shuffle(b)
for carta in b:
    print(carta)
