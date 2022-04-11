tabuada = int(input("Digite um numero para exibir a tabuada:"))
print("Tabuada do número", tabuada)

# inicio, fim, incremento
for valor in range(1,11,1):
    print(str(tabuada) + " x " + str(valor) + " = " + str((tabuada*valor)))