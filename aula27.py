"""
Fatiamento de strings
 012345678
 Olá mundo
-987654321
Fatiamento [i:f:p] [::]
Obs.: a função len retorna a qtd 
de caracteres da str
"""
variavel = 'Olá mundo'
print(variavel[::-1])
print(variavel[::1])
print(variavel[4:9])
print(variavel[-9:-6])
print(len(variavel))
print(len(variavel[0:9]))
