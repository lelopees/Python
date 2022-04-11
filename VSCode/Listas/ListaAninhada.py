matriz = [[2.0, 2.1, 2.2, 'Le'], [3.0, 3.1, 3.2, 'Alexandra'], [4.0, 4.1, 4.2, 'Leo']]

print("Matriz 3x3: ", matriz)

# A sintaxe abaixo será explicada posteriormente.
print("Matriz impressa de outra forma:")
for lista in matriz:
    for elemento in lista:
        print(elemento, end=' ')
    print()

for lista in matriz:
    vai = 0
    flor = ""
    for elemento in lista: 
        if type(elemento) is float:
           # print(type(elemento) is float)
            vai = vai + elemento 
        else:
            flor= elemento
    print(flor + ' = ' + str(vai))


