import re
import os 

os.system('cls' if os.name == 'nt' else 'clear')

text = "Udemy - uma plataforma com muitos cursos"
# 1 Índice inicial e final de palavras
# O r significa uma row string (string crua)
match = re.search(r"uma plataforma", text)
print(f"Indice Inicial: {match.start()}")
print(f"Indice Final: {match.end()}")   

# 2 Busca por índice que possui um ponto.
site = "https://www.udemy.com"
match = re.search(r"\.", site)
print(f"Índice do ponto: {match.start()}")

# 3 Buscando uma lista de caracteres dentro de  uma frase 
pattern = "[g-m]"
result = re.findall(pattern, text)
print(result)

# Verificando o início de uma string
rule = r"^A"
phrases = ["A vida é bela", "O dia está ensolarado", "Vamos passear", "A casa está suja!"]
for f in phrases:
    if re.match(rule, f):
        print(f"Corresponde: {f}")
    else:
        print(f"Não corresponde: {f}")

# Verificando o final de uma string
rule = r"!$"
phrases2 = ["A vida é bela!", "O dia está ensolarado", "Vamos passear!", "A casa está suja!"]
for f in phrases2:
    if re.search(rule, f):
        print(f"Corresponde: {f}")
    else:
        print(f"Não corresponde: {f}")