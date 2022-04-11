usuarios = {}
opcao = perguntar()

while opcao=="I" or opcao=="P" or opcao=="E" or opcao=="L":
    if opcao=="I":
        inserir(usuarios)
    opcao = perguntar()

def perguntar():
    return input("O que deseja realizar?\n" +
                 "<I> - Para Inserir um usuário\n" +
                 "<P> - Para Pesquisar um usuário\n" +
                 "<E> - Para Excluir um usuário\n" +
                 "<L> - Para listar um usuário:").upper()


def inserir(dicionario):
    dicionario[input("Digite o login: ").upper()] = [input("Digite o nome").upper(),
                                                     input(
                                                         "Digite a última data de acesso:"),
                                                     input("Digite a última estação acessada:").upper()]
