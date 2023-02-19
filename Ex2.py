nota1 = float(input("Escreva a nota1: "))
nota2 = float(input("Escreva a nota2: "))

total = nota1 + nota2

if nota1 + nota2 > 100:
    print("Sua nota passou de 100, você colocou algum numero errado")
elif total < 60: 
    print("Você reprovou")
else:
    print("Você passou")