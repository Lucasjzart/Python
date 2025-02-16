import os
import shutil

def organizar_arquivos(pasta):
    # Verifica se a pasta existe
    if not os.path.exists(pasta):
        print(f"A pasta '{pasta}' não existe.")
        return

    # Lista todos os arquivos na pasta
    arquivos = [f for f in os.listdir(pasta) if os.path.isfile(os.path.join(pasta, f))]

    # Cria pastas para cada tipo de arquivo e move os arquivos
    for arquivo in arquivos:
        # Obtém a extensão do arquivo
        extensao = os.path.splitext(arquivo)[1][1:]  # Remove o ponto da extensão
        if not extensao:
            continue  # Ignora arquivos sem extensão

        # Cria a pasta para a extensão, se não existir
        pasta_destino = os.path.join(pasta, extensao)
        if not os.path.exists(pasta_destino):
            os.makedirs(pasta_destino)

        # Move o arquivo para a pasta correspondente
        caminho_origem = os.path.join(pasta, arquivo)
        caminho_destino = os.path.join(pasta_destino, arquivo)
        shutil.move(caminho_origem, caminho_destino)
        print(f"Movido: {arquivo} -> {pasta_destino}")

    print("Organização concluída!")

# Caminho da pasta a ser organizada
pasta_para_organizar = "C:/Users/lucas/Downloads"

# Executa a função
organizar_arquivos(pasta_para_organizar)