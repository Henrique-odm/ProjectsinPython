#calcular indice de massa corporal IMC
# IMC = peso / (altura*altura)

nome = (input ("Digite seu nome: "))
altura = float (input ("Digite sua altura: "))
peso = float (input ("Digite seu peso: "))
imc = peso / (altura*altura)

linha_1 = f'{nome} tem {altura:.2f} de altura,'
linha_2 = f'pesa {peso} quilos e seu imc é'
linha_3 = f'{imc:.2f}'


if imc <= 16:
    classificacao = "Magreza grau 1"
elif imc <= 25:
    classificacao = "Pré-obesidade"
elif imc <= 35:
    classificacao = "Obesidade moderada"
elif imc <= 40:
    classificacao = "Obesidade severa"
else:
    classificacao = "Obesidade muito severa"
print("Classificação:", classificacao)

print(linha_1)
print(linha_2)
print(linha_3)
