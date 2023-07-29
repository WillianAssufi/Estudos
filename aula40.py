try:
    print("Digite o Número referente a operação desejada:")

    inp_op = input(
        "0 - Sair\n1 - Soma\n2 - Subtração\n3 - Divisão\n4 - Multiplicação\n\n")
    inp_op = int(inp_op)
    lista = [0, 1, 2, 3, 4]
    if inp_op in lista:
        while inp_op != 0:
            opcao = 1
            while opcao != 0:

                num1 = input("\nDigite o primeiro número: ")
                num2 = input("Digite o segundo número: ")
                num1 = int(num1)
                num2 = int(num2)
                inp_op = int(inp_op)
                resultado = 0
                if inp_op == 1:
                    resultado = num1 + num2
                    print(f"\nA soma dos números é igual a: {resultado}\n")
                elif inp_op == 2:
                    resultado = num1 - num2
                    print(
                        f"\nA subtração dos números é igual a: {resultado}\n")
                elif inp_op == 3:
                    resultado = num1 / num2
                    print(f"\nA divisão dos números é igual a: {resultado}\n")
                elif inp_op == 4:
                    resultado = num1 * num2
                    print(
                        f"\nA multiplicação dos números é igual a: {resultado}\n")

                print("Deseja realizar outra operação?")
                opcao = input(
                    "9 - Continuar\n0 - Sair\n\n")
                opcao = int(opcao)
                if opcao == 9:
                    inp_op = input(
                        "\n1 - Soma\n2 - Subtração\n3 - Divisão\n4 - Multiplicação\n\n")
                    continue
                elif opcao == 0:
                    break
                break
            break
    else:
        print("A operação desejada não existe!")
except:
    print("O digito informado não é um número inteiro!")

print("\nPrograma encerrado!")


"""AULA

 # Calculadora com while 
while True:
    numero_1 = input('Digite um número: ')
    numero_2 = input('Digite outro número: ')
    operador = input('Digite o operador (+-/*): ')

    numeros_validos = None

    try:
        num_1_float = float(numero_1)
        num_2_float = float(numero_2)
        numeros_validos = True
    except:
        numeros_validos = None

    if numeros_validos is None:
        print('Um ou ambos os números digitados são inválidos.')
        continue

    operadores_permitidos = '+-/*'

    if operador not in operadores_permitidos:
        print('Operador inválido.')
        continue

    if len(operador) > 1:
        print('Digite apenas um operador.')
        continue

    ###

    sair = input('Quer sair? [s]im: ').lower().startswith('s')

    if sair is True:
        break

"""