"""
# Dicionário com os valores de desconto
descontos = {
    "DESCONTO10": 0.10,
    "DESCONTO20": 0.20,
    "SEM_DESCONTO": 0.00
}

# Entrada do usuário
preco = float(input().strip())
cupom = input().strip()

# TODO: Aplique o desconto se o cupom for válido:

if cupom == "DESCONTO10":
  preco = preco - (preco*0.10) 
  print(f"{preco:.2F}")  

"""


email = input("Digite o e-mail: ").strip()
numMax = len(email)

# Não pode ter espaço
if " " not in email:
    # Primeiro e último caractere não podem ser "@"
    if email[0] != "@" and email[numMax - 1] != "@":
        # Deve conter pelo menos um "@"
        if "@" in email and ("gmail.com" in email or "outlook.com" in email):
            print("✅ E-mail válido:", email)
        else:
            print("❌ E-mail inválido: falta '@'")