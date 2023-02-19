idade = int(input("Digite sua idade: "))
categoria = str(input("--------------------------\nDigite 1 se você for estudante.\nDigite 2 se você for aposentado\nDigite 3 se você for portador de alguma deficiencia.\nCaso ao contrario digite 0: "))

if categoria == 1:
    print("Voce tem 5% de desconto")
elif categoria == 2:
    print("Voce tem 10% de desconto")
elif categoria == 3:
    print ("Voce tem 12% de desconto")
else:
    print("Você não tem desconto")  