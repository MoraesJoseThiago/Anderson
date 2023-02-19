idade = int(input("Digite sua idade: "))
autorizacao = str(input("Voce tem autorização? (S/N) "))

if idade >= 18:
    print("Pode ir")

elif autorizacao == "S" or autorizacao == "s":
    print("Pode ir")

else:
    print("Você vai ficar!")