nome = input("digite seu nome: ")
idade = input("digite sua idade: ")

if nome and idade:
    print(f'Seu nome é: {nome}')
    print(f'Seu nome invertido é: {nome[::-1]}')

    if " " in nome: #(" "aspas seria o espaço), tem espaço dentro(in) do nome?
        print("Seu nome contém espaços")
    else:
        print("Seu nome não contem espaços")

    print(f'Seu nome tem {len (nome)} letras')
    print(f'A primeira letra do seu nome é: {nome[0]}')
    print(f'A última letra do seu nome é: {nome[-1]}')
else:
    print("Desculpe, você deixou os campos vazios")