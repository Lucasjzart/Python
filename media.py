def receber_nota():
    while True:
        try:
            nota = float(input("Digite uma nota (0 a 10): "))
            if 0 <= nota <= 10:
                return nota
            else:
                print("Nota inválida! A nota deve ser entre 0 e 10.")
        except ValueError:
            print("Entrada inválida! Por favor, digite um número.")

def main():
    print("Digite as três notas do aluno:")
    
    nota1 = receber_nota()
    nota2 = receber_nota()
    nota3 = receber_nota()
    
    # Calcula a média
    media = (nota1 + nota2 + nota3) / 3
    
    # Verifica se o aluno foi aprovado ou reprovado
    if media >= 6.0:
        print(f"Aprovado! Sua média foi: {media:.2f}")
    else:
        print(f"Reprovado! Sua média foi: {media:.2f}")
    
if __name__ == "__main__":
    main()
