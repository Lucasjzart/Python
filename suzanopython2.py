def obter_nome_usuario():
    """Solicita e retorna o nome do usuário."""
    return input("Digite seu nome: ")

def exibir_nome_usuario(nome):
    """Exibe o nome do usuário."""
    print(f"O nome digitado foi: {nome}")

# Fluxo principal do programa
nome_usuario = obter_nome_usuario()
exibir_nome_usuario(nome_usuario)     