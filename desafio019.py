import random

def receber_nomes_alunos():
    alunos = []
    for i in range(4):
        nome = input(f"Digite o nome do {i+1}º aluno: ")
        alunos.append(nome)
    return alunos

def sortear_aluno(alunos):
    return random.choice(alunos)

def exibir_resultado(aluno_sorteado):
    print(f"O aluno escolhido para apagar o quadro é: {aluno_sorteado}")

def main():
    print("Bem-vindo ao sorteio de alunos para apagar o quadro!")
    alunos = receber_nomes_alunos()
    aluno_sorteado = sortear_aluno(alunos)
    exibir_resultado(aluno_sorteado)

if __name__ == "__main__":
    main()