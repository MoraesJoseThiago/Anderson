num = int(input("Digite o numero que voce quer: "))

if num % 2 == 0:
    print(num, "é um número par")

elif num % 3 == 0:
    print(num, "é divisível por 3")
    
else:
    print(num, "não é par e não é divisível por 3")
