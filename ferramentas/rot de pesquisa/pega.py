import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def obter_noticias_g1():
    url = 'https://g1.globo.com/'

    # Faz a requisição HTTP para a página do G1
    response = requests.get(url)

    if response.status_code != 200:
        print(f"Erro ao acessar o site. Código de status: {response.status_code}")
        return None

    # Parseia o HTML da página
    soup = BeautifulSoup(response.text, 'html.parser')

    # Encontra as manchetes no HTML
    manchetes = soup.find_all('a', class_='feed-post-link')

    noticias = []

    # Itera sobre as manchetes e extrai informações
    for i, manchete in enumerate(manchetes):
        titulo = manchete.text.strip()
    
        # Verifica se a tag 'a' possui o atributo 'href'
        if 'href' in manchete.attrs:
            link = manchete['href']
        else:
            # Se não tiver, pule para a próxima manchete
            print(f"Manchete {i + 1} não possui atributo 'href'. Pulando para a próxima.")
            continue

        # Faz uma nova requisição para obter o conteúdo completo da notícia
        noticia_response = requests.get(link)
        noticia_soup = BeautifulSoup(noticia_response.text, 'html.parser')

        # Extrai o conteúdo da notícia
        paragrafos = noticia_soup.find_all('p')
        conteudo = '\n'.join([p.text for p in paragrafos])

        # Tenta obter o link da imagem
        try:
            imagem_url = noticia_soup.find('meta', {'property': 'og:image'})['content']
        except (TypeError, KeyError):
            imagem_url = None

        noticias.append({'titulo': titulo, 'conteudo': conteudo, 'imagem_url': imagem_url})

    return noticias

def salvar_noticias(noticias):
    diretorio_destino = os.path.join(os.path.expanduser("~/Desktop"), "Noticias_G1")
    os.makedirs(diretorio_destino, exist_ok=True)

    for i, noticia in enumerate(noticias):
        pasta = os.path.join(diretorio_destino, f'noticia_{i + 1}')
        os.makedirs(pasta, exist_ok=True)

        if noticia['titulo']:
            with open(os.path.join(pasta, 'titulo.txt'), 'w', encoding='utf-8') as f:
                f.write(noticia['titulo'])

        if noticia['conteudo']:
            with open(os.path.join(pasta, 'conteudo.txt'), 'w', encoding='utf-8') as f:
                f.write(noticia['conteudo'])

        if noticia['imagem_url']:
            with open(os.path.join(pasta, 'imagem_link.txt'), 'w', encoding='utf-8') as f:
                f.write(noticia['imagem_url'])

if __name__ == "__main__":
    # Obtém automaticamente 10 notícias
    noticias = obter_noticias_g1()[:10]

    if noticias:
        salvar_noticias(noticias)
        print("Notícias salvas com sucesso na área de trabalho, dentro da pasta 'Noticias_G1'.")
        
        
def gerar_html_conteudo(titulo, conteudo, imagem_url, data):
    # Substitua os espaços e caracteres especiais no título para criar um identificador único
    identificador = titulo.lower().replace(' ', '_')

    # Monta o HTML para a notícia
    html = f"""
    <section class="bloco-noticias">
        <article>
            <img src="{imagem_url}" alt="{titulo}">
            <div class="content">
                <h2>{titulo}</h2>
                <p class="description ellipsis"></p>
                <p class="full-text" style="display: none;">
                    {conteudo}
                </p>
                <p class="read-more" onclick="toggleContent(this)">Mostrar Mais</p>
            </div>
            <p class="paragrafo">
                {data}
            </p>
        </article>
    <section>
   <!------------------------------------------------------>
    """
    return html

def main():
    pasta_noticias = os.path.join(os.path.expanduser("~/Desktop"), "Noticias_G1")
    pasta_html = os.path.join(pasta_noticias, "html")

    # Cria a pasta "html" se ela não existir
    os.makedirs(pasta_html, exist_ok=True)

    # Substitua pela data desejada
    data = '10:40   31/12/2023'

    # Inicia o arquivo HTML com a estrutura inicial
    html_total = """<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Notícias G1</title>
    <style>
        .article {
            margin-bottom: 20px;
        }
        hr {
            border: 0.5px solid #ccc;
        }
    </style>
</head>
<body>
"""

    for subpasta in os.listdir(pasta_noticias):
        subpasta_path = os.path.join(pasta_noticias, subpasta)

        # Verifica se é uma pasta
        if os.path.isdir(subpasta_path):
            conteudo_path = os.path.join(subpasta_path, 'conteudo.txt')
            imagem_path = os.path.join(subpasta_path, 'imagem_link.txt')
            titulo_path = os.path.join(subpasta_path, 'titulo.txt')

            # Verifica se todos os arquivos existem
            if os.path.exists(conteudo_path) and os.path.exists(imagem_path) and os.path.exists(titulo_path):
                with open(conteudo_path, 'r', encoding='utf-8') as f_conteudo, \
                        open(imagem_path, 'r', encoding='utf-8') as f_imagem, \
                        open(titulo_path, 'r', encoding='utf-8') as f_titulo:

                    conteudo = f_conteudo.read().strip()
                    imagem_url = f_imagem.read().strip()
                    titulo = f_titulo.read().strip()

                    # Gera o código HTML para a notícia
                    html_total += gerar_html_conteudo(titulo, conteudo, imagem_url, data)

    # Finaliza o arquivo HTML
    html_total += """
</body>
</html>
"""

    # Salva o HTML em um único arquivo na pasta "html"
    with open(os.path.join(pasta_html, "noticias_g1.html"), 'w', encoding='utf-8') as html_file:
        html_file.write(html_total)

if __name__ == "__main__":
    main()
