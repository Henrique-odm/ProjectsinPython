#letras na horizontal
nome = "Henrique Andrade"
indice = 0 #primeira letra iterável
novo_nome = ""

while indice < len(nome):
    print(nome[indice])
    indice += 1
print(novo_nome) 

#///////letras na vertical///////
nome = "Henrique Andrade" #ITERÁVEIS
indice = 0
novo_nome = ""

while indice < len(nome):
    letra = nome[indice]
    novo_nome += f'*{letra}'
    indice += 1
print(novo_nome) 
