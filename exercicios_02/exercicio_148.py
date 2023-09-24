op = int(input("\nDigite:\n1 - Regiao Norte\n2 - Regiao Nordeste\n3 - Regiao Centro-Oeste\n4 - Regiao Sul\nOpção: "))
iv = int(input("\nDigite:\n1 - Ida\n2 - Ida e Volta\nOpção: "))
if op == 1 and iv == 1:
    print("\nO valor da passagem de ida para R. Norte é R$500,00")
elif op == 1 and iv == 2:
    print("\nO valor da passagem de ida e volta para R. Norte é R$900,00")
elif op == 2 and iv == 1:
    print("\nO valor da passagem de ida para R. Nordeste é R$350,00")
elif op == 2 and iv == 2:
    print("\nO valor da passagem de ida e volta para R. Nordeste é R$650,00")
elif op == 3 and iv == 1:
    print("\nO valor da passagem de ida para R. Centro-Oeste é R$350,00")
elif op == 3 and iv == 2:
        print("\nO valor da passagem de ida e volta para R. Centro-Oeste é R$600,00")
elif op == 4 and iv == 1:
    print("\nO valor da passagem de ida para R. Sul é R$300,00")
elif op == 4 and iv == 2:
     print("\nO valor da passagem de ida e volta para R. Sul é R$550,00")
else:
     print("\nOpção Inexistente")

print("\n")



