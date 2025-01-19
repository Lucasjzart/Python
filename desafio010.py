valor_conta = float(input("Quanto vocë tem na sua conta? R$ "))
cotacao_dolar = 6.25
quantidade_dolar = valor_conta / cotacao_dolar
print(f"Com R$ {valor_conta:.2f}, você pode comprar US$ {quantidade_dolar:.2f}.")
