preco_produto = float(input("Digite o preço do produto: R$ "))
desconto = 5 / 100
preco_com_desconto = preco_produto * (1 - desconto)

print(f"O preço original do produto é R$ {preco_produto:.2f}.")
print(f"Com desconto de 5%, o preço final é R$ {preco_com_desconto:.2f}.")
