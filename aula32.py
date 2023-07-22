"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

# num = input("Digite um número inteiro: ")

# try:
#     par_impar = int(num) % 2
#     if par_impar == 0:
#         print("O número que você digitou é par")
#     else:
#         print("O número que você digitou é ímpar")
# except:
#     print("O que você digitou não é um número inteiro")

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

# hora_atual = input("Digite uma hora: ")

# hora = int(hora_atual)

# horario_dia = [0,1,2,3,4,5,6,7,8,9,10,11]
# horario_tarde = [12,13,14,15,16,17]
# horario_noite = [18,19,20,21,22,23]

# if hora in horario_dia:
#     print("Bom dia")
# elif hora in horario_tarde:
#     print("Boa tarde")
# elif hora in horario_noite:
#     print("Boa noite")   
# else:
#     print("Isso não é uma hora valída")

# try:
#     hora = int(hora_atual)
#     if hora >= 0 and hora <= 11:
#         print("Bom dia")
#     elif hora >= 12 and hora <= 17:
#         print("Boa tarde")
#     elif hora >= 18 and hora <= 23:
#         print("Boa noite")
#     else:
#         print("Isso não é uma hora valída")
# except:
#     print("Por favor digite apenas números inteiros!")

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

# prim_nome = input("Digite seu primeiro nome:")

# nome = len(prim_nome)

# if prim_nome.isalpha():
#     if nome > 0 and nome <= 4:
#         print("Seu nome é curto")
#     elif nome > 4 and nome <= 6:
#         print("Seu nome é normal")
#     else:
#         print("Seu nome é muito grande")
# else:    
#     print("Esse não é um nome valído!")
