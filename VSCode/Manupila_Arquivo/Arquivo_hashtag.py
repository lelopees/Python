with open("email.txt", "r") as arquivo:
    email = arquivo.read()
    print(email)


with open("mensagem.txt", "r", encoding="utf-8") as arquivo:
    # ele cria uma lista, para cada linha do arquivo
    msg = arquivo.readlines()
    #print(msg)

for linha in msg:
    if "faturamento" in linha:
        print(linha)


#substitui a informação
with open("senha.txt", "w") as arquivo:
   arquivo.write(input("Digite a senha: "))

# acrescenta a informação
with open("email.txt", "a") as arquivo:
   arquivo.write(input("\nDigite o email: "))
