def solicitar_nome_completo():
    """Solicita e retorna o nome completo do usuário."""
    return input("Digite seu nome completo: ")

def converter_para_maiusculas(nome):
    """Converte o nome para letras maiúsculas."""
    return nome.upper()

def converter_para_minusculas(nome):
    """Converte o nome para letras minúsculas."""
    return nome.lower()

def contar_letras_sem_espacos(nome):
    """Retorna o total de letras no nome, excluindo espaços."""
    return len(nome.replace(" ", ""))

def contar_letras_primeiro_nome(nome):
    """Retorna o número de letras no primeiro nome."""
    primeiro_nome = nome.split()[0]
    return len(primeiro_nome)

def exibir_resultados(nome_maiusculo, nome_minusculo, total_letras, letras_primeiro_nome):
    """Exibe os resultados formatados."""
    print(f"Nome em maiúsculas: {nome_maiusculo}")
    print(f"Nome em minúsculas: {nome_minusculo}")
    print(f"Total de letras (sem espaços): {total_letras}")
    print(f"Quantidade de letras no primeiro nome: {letras_primeiro_nome}")

def main():
    """Função principal que orquestra a execução do programa."""
    nome_completo = solicitar_nome_completo()
    
    nome_maiusculo = converter_para_maiusculas(nome_completo)
    nome_minusculo = converter_para_minusculas(nome_completo)
    total_letras = contar_letras_sem_espacos(nome_completo)
    letras_primeiro_nome = contar_letras_primeiro_nome(nome_completo)
    
    exibir_resultados(nome_maiusculo, nome_minusculo, total_letras, letras_primeiro_nome)

if __name__ == "__main__":
    main()