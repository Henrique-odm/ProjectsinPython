while True:
    numero_validos = None
    try: 
        numero = 4  
        numero = input("Tente adivinhar o número correto de 1 á 10: ")
        
        numero = int (numero)
        numero_validos = True
        if numero != 4:
            print("Você ainda não acertou o número!")
            continue
        if numero == 4:
            print("Você acertou o número, Parabéns!")
            break

    except ValueError:
        print("Por favor, digite números inteiros válidos.")
    if numero_validos is None:
        print("Você não digitou nenhum número")
        continue   
           
print("Obrigado")
        
