import os
import zipfile
import pdfplumber 
import pandas as pd
 

pdf_path = "anexo1.pdf"
csv_path = "anexo1.csv"
zip_path = "Teste_Kaiky.zip"

SUBSTITUICOES = {
    "OD": "Segurança Odontológica",
    "AMB": "Segurança Ambulatorial",
}

def extrair_tabela(pdf_path):
    tabelas = []

    with pdfplumber.open(pdf_path) as pdf: # Abre o arquivo PDF
        for page in pdf.pages:
            tabelas_extraidas = page.extract_tables() # Extrai as tabelas da página
            for tabela in tabelas_extraidas:
                tabelas.append(pd.DataFrame(tabela)) # Converte a tabela extraída para um DataFrame

    if not tabelas:
        raise ValueError("Nenhuma tabela encontrada")
    
    # Concatena todas as tabelas extraídas em um único DataFrame
    df_final = pd.concat(tabelas, ignore_index=True)

     # Renomeia colunas (supondo que a primeira linha contenha os nomes corretos)
     # Pega a primeira linha e a transforma em cabeçalho
     
    df_final.columns = df_final.iloc[0]
    df_final = df_final[1:].reset_index(drop=True)

    # Substitui abreviações OD e AMB
    df_final.replace(SUBSTITUICOES, inplace=True)

    return df_final

def salvar_csv(df, csv_path):
    """Salva o DataFrame em um arquivo CSV"""
    df.to_csv(csv_path, index=False, encoding="utf-8")

def compactar_arquivo(csv_path, zip_path):
    """Compacta o CSV em um arquivo ZIP"""
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        zipf.write(csv_path, os.path.basename(csv_path))

# Execução das funções
df = extrair_tabela(pdf_path)
salvar_csv(df, csv_path)
compactar_arquivo(csv_path, zip_path)

print(f"Processo concluído. Arquivo compactado: {zip_path}")

