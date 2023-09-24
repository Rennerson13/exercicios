nome = str(input("Digite seu Nome: "))
idade = int(input("Digite sua Idade: "))

if idade <= 10:
    print(f'{nome}, você receberá R$ 30,00')
elif idade >10 and idade <=29:
    print(f'{nome}, você pagará R$ 60,00')
elif idade >29 and idade <=45:
    print(f'{nome}, você pagará R$ 120,00')
elif idade >45 and idade <=59:
    print(f'{nome}, você pagará R$ 150,00')
elif idade >59 and idade <=65:
    print(f'{nome}, você pagará R$ 250,00')
else:print(f'{nome}, você pagará R$ 400,00')   
