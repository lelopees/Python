from cgitb import text

texto = "amo python"

print(texto.find("o")) # pega o primeira posição encontrada
print(texto[texto.find("o")+1:].find("o"))  

print(texto.split(" "))
