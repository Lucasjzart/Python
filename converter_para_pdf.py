from fpdf import FPDF
from PIL import Image
import os
from tkinter import Tk, filedialog

def selecionar_imagem():
    """Abre uma janela para selecionar uma imagem manualmente."""
    root = Tk()
    root.withdraw()  # Esconde a janela principal do tkinter
    caminho_imagem = filedialog.askopenfilename(
        title="Selecione uma imagem",
        filetypes=[("Imagens", "*.jpg;*.jpeg;*.png;*.bmp;*.gif")]
    )
    return caminho_imagem

def image_to_pdf(image_path, pdf_path):
    try:
        # Verifica se o caminho da imagem existe
        if not os.path.exists(image_path):
            print(f"Erro: O arquivo '{image_path}' não foi encontrado.")
            return

        # Verifica se o caminho é um arquivo
        if not os.path.isfile(image_path):
            print(f"Erro: '{image_path}' não é um arquivo válido.")
            return

        # Abrir a imagem usando Pillow
        image = Image.open(image_path)
        
        # Criar um objeto PDF
        pdf = FPDF(unit="pt", format=[image.width, image.height])
        pdf.add_page()
        
        # Inserir a imagem no PDF
        pdf.image(image_path, 0, 0, image.width, image.height)
        
        # Salvar o PDF
        pdf.output(pdf_path, "F")
        print(f"PDF salvo em {pdf_path}")

    except PermissionError:
        print(f"Erro: Permissão negada para acessar o arquivo ou diretório '{image_path}'.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

def main():
    """Função principal do programa."""
    # Selecionar a imagem manualmente
    print("Selecione a imagem que deseja converter para PDF.")
    image_path = selecionar_imagem()
    if not image_path:
        print("Nenhuma imagem selecionada. Operação cancelada.")
        return

    # Solicitar o nome do arquivo PDF de saída
    pdf_path = input("Digite o nome do arquivo PDF de saída (com extensão .pdf): ").strip('"')

    # Converter a imagem em PDF
    image_to_pdf(image_path, pdf_path)

if __name__ == "__main__":
    main()