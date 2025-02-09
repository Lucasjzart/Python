def solicitar_nome_cidade():
    """Solicita e retorna o nome da cidade do usuário."""
    return input("Digite o nome da cidade: ")

def verificar_se_comeca_com_santo(nome_cidade):
    """Verifica se o nome da cidade começa com 'SANTO'."""
    return nome_cidade.strip().upper().startswith("SANTO")

def exibir_resultado(resultado):
    """Exibe se a cidade começa ou não com 'SANTO'."""
    if resultado:
        print("O nome da cidade começa com 'SANTO'.")
    else:
        print("O nome da cidade NÃO começa com 'SANTO'.")

def main():
    """Função principal que orquestra a execução do programa."""
    nome_cidade = solicitar_nome_cidade()
    comeca_com_santo = verificar_se_comeca_com_santo(nome_cidade)
    exibir_resultado(comeca_com_santo)

if __name__ == "__main__":
    main()