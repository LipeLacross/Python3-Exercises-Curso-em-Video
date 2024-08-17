import glob
import os

# Diretório onde estão os arquivos .txt
diretorio = './'

# Obter todos os arquivos .txt no diretório
arquivos_txt = glob.glob(os.path.join(diretorio, '*.txt'))

# Loop para converter cada arquivo .txt em .py
for arquivo_txt in arquivos_txt:
    # Nome do novo arquivo .py
    arquivo_py = arquivo_txt.replace('.txt', '.py')

    # Ler o conteúdo do arquivo .txt
    with open(arquivo_txt, 'r', encoding='utf-8') as f:
        conteudo = f.read()

    # Escrever o conteúdo no novo arquivo .py
    with open(arquivo_py, 'w', encoding='utf-8') as f:
        f.write(conteudo)

    print(f"Convertido: {arquivo_txt} -> {arquivo_py}")
