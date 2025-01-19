salario_funcionario = float(input("Digite seu salario: R$ "))
aumento = 15 / 100
salario_com_aumento = salario_funcionario * (1 + aumento)

print(f"O preço original do produto é R$ {salario_funcionario:.2f}.")
print(f"Com desconto de 5%, o preço final é R$ {salario_com_aumento:.2f}.")