DOMINIOS = ['gmail.com', 'outlook.com']

def main():
    resultado = validador(input("E-mail: ").strip())
    print("E-mail válido" if resultado else "E-mail inválido")

def validador(email):
    try:
        user, dominio = email.split("@")
    except Exception:
        return False
    else: 
        if dominio not in DOMINIOS or email.startswith("@") or email.endswith("@") or " " in email:
            return False
        else:
            return True
        
main()