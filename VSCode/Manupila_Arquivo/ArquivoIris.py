from email.mime import base

basedados = []

with open("iris.data", "r") as arquivo:
    for registro in arquivo.readlines():
        basedados.append(registro.split(","))
    
#print(basedados)

print('Total = ' + str(float(basedados[0][0]) + float(basedados[0][1]) +
      float(basedados[0][2]) + float(basedados[0][3])) + ' ' + basedados[0][4])

print('Total = ' + str(float(basedados[1][0]) + float(basedados[1][1]) +
      float(basedados[1][2]) + float(basedados[1][3])) + ' ' + basedados[1][4])

for lista in basedados:
    vai = 0
    flor = ""
    for elemento in lista:
        if type(elemento) is float:
            print('aqui')
            vai = vai + elemento
        else:
            flor = elemento
    print('Total ' + str(vai) + ' ' + flor)




