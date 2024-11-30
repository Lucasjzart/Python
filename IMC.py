def calcular_imc():
    try:
        # Entrada de dados
        peso = float(input("Digite seu peso em kg: "))
        altura = float(input("Digite sua altura em metros: "))
        
        # Calcula o IMC
        imc = peso / (altura ** 2)
        
        # Exibe o IMC calculado
        print(f"Seu IMC é: {imc:.2f}")
        
        # Avaliação do IMC
        if 18.5 <= imc <= 24.9:
            print("Parabéns! Você está no IMC ideal.")
        elif imc < 18.5:
            print("Você está abaixo do peso.")
        else:
            print("Você está acima do peso.")
    except ValueError:
        print("Por favor, insira valores numéricos válidos.")

# Executa a função
calcular_imc()
