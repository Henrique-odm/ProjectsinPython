try:
    numero_1 = int(input("Digite um número: "))
    numero_2 = int(input("Digite o segundo número: "))
    soma = numero_1 + numero_2
except:
    print("Você deve digitar um número inteiro.")
else:
    print(f' a soma dos dois número é: {soma}')