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
        link = manchete['href']

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
    # Solicita ao usuário o número de notícias a serem baixadas
    num_noticias = int(input("Digite o número de notícias a serem baixadas: "))

    noticias = obter_noticias_g1()[:num_noticias]

    if noticias:
        salvar_noticias(noticias)
        print("Notícias salvas com sucesso na área de trabalho, dentro da pasta 'Noticias_G1'.")
