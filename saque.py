def realizar_saque(saldo, valor_saque):
    if saldo >= valor_saque:
        print("Realizando saque!")
    else:
        print("Saldo insuficiente!")

def main():
    saldo = 2000.0
    valor_saque = float(input("Informe o valor do saque: "))
    
    realizar_saque(saldo, valor_saque)

if __name__ == "__main__":
    main()