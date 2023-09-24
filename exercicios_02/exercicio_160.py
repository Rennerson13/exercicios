def funcao (x = float):
    if x<1:
        print ("y é 1")
        return 1
    elif x>=1 and x<=2:
        print("Y é 2")
        return 2
    if x>2 and x <= 3:
        print("y é x ao quadrado")
        return x**2
    else:
        print("y é x ao cubo")
        return x**3

x = float(input("Entre com X: "))
y = funcao(x)
print (y)