idade1 = int(input("Digite sua idade: "))

if idade1 >= 25:

    alfabetizado = input("Voce é alfabetizado? (S/N) ")
    
    if alfabetizado == "s"  or alfabetizado == "S":
        print("Voce é alfabetizado e tem 25 anos")
    else:
        print("Voce não é alfabetizado")

else:
    print("Voce não tem 25 anos de idade")
