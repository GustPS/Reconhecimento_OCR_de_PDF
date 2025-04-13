# ocr_pdf_extractor.py

# Bibliotecas utilizadas no projeto
import pytesseract
import cv2
import fitz  # PyMuPDF
from spellchecker import SpellChecker
import os
import numpy as np

# Caminho do executável do Tesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Função que extrai as imagens das páginas do PDF
def extrair_imagens_pdf(caminho_pdf):
    documento = fitz.open(caminho_pdf)
    imagens = []

    for pagina in documento:
        pix = pagina.get_pixmap()
        imagem = cv2.imdecode(
            np.frombuffer(pix.tobytes(), np.uint8),
            cv2.IMREAD_COLOR
        )
        imagens.append(imagem)

    return imagens

# Função que realiza o OCR nas imagens extraídas
def realizar_ocr(imagens):
    texto_extraido = ""
    for imagem in imagens:
        texto = pytesseract.image_to_string(
            imagem,
            lang='por',
            config='--psm 6'
        )
        texto_extraido += texto + "\n"

    return texto_extraido

# Função que corrige o texto extraído pelo OCR
def corrigir_texto(texto):
    spell = SpellChecker(language='pt')
    palavras = texto.split()
    texto_corrigido = ""

    for palavra in palavras:
        if palavra.isalpha():
            palavra_corrigida = spell.correction(palavra)
            texto_corrigido += palavra_corrigida + " "
        else:
            texto_corrigido += palavra + " "

    return texto_corrigido

# Função principal que executa o processo completo
def main():
    caminho_pdf = 'download.pdf'  # Nome do arquivo PDF que será processado

    print("Extraindo imagens do PDF...")
    imagens = extrair_imagens_pdf(caminho_pdf)

    print("Realizando OCR nas imagens...")
    texto_extraido = realizar_ocr(imagens)

    print("Corrigindo texto extraído...")
    texto_corrigido = corrigir_texto(texto_extraido)

    print("Salvando o texto em um arquivo TXT...")
    caminho_txt = os.path.join(os.getcwd(), 'texto_extraido_corrigido.txt')  # Caminho do arquivo de saída

    with open(caminho_txt, 'w', encoding='utf-8') as f:
        f.write(texto_corrigido)

    print(f"Arquivo salvo em: {caminho_txt}")
    print("Processo finalizado com sucesso!")

# Execução do programa
if __name__ == "__main__":
    main()