#dicionário sempre tem uma chave e um valor
emails_gerantes ={
    "Iguatemi": "iguatemi@gmail.com",
    "Plaza": "pla@gmail.com",
    "Barra": "barra@gmail.com"
}

email = emails_gerantes['Iguatemi']
print(email)

#adicionando um item no dicionário, caso já existe ele substitui, senão ele adiciona
emails_gerantes["Leblon"] = "leblon@gmail.com"

#listando todos os shopping
for shopping in emails_gerantes:
    print(shopping)

# keys, todas as chaves do dicionário
print(emails_gerantes.keys())

#imprimir todos os emails 
for shopping in emails_gerantes:
    email = emails_gerantes[shopping]
    print(email)

print(emails_gerantes.values())

#remover um item do dicionário
emails_gerantes.pop("Leblon")
print(emails_gerantes)

# se existe o item existe dentro do dicionário, verifica pela chave
if "Leblon" in emails_gerantes:
    print("Existe")
else:
    print("Não existe")

# se existe esse valor dentro do dicionário
if "iguatemi@gmail.com" in emails_gerantes.values():
    print("Existe")
else:
    print("Não existe")




