"""
Faça um programa que peça o primeiro nome do usuário. 
4 letras ou menos escreva: "Seu nome é curto"; 
5 e 6 letras: "Seu nome é normal";
6 letras ou mais:"Seu nome é muito grande"
"""

nome = input("Digite seu primeiro nome: ") 

if not nome.isalpha(): #nome.isalpha() corrige o usuário para digitar somente letras
    print("você não digitou seu nome")

else:
    tamanho = len(nome)
    if tamanho > 1:
        print(f'Seu nome tem {tamanho} letra, seu nome é curto!')
    if tamanho <= 4:
        print(f'Seu nome tem {tamanho} letras, seu nome é curto!')
    elif 5 <= tamanho <= 6:
        print(f'Seu nome tem {tamanho} letras, seu nome é normal!')
    else:
        print(f'Seu nome tem {tamanho} letras, seu nome é muito grande!')

    
