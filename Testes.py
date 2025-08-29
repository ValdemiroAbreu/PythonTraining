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
"""
carros = ("gol") 
print(isinstance(carros, tuple))

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
"""

"""
# Lista para armazenar os produtos e preços
carrinho = []
total = 0.0

# Entrada do número de itens
n = int(input().strip())

# Loop para adicionar itens ao carrinho
for _ in range(n):
    linha = input().strip()
    
    # Encontra a última ocorrência de espaço para separar nome e preço
    posicao_espaco = linha.rfind(" ")
    
    # Separa o nome do produto e o preço
    item = linha[:posicao_espaco]
    preco = float(linha[posicao_espaco + 1:])
    
    # Adiciona ao carrinho
    carrinho.append((item, preco))
    total += preco

# TODO: Exiba os itens e o total da compra

for produto, preco in carrinho.items():
    print(f"{produto}: R${preco:.2f}")
    total += preco

print(f"Total: R${total:.2f}")

"""
# Dicionário para agrupar participantes por tema
eventos = {}

# Entrada do número de participantes
n = int(input().strip())

# Loop para armazenar participantes e seus temas
for _ in range(n):
    linha = input().strip()
    
    # Divide pelo separador ", "
    posicao_virgula = linha.rfind(", ")
    
    participante = linha[:posicao_virgula]
    tema = linha[posicao_virgula + 2:]
    
    # Adiciona no dicionário agrupado por tema
    if tema not in eventos:
        eventos[tema] = []
    eventos[tema].append(participante)

# Exibe os grupos organizados
for tema, participantes in eventos.items():
    print(f"{tema}: {', '.join(participantes)}")