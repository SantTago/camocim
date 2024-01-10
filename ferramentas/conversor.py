from PIL import Image
import os

# Caminho para o diretório das imagens JPEG
diretorio_jpg = "C:\\Users\\mocob\\Desktop\\formatos"

# Caminho para o diretório de destino das imagens WebP
diretorio_webp = "C:\\Users\\mocob\\Desktop\\formatos"

# Garanta que o diretório de destino exista
if not os.path.exists(diretorio_webp):
    os.makedirs(diretorio_webp)

# Lista todos os arquivos no diretório JPEG
arquivos_jpg = [arquivo for arquivo in os.listdir(diretorio_jpg) if arquivo.lower().endswith('.jpg')]

# Itera sobre cada arquivo JPEG
for arquivo_jpg in arquivos_jpg:
    caminho_jpg = os.path.join(diretorio_jpg, arquivo_jpg)
    
    # Abre a imagem JPEG
    imagem = Image.open(caminho_jpg)
    
    # Gera o caminho para o arquivo WebP no diretório de destino
    caminho_webp = os.path.join(diretorio_webp, os.path.splitext(arquivo_jpg)[0] + '.webp')
    
    # Salva a imagem como WebP
    imagem.save(caminho_webp, 'WEBP')
    
    # Exclui o arquivo JPEG após a conversão
    os.remove(caminho_jpg)

print("Conversão e exclusão concluídas.")
