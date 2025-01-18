"""
Calculadora com while
.lower() transforma tudo que for maiúsculo em minúsculo (caso o usuário digite errado)
.startswith informaque a letra inicial tem ue ser s
.endswith("s") termina com s
"""
while True:
    numero_1 = input("Digite um número: ")
    numero_2 = input("Digite o segundo número: ")
    operador = input("Digite o operador (+ - / *): ")

    numeros_validos = None #flag: Em caso de erro ele cai para o except

    try:
        numero_1_float = float(numero_1)
        numero_2_float = float(numero_2) 
        numeros_validos = True                    
    except ValueError:
        numeros_validos = None
        print("error")

    if numeros_validos is None: #Se os número não forem válido é NONE (NÃO VÁLIDOS!)
        print("Um ou ambos os número digitados são inválidos.")
        continue
    
    operadores_permitidos = "+-/*"
    if operador not in operadores_permitidos:
        print("Operador inválido")
        continue

    if len(operador) > 1:
        print("Digite apenas um operador")
        continue

    if operador == "+":
        print(f'{numero_1_float} + {numero_2_float}=', numero_1_float + numero_2_float)
    elif operador == "-":
        print(f'{numero_1_float} - {numero_2_float}=', numero_1_float - numero_2_float)
    elif operador == "/":
        print(f'{numero_1_float} / {numero_2_float}=', numero_1_float / numero_2_float)
    elif operador == "*":
        print(f'{numero_1_float} * {numero_2_float}=', numero_1_float * numero_2_float)
    else:
        print("Deu tudo erro")
    

    #########
    sair = input("Você deseja sair? [s]im: ").lower().startswith("s")
    
    if sair is True:
        break

print("Obrigado")     