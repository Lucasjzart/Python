def verificar_par_impar():
    try:
        numero = int(input("Digite um número: "))
        
        if numero % 2 == 0:
            print(f"O número {numero} é par.")
        else:
            print(f"O número {numero} é ímpar.")
    except ValueError:
        print("Por favor, insira um número válido.")

# Executa a função
verificar_par_impar()
