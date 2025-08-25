#if/if...else/elif
"""
saldo = 1000
opcao = int(input("Informe a opção:\n[1] Sacar \n[2] Extrato \n"))
if opcao == 1:
    valor = float(input("Informe o valor para o saque: \n"))
    saldo -= valor
elif opcao == 2:
    print ("Seu extrato: " + str(saldo))
else:
    SystemExit("Opção Inválida")    
"""
#Outro exemplo com o IF aninhado
'''
conta_normal= False
conta_universitaria= True

saldo = 2000
saque = 2500
cheque_especial= 2000

if conta_normal:
    if saldo >= saque:
        print("Saque realizado com sucesso!")
    elif saque <= (saldo + cheque_especial):
        print("Saque realizado com uso do cheque especial!")
if conta_universitaria:
    if saldo >= saque:
        print("Saque realizado com sucesso!")
    else :
        print("Saldo insuficiente!")        
'''      
#If ternário
saque = 2000
saldo = 1250

status = "Sucesso" if saldo >= saque else "Falha"

print(f"{status} ao realizar o saque")
