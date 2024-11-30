def calcular_imc():
    try:
        print("=== Cálculo do IMC ===")
        print("O IMC é calculado como: peso (kg) / altura² (m²)\n")
        
        # Entrada de dados
        peso = float(input("Digite seu peso em kg: "))
        altura = float(input("Digite sua altura em metros: "))
        
        # Calcula o IMC
        imc = peso / (altura ** 2)
        
        # Exibe o IMC calculado
        print(f"\nSeu IMC é: {imc:.2f}")
        
        # Avaliação do IMC com classificações mais detalhadas
        if imc < 18.5:
            print("Você está abaixo do peso.")
        elif 18.5 <= imc <= 24.9:
            print("Parabéns! Você está no IMC ideal.")
        elif 25 <= imc <= 29.9:
            print("Você está com sobrepeso.")
        elif 30 <= imc <= 34.9:
            print("Você está com obesidade grau 1.")
        elif 35 <= imc <= 39.9:
            print("Você está com obesidade grau 2.")
        else:
            print("Você está com obesidade grau 3 (mórbida).")
    
    except ValueError:
        print("\nPor favor, insira valores numéricos válidos.")

# Execução com opção de repetição
while True:
    calcular_imc()
    repetir = input("\nDeseja calcular novamente? (s/n): ").strip().lower()
    if repetir != 's':
        print("Programa encerrado. Até mais!")
        break
