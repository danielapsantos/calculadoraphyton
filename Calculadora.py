def calculadora():
    while True:
        print("Calculadora Simples")
        print()
        print("1 - Soma")
        print("2 - Subtração")
        print("3 - Multiplicação")
        print("4 - Divisão")
        print("S - Sair")
        operacao = input("Selecione uma opção ou S para sair.")

        if operacao == 's' or operacao == 'S':
            print("Obrigada por utilizar a Calculadora Simples.")
            break

        if operacao not in ['1','2','3','4']:
            print("Opção inválida! Tente novamente.")
            continue

        numero_1 = float(input("Digite o primeiro número: "))
        numero_2 = float(input("Digite o segundo número: "))

        if operacao == '1':
            resultado = numero_1 + numero_2
            print("O resultado da soma é: ", resultado)

        elif operacao == '2':
            resultado = numero_1 - numero_2
            print("O resultado da subtração é: ", resultado)

        elif operacao == '3':
            resultado = numero_1 * numero_2
            print("O resultado da multiplicação é: ", resultado)

        else:
            if numero_2 == 0:
                print("Divisão por 0 não é possível. Tente novamente!")
                continue
            else:
                resultado = numero_1 / numero_2
                print("O resultado da divisão é: ", resultado)

calculadora()