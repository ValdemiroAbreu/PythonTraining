#MAIÚSCULA, minúscula e Título

curso = "pYtHoN"

print(curso.upper())
print(curso.lower())
print(curso.title())
print()
#Eliminando espaços em branco

curso = "     Python  "

print(curso.strip())
print(curso.lstrip()) #elimina espaço a esquerda
print(curso.rstrip()) #elimina espaço a direita

# Junções e centralização

curso = "Python"

print(".".join(curso))

print(curso.center(10,"#")) #10 define total de caracteres, e o 
# é opcional que vai compor o restante dos caracteres

for letra in curso:
    print(letra,end="-")
print()

print("-".join(curso))