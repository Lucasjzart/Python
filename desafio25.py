def solicitar_nome():
    """Solicita e retorna o nome da pessoa do usuário."""
    return input("Digite o nome da pessoa: ")

def verificar_se_contem_silva(nome):
    """Verifica se o nome contém 'SILVA'."""
    return "SILVA" in nome.strip().upper()

def exibir_resultado(resultado):
    """Exibe se o nome contém ou não 'SILVA'."""
    if resultado:
        print("O nome contém 'SILVA'.")
    else:
        print("O nome NÃO contém 'SILVA'.")

def main():
    """Função principal que orquestra a execução do programa."""
    nome = solicitar_nome()
    contem_silva = verificar_se_contem_silva(nome)
    exibir_resultado(contem_silva)

if __name__ == "__main__":
    main()