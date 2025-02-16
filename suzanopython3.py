# Definição de constantes para os valores dos produtos
PRECO_PRODUTO_1 = 20
PRECO_PRODUTO_2 = 10

# Função para calcular a soma dos produtos
def calcular_soma(preco1, preco2):
    return preco1 + preco2

# Função para exibir o resultado
def exibir_resultado(soma):
    print(f"A soma dos produtos é: {soma}")

# Fluxo principal do programa
soma_produtos = calcular_soma(PRECO_PRODUTO_1, PRECO_PRODUTO_2)
exibir_resultado(soma_produtos)