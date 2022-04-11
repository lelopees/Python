lista_materiais = []

def cadastrarMateriais(nome, codigo, unidade, quantidade):
    tupla = (nome, codigo, unidade, quantidade)
    lista_materiais.append(tupla)
    return lista_materiais


def consultarMateriais(codigo):
    for material in lista_materiais:
        if material[1] == codigo:
            return print(material)
        else:
            pass

cadastrarMateriais ('Borracha', 1, 'un.', 500)
cadastrarMateriais('Tesoura', 2, 'un.', 200)

print(lista_materiais)

material2 = int(input('Digite o material: '))

consultarMateriais(material2)




