
# Projeto - OCR para Extração de Texto de PDF

## Sobre o Projeto

Esse projeto tem como objetivo fazer a leitura de arquivos PDF que estão em formato de imagem, ou seja, não dá pra copiar o texto direto.

Aqui eu usei um processo chamado OCR (Reconhecimento Óptico de Caracteres), que basicamente lê o que está na imagem e transforma em texto. Depois que ele pega o texto, o código ainda faz uma correção ortográfica pra tentar arrumar possíveis erros.

Tudo isso foi feito utilizando a linguagem Python e algumas bibliotecas bem conhecidas.

## Tecnologias Utilizadas

- Python
- pytesseract (OCR)
- OpenCV (Manipulação de imagem)
- PyMuPDF (Leitura de PDF)
- pyspellchecker (Correção ortográfica)

## Estrutura do Projeto

```
Reconhecimento_OCR_de_PDF/
|
├── main.py                      # Código principal
├── download.pdf                 # Arquivo PDF que vai ser analisado
├── texto_extraido_corrigido.txt # Arquivo gerado com o texto final
├── requirements.txt             # Bibliotecas necessárias
└── README.md                    # Documentação do projeto
```

## Como Executar o Projeto

1. Clonar o repositório:

```
git clone [https://github.com/GustPS/Reconhecimento_OCR_de_PDF.git]
```

2. Criar o ambiente virtual:

```
python -m venv .venv
```

3. Ativar o ambiente virtual:

Windows:

```
.venv\Scripts\activate
```

4. Instalar as dependências:

```
pip install -r requirements.txt
```

5. Colocar seu arquivo PDF dentro da pasta do projeto com o nome:

```
download.pdf
```

6. Executar o projeto:

```
python main.py
```

7. O resultado vai ser salvo em:

```
texto_extraido_corrigido.txt
```

## Considerações Finais

Esse projeto foi desenvolvido com fins de criar o projeto de um trabalho exigido pelo Ariel. 

Provavelmente tem muitas melhorias que podem ser feitas, mas pra o objetivo do trabalho e da entrega ficou bem funcional.
