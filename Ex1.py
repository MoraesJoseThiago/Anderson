num1 = float(input("Escreva o 1 Valor: "))
num2 = float(input("Escreva o 2 Valor: "))
num3 = float(input("Escreva o 3 Valor: "))

if num1 > num2 and num1 > num3:
    print("Numero1")
elif num2 > num1 and num2 > num3:
    print("Numero2")
elif num3 > num1 and num3 > num2:
    print("Numero3")
else:
    print("Tem parada errada ai")
    