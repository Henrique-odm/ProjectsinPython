try:
    numero = int(input("Digite um número de 1 a 10: "))
    tabuada_1 = f'{numero}x1={numero * 1}'
    tabuada_2 = f'{numero}x2={numero * 2}'
    tabuada_3 = f'{numero}x3={numero * 3}'
    tabuada_4 = f'{numero}x4={numero * 4}'
    tabuada_5 = f'{numero}x5={numero * 5}'
    tabuada_6 = f'{numero}x6={numero * 6}'
    tabuada_7 = f'{numero}x7={numero * 7}'
    tabuada_8 = f'{numero}x8={numero * 8}'
    tabuada_9 = f'{numero}x9={numero * 9}'
    tabuada_10 = f'{numero}x10={numero * 10}'
    
except ValueError:
    print("Você não digitou um número inteiro.")
else:
    print(f'Segue a sequêcia da tabuada de multiplicação: {tabuada_1}, {tabuada_2}, {tabuada_3}, {tabuada_4},\
{tabuada_5}, {tabuada_6}, {tabuada_7}, {tabuada_8}, {tabuada_9}, {tabuada_10}')