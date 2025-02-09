import pandas as pd
import numpy as np
from datetime import datetime, timedelta

def gerar_dados_ficticios(num_itens=100):
    """Gera dados fictícios para o controle de estoque."""
    categorias = ["Shampoo", "Condicionador", "Máscara", "Finalizador", "Óleo Capilar", "Creme para Pentear", "Leave-in"]
    np.random.seed(42)  # Para garantir consistência nos dados fictícios

    dados = {
        "Código do Produto": [f"PROD{i:03d}" for i in range(1, num_itens + 1)],
        "Nome do Produto": [f"Produto {i}" for i in range(1, num_itens + 1)],
        "Categoria": np.random.choice(categorias, num_itens),
        "Quantidade em Estoque": np.random.randint(0, 100, num_itens),
        "Estoque Mínimo": np.random.randint(10, 30, num_itens),
        "Lote": [f"LOTE{i:03d}" for i in range(1, num_itens + 1)],
        "Validade": [datetime.now() + timedelta(days=np.random.randint(30, 365)) for _ in range(num_itens)],
        "Última Entrada": [datetime.now() - timedelta(days=np.random.randint(1, 30)) for _ in range(num_itens)],
        "Última Saída": [datetime.now() - timedelta(days=np.random.randint(1, 30)) for _ in range(num_itens)],
    }
    return pd.DataFrame(dados)

def aplicar_formatacao_condicional(worksheet, num_linhas, formato_vermelho):
    """Aplica formatação condicional para destacar estoque abaixo do mínimo."""
    worksheet.conditional_format(1, 3, num_linhas, 3, {
        "type": "formula",
        "criteria": "=D2<E2",  # Compara "Quantidade em Estoque" com "Estoque Mínimo"
        "format": formato_vermelho
    })

def configurar_autofiltro(worksheet, num_linhas, num_colunas):
    """Configura o autofiltro na planilha."""
    worksheet.autofilter(0, 0, num_linhas, num_colunas - 1)

def ajustar_largura_colunas(worksheet, colunas):
    """Ajusta a largura das colunas com base no tamanho do cabeçalho."""
    for i, coluna in enumerate(colunas):
        worksheet.set_column(i, i, len(coluna) + 5)

def criar_planilha_estoque(caminho_arquivo, dados):
    """Cria a planilha de controle de estoque com formatações."""
    with pd.ExcelWriter(caminho_arquivo, engine="xlsxwriter") as writer:
        dados.to_excel(writer, sheet_name="Estoque", index=False)
        workbook = writer.book
        worksheet = writer.sheets["Estoque"]

        # Formatação condicional
        formato_vermelho = workbook.add_format({"bg_color": "#FF9999"})
        aplicar_formatacao_condicional(worksheet, dados.shape[0], formato_vermelho)

        # Autofiltro
        configurar_autofiltro(worksheet, dados.shape[0], dados.shape[1])

        # Ajustar largura das colunas
        ajustar_largura_colunas(worksheet, dados.columns)

def main():
    """Função principal para executar o programa."""
    caminho_arquivo = "controle_estoque_cosmeticos.xlsx"
    dados = gerar_dados_ficticios(num_itens=100)
    criar_planilha_estoque(caminho_arquivo, dados)
    print(f"Planilha de controle de estoque criada com sucesso: {caminho_arquivo}")

if __name__ == "__main__":
    main()