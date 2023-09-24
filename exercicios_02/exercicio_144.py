salario = float(input("Entre com o Salário:  "))


if salario >0 and salario <=500:
    print(f'Você tem 0 de crédito')
elif salario > 500 and salario <=1000:
    print(f'O Valor de credito será {salario*0.3}')
elif salario > 1000 and salario <=3001:
    print(f'O Valor de crédito será {salario*0.4}')
else:
    print(f'O Valor de crédito será de {salario*0.5}')
    
if salario == 0:
    print("Você não possui disponibilidade de crédito")
if salario <0:
    print("Pague o Banco")