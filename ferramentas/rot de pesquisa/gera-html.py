import os

def gerar_html_conteudo(titulo, conteudo, imagem_url, data):
    # Substitua os espaços e caracteres especiais no título para criar um identificador único
    identificador = titulo.lower().replace(' ', '_')

    # Monta o HTML para a notícia
    html = f"""
    <article id="{identificador}">
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
    """
    return html

def ler_arquivos_noticias(pasta):
    noticias = []
    for arquivo in os.listdir(pasta):
        if arquivo.endswith(".txt"):
            path_arquivo = os.path.join(pasta, arquivo)
            with open(path_arquivo, 'r', encoding='utf-8') as f:
                conteudo = f.read().strip()
                noticias.append({'titulo': os.path.splitext(arquivo)[0], 'conteudo': conteudo})

    return noticias

def main():
    pasta_noticias = os.path.join(os.path.expanduser("~/Desktop"), "Noticias_G1")
    pasta_html = os.path.join(pasta_noticias, "html")
    
    # Cria a pasta "html" se ela não existir
    os.makedirs(pasta_html, exist_ok=True)

    # Substitua pela data desejada
    data = '10:40   31/12/2023'

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
                    html = gerar_html_conteudo(titulo, conteudo, imagem_url, data)

                    # Salva o HTML em um arquivo na pasta "html"
                    with open(os.path.join(pasta_html, f"{subpasta}.html"), 'w', encoding='utf-8') as html_file:
                        html_file.write(html)

if __name__ == "__main__":
    main()
