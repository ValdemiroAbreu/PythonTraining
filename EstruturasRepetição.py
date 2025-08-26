#For
#Utilizado para percorrer um objeto iterável, faz sentido usar quando sabemos o número exato de vezes
#que o nosso bloco vai ser executado

texto = input("Informe um texto: ")
VOGAIS = "AEIOU"

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra,end="")
else:
    print()

#Função range
#utilizada para produzir uma sequencia de números inteiros com inicio e fim
# i, i+1, i+2, ..., j-1
#stop(obrigatório), start (opcional) e step opcional

#range com for

for numero in range (0,11):
    print (numero,end=" ")

print()
#range(start,stop,step) step é o incremento
for numero in range (0,51,5):
    print (numero,end=" - ")
print()

#While
#faz sentido usar quando não sabemos o número exato de vezes que vai ser executado

opcao = -1

while opcao != 0:
    opcao = int(input("[1]Sacar \n[2]Extrato \n[0]Sair \n"))

    if opcao == 1:
        print ("Realizando saque... ")
    elif opcao == 2:
        print ("Exibindo seu extrato... ")
    elif opcao == 0:
        print ("Obrigado pela preferência!")
    else:
        print("Digite uma opção válida!")  

#Utilizar o continue caso queira pular a execução e break quando quiser finalizar a execução

while True:
    
    digito = int(input("Informe um número: "))
    
    if digito == 10:
        break

    if digito % 2 == 0:
        continue

    
   
    print (digito)