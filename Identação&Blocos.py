#No python é obrigatório a identação para o funcionamento do codigo
def sacar(self, valor: float) -> None:     #Inicio do bloco do método
    if self.saldo >= valor:         #Inicio do bloco do IF
        self.saldo -= valor         

    #Final do bloco do IF

#Final do bloco do método

def sacar(valor):
    saldo = 500

    if saldo >= valor:
        print ("valor sacado!")
        print ("retire o seu dinheiro")
    
    print ("Obrigado por ser nosso cliente,tenha um bom dia!")


sacar(100)