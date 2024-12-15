import math

def pesquisa_binaria(lista, item):
    baixo = 0
    alto = len(lista) - 1
    passos = 0  # Contador de etapas

    while baixo <= alto:
        passos += 1
        meio = (baixo + alto) // 2
        chute = lista[meio]

        if chute == item:
            return meio, passos
        if chute > item:
            alto = meio - 1
        else:
            baixo = meio + 1
    return None, passos

# Exemplo com 128 nomes
nomes = [f"Nome {i}" for i in range(1, 129)]
resultado, etapas = pesquisa_binaria(nomes, "Nome 64")

print(f"Resultado: {resultado}, Número de etapas: {etapas}")
