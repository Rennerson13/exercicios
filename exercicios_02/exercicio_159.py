import math as mt

x = float (input("Entre com o valor de x: "))
nume = 5*x+3
deno = mt.sqrt(x**2 - 16)

if x>4 or x < (-4):
    y = nume/deno
    print(y)
elif x**2 < 16:
    print("Sem solução real")