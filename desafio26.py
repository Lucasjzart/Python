def solicitar_frase():
    """Solicita e retorna uma frase do usuário."""
    return input("Digite uma frase: ")

def contar_ocorrencias_r(frase):
    """Conta quantas vezes a letra 'R' aparece na frase."""
    return frase.upper().count("R")

def encontrar_posicao_primeiro_r(frase):
    """Encontra a posição da primeira ocorrência da letra 'R' na frase."""
    return frase.upper().find("R") + 1  # +1 para posição começando em 1

def encontrar_posicao_ultimo_r(frase):
    """Encontra a posição da última ocorrência da letra 'R' na frase."""
    return frase.upper().rfind("R") + 1  # +1 para posição começando em 1

def exibir_resultados(ocorrencias, primeira_posicao, ultima_posicao):
    """Exibe os resultados da análise da frase."""
    print(f"Quantidade de vezes que 'R' aparece: {ocorrencias}")
    print(f"Posição da primeira ocorrência de 'R': {primeira_posicao}")
    print(f"Posição da última ocorrência de 'R': {ultima_posicao}")

def main():
    """Função principal que orquestra a execução do programa."""
    frase = solicitar_frase()
    ocorrencias = contar_ocorrencias_r(frase)
    primeira_posicao = encontrar_posicao_primeiro_r(frase)
    ultima_posicao = encontrar_posicao_ultimo_r(frase)
    exibir_resultados(ocorrencias, primeira_posicao, ultima_posicao)

if __name__ == "__main__":
    main()