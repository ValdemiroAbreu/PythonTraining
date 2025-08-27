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


#Interpolação de variáveis
#Utilizando %,format e f strings 

nome = "Valdemiro"
idade = 24
profissao = "Programador"
linguagem = "Python"
#Usando %
print("Olá,me chamo %s. Eu tenho %d anos de idade,trabalho como %s e estou matriculado no curso de %s." % (nome,idade,profissao,linguagem))
#Usando format
#1º colocando as variaveis na sequencia de exibição e na 2ª ajustando a numeração de acordo com sua posição
print("Olá,me chamo {}. Eu tenho {} anos de idade,trabalho como {} e estou matriculado no curso de {}." .format (nome,idade,profissao,linguagem))
print("Olá,me chamo {3}. Eu tenho {2} anos de idade,trabalho como {1} e estou matriculado no curso de {0}." .format (linguagem,profissao,idade,nome))
print("Olá,me chamo {nome}. Eu tenho {idade} anos de idade,trabalho como {profissao} e estou matriculado no curso de {linguagem}." 
      .format (nome = nome,idade=idade,profissao=profissao,linguagem=linguagem))
#print("Olá,me chamo {nome}. Eu tenho {idade} anos de idade,trabalho como {profissao} e estou matriculado no curso de {linguagem}." 
#      .format (**pessoa))

#Usando f-string
print(f"Olá,me chamo {nome}. Eu tenho {idade} anos de idade,trabalho como {profissao} e estou matriculado no curso de {linguagem}.") 

PI = 3.14159

print (f"Valor de PI: {PI:.2f}") #Depois do ponto é as casa decimais
print (f"Valor de PI: {PI:10.4f}") #Antes do ponto é a quantidade de caracteres

#Fatiamento de strings
#usado para retornar substrings, informando inicio(start) fim (stop) e passo (step) [start:stop[,step]]

nome = "Valdemiro Dantas"
#Buscando a letra pelo índice
print(nome[0])
print(nome[10:])
print(nome[:10])
print(nome[6:12])
#Onde inicia,onde para,quantos passos
print(nome[2:17:2])
#Para espelhar a string
print(nome[:: -1])

mensagem = f'''
    Olá,me chamo {nome},
        Eu estou aprendendo {linguagem}.
E esta mensagem tem recuos diferentes!!

'''
print(mensagem)









