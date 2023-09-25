nome = str(input("Entre com o nome do paciente: "))
peso = float(input("Entre com o peso do paciente: em KG "))
altura = float(input("Entre com a atura do paciente: em Metros "))

imc = peso/(altura**2)
print(f'Imc de {imc}')

if imc < 20:
    print(f'{nome} está abaixo do peso')
elif imc >=20 and imc <= 25:
    print(f'{nome} está com peso normal do peso')
elif imc >25 and imc <= 30:
    print(f'{nome} está com peso excesso do peso')
elif imc >30 and imc <= 35:
    print(f'{nome} está com obesidade')
else:
    print(f'{nome} está com obesidade mórbida')
