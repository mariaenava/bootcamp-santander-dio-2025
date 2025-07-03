descontos = {
    "DESCONTO10": 0.10,
    "DESCONTO20": 0.20,
    "SEM_DESCONTO": 0.00
}

def main():
    resultado = aplica_desconto(float(input("Preço: ").strip()))
    print(f"Preço final: R${resultado:.2f}")


def aplica_desconto(preco):
    while True:
        cupom = input("Cupom de Desconto: ").strip().upper()
        if cupom in descontos:
            desconto = preco * descontos[cupom]
            valor_final = preco - desconto
            return valor_final
        else:
            print("Cupom inválido! Tente novamente.")

main()
