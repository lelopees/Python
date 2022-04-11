with open("arquivo,txt", "r") as arquivo:
    #conteudo = arquivo.read() pega a primeira linha
    # readline > le a primeira linha
    #conteudo = arquivo.readline() 
    for linha in arquivo.readlines():
        print(linha)
