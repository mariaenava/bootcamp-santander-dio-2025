# Dicionário com os valores de desconto
descontos = {
    "DESCONTO10": 0.10,
    "DESCONTO20": 0.20,
    "SEM_DESCONTO": 0.00
}

# Entrada do usuário
preco = float(input("Preço: ").strip())

# Aplique o desconto se o cupom for válido:
while True:
    cupom = input("Cupom de Desconto: ").strip().upper()
    if cupom in descontos:
        desconto = preco * descontos[cupom]
        valor_final = preco - desconto
        print(f"{valor_final:.2f}")
        break
    else:
        print("Cupom inválido! Tente novamente.")