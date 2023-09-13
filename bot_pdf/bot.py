
"""
FUNÇÃO DE LER DOCUMENTOS NO BOTSTUDIO DISPONIVEL APENAS NOS PRIMEIROS 30 DIAS
NA VERSÃO COMUNIDADE OU NA VERSÃO PAGA ATÉ O MOMENTO ATUAL 09/2023

"""

# from botcity.document_processing import *
import pathlib

def lerPDF():
    #reader = PDFReader()
    #parser = reader.read_file(r'./docs/Contoso_INVOICE_TailSpin.pdf')

    # a variavel armazena uma lista de arquivos que é lida a partir de uma pasta seguindo a regra passada na função abaixo
    arquivos = pathlib.Path(
        r'C:\Users\ash\VscodeProjects\learning-botcity\bot_pdf\docs'
        ).glob('*.pdf')
    
    # loop percorre todos iteraveis da variavel arquivos pegando uma a um para printar o caminho do arquivo
    for arquivo in arquivos:
        print(arquivo)

lerPDF()