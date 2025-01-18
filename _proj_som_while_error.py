while True:
    numero_validos = None
    try:
        numero_1 = int(input("Digite um número inteiro: "))
        numero_2 = int(input("Digite o segundo número inteiro: "))
        operador = input("Digite o sinal de (+) para a soma dos números: ")
        
        
        numero_1 = int (numero_1)
        numero_2 = int (numero_2)
        numero_validos = True

        # Verificação do operador permitido
        if operador != "+":
            print("Você não digitou o operador correto")
            continue
        # Realiza a operação de soma
        print(f'A soma dos números é: {numero_1 + numero_2}')

    except ValueError:  # Captura apenas erros de conversão para int
        print("Por favor, digite números inteiros válidos.")
    
    if numero_validos is None:
        print("Você não digitou nenhum número")
        continue

        
    #######    
    sair = input("Deseja encerrar a operação? [s]im ").lower().startswith("s")
    if sair == "s":
        break

print("Obrigado")