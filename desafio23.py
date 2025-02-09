def solicitar_numero():
    """Solicita e retorna um número inteiro do usuário."""
    return input("Digite um número: ")

def separar_digitos(numero):
    """Separa os dígitos do número em unidade, dezena, centena e milhar."""
    return {
        "unidade": numero[-1],
        "dezena": numero[-2] if len(numero) >= 2 else "0",
        "centena": numero[-3] if len(numero) >= 3 else "0",
        "milhar": numero[-4] if len(numero) >= 4 else "0",
    }

def exibir_digitos(digitos):
    """Exibe os dígitos separados na tela."""
    print(f"Unidade: {digitos['unidade']}")
    print(f"Dezena: {digitos['dezena']}")
    print(f"Centena: {digitos['centena']}")
    print(f"Milhar: {digitos['milhar']}")

def main():
    """Função principal que orquestra a execução do programa."""
    numero = solicitar_numero()
    digitos = separar_digitos(numero)
    exibir_digitos(digitos)

if __name__ == "__main__":
    main()