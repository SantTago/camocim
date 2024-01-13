from youtubesearchpython import VideosSearch

def obter_links_incorporacao_ultimas_noticias(query, max_resultados, arquivo_saida):
    videos_search = VideosSearch(query, limit=max_resultados)
    results = videos_search.result()

    # Extrai os links de incorporação dos vídeos
    links_incorporacao = [f"'https://www.youtube.com/embed/{video['id']}'," for video in results['result']]

    # Salva os links em um arquivo TXT
    with open(arquivo_saida, 'w') as arquivo:
        for link in links_incorporacao:
            arquivo.write(link + '\n')

    print(f'Links de incorporação das últimas notícias do YouTube foram salvos em {arquivo_saida}')

# Substitua 'QUERY' pela consulta de pesquisa que corresponde aos vídeos desejados
QUERY = 'últimas notícias'  # Pode ser ajustado conforme necessário
# Substitua 'MAX_RESULTADOS' pelo número máximo de vídeos que você deseja obter
MAX_RESULTADOS = 20
# Nome do arquivo de saída
ARQUIVO_SAIDA = 'links_incorporacao_noticias_youtube.txt'

obter_links_incorporacao_ultimas_noticias(QUERY, MAX_RESULTADOS, ARQUIVO_SAIDA)
