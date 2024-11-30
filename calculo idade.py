from datetime import date

def calcular_idade():
    try:
        ano_atual = date.today().year
        ano_nascimento = int(input("Digite o ano de nascimento: "))
        
        if ano_nascimento > ano_atual:
            print("O ano de nascimento não pode ser no futuro!")
        else:
            idade = ano_atual - ano_nascimento
            print(f"Você tem {idade} anos.")
    except ValueError:
        print("Por favor, insira um número válido.")

# Executa a função
calcular_idade()
