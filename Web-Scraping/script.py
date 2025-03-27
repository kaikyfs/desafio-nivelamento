import requests
from bs4 import BeautifulSoup
import os
import zipfile

url_pagina = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos"
download_folder = "arquivos-baixados"
arquivo_zip = 'arquivos.zip'


def obter_links_pdfs(url):
    # Verificamos o sucesso da requisição
    response = requests.get(url)
    if response.status_code != 200:
        print("Erro ao acessar a página.")
        exit()

    # Pegando o conteúdo da página
    soup = BeautifulSoup(response.text, "html.parser")
    links_pdfs = []

    # Procurando todos os links <a> que contenham "Anexo" no nome
    for link in soup.find_all("a", href=True):
        href = link["href"]
        if "anexo" in href.lower() and href.endswith(".pdf"):  # Filtro para links de PDFs
            if href.startswith("/"):  # Corrige links relativos
                href = "https://www.gov.br" + href
            links_pdfs.append(href)
    if not links_pdfs:
        print("Nenhum PDF encontrado na página.")
        exit()    

    return links_pdfs

def baixar_pdfs(links_pdfs):
    if not os.path.exists(download_folder):
        os.makedirs(download_folder)

    arquivos_baixados = []

    for link in links_pdfs:
        nome_arquivo = link.split("/")[-1] # Pega o nome do arquivo
        caminho_arquivo = os.path.join(download_folder, nome_arquivo)

        # Baixando o arquivo
        response = requests.get(link)
        if response.status_code == 200:
            with open(caminho_arquivo, "wb") as f: 
                f.write(response.content)
            print(f"Arquivo {nome_arquivo} baixado com sucesso.")
            arquivos_baixados.append(caminho_arquivo)
        else:
            print(f"Erro ao baixar o arquivo {nome_arquivo}.")

    return arquivos_baixados


def compactar_arquivos(arquivos_baixados):
    # Compactando arquivos em um arquivo ZIP
    with zipfile.ZipFile(arquivo_zip, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for arquivo in arquivos_baixados:
            zipf.write(arquivo, os.path.basename(arquivo))
    print(f'Arquivos compactados em {arquivo_zip}')


# Execução do script (em try catch para tratamento de erros)
try:
    print("Obtendo links dos PDFs...")
    links_pdfs = obter_links_pdfs(url_pagina)
    
    print("Baixando PDFs...")
    arquivos_baixados = baixar_pdfs(links_pdfs)
    
    print("Compactando PDFs...")
    compactar_arquivos(arquivos_baixados)
    
    print(f"Processo concluído! Arquivo ZIP criado: {arquivo_zip}")
except Exception as e:
    print(f"Erro: {e}")
