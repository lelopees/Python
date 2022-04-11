from IdentificacaodeFuncoes import preencherInventario, localizarPorNome, depreciarPornome, excluirPorSerial,exibirInventario, resumirValores

minhaLista=[]
print("Preenchendo")

preencherInventario(minhaLista)
print("Exibindo")
exibirInventario(minhaLista)

print("Pesquisando")
localizarPorNome(minhaLista)
print("Alterando")
depreciarPornome(minhaLista, 20)

print("Excluindo")
print(excluirPorSerial(minhaLista))
exibirInventario(minhaLista)

print("Resumindo")
resumirValores(minhaLista)
