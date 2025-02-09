def solicitar_nome_completo():
    """Solicita e retorna o nome completo do usuário."""
    return input("Digite seu nome completo: ")

def separar_primeiro_ultimo_nome(nome_completo):
    """Separa o primeiro e o último nome."""
    nomes = nome_completo.split()
    primeiro_nome = nomes[0]
    ultimo_nome = nomes[-1]
    return primeiro_nome, ultimo_nome

def exibir_resultados(primeiro_nome, ultimo_nome):
    """Exibe o primeiro e o último nome separadamente."""
    print(f"Primeiro nome: {primeiro_nome}")
    print(f"Último nome: {ultimo_nome}")

def main():
    """Função principal que orquestra a execução do programa."""
    nome_completo = solicitar_nome_completo()
    primeiro_nome, ultimo_nome = separar_primeiro_ultimo_nome(nome_completo)
    exibir_resultados(primeiro_nome, ultimo_nome)

if __name__ == "__main__":
    main()