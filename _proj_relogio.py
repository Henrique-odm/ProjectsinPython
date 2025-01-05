"""
Faça um programa que pergunte a hora ao usuário e baseando-se no horário
descrito, exiba a saudação apropriada. 
Ex. Bom dia 0-11, boa tarde 12-12 e boa noite 18-23.
"""
try:
    hora = float(input("what time is it? "))

    if 0 <= hora <= 11:
        print("Good morning")
    elif 12 <= hora <= 17:
        print("Good afternoon")
    elif 18 <= hora <= 23:
        print("Good night")
    else:
        print("Please enter a valid hour between 0 and 23.") 
except ValueError:
    print("You did not enter a valid number.") #tratamento de erro / ValueError: processo de entrada inadequadas

finally:
    print("Thanks!") #finally: finalizar o programa


      



