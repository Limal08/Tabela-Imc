#CALC IMAC
peso = float(input("Digite o seu peso:  "))
print(peso, "kgs")
altura = float(input("Digite sua altura: " ))
print(altura, "m")
imc= (peso/altura**2)
print("O seu Imc é igual a:", imc)
if imc <= 16:
    print("Magreza grave")
elif imc>= 16 and imc<=16.9:
    print("magreza moderada")
elif imc>= 17 and imc<=18.5:
    print("magreza leve")      
elif imc>= 18.6 and imc<=24.9:
    print("peso ideal")  
elif imc>= 25 and imc<=29.9:
    print("sobrepeso")
elif imc>= 30 and imc<=34.9:
    print("obesidade grau I")
elif imc>= 35 and imc<=39.9:
    print("obesidade grau II ou severa")
elif imc>= 40:
    print("obesidade grau III ou mórbida")