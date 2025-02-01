import random

def receber_nomes_alunos():
    alunos = []
    for i in range(4):
        nome = input(f"Digite o nome do {i+1}º aluno: ")
        alunos.append(nome)
    return alunos

def sortear_ordem_apresentacao(alunos):
    random.shuffle(alunos)
    return alunos

def exibir_ordem_apresentacao(alunos_ordenados):
    print("A ordem de apresentação dos alunos é:")
    for i, aluno in enumerate(alunos_ordenados, start=1):
        print(f"{i}º: {aluno}")

def main():
    print("Bem-vindo ao sorteio da ordem de apresentação dos alunos!")
    alunos = receber_nomes_alunos()
    alunos_ordenados = sortear_ordem_apresentacao(alunos)
    exibir_ordem_apresentacao(alunos_ordenados)

if __name__ == "__main__":
    main()