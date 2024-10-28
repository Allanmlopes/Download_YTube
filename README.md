<h2>YouTube Video & Playlist Downloader</h2>

Este projeto é um script em Python para baixar vídeos individuais ou playlists inteiras do YouTube, organizando os arquivos automaticamente em pastas com base no nome do canal e, quando aplicável, no nome da playlist.
Funcionalidades

  Download de Vídeos: Dado o link de um vídeo do YouTube, o script baixa o vídeo na melhor qualidade disponível.
  Download de Playlists: Dado o link de uma playlist do YouTube, o script baixa todos os vídeos da playlist, mantendo a ordem correta.
  Organização por Canal: Cria uma pasta com o nome do canal para cada vídeo ou playlist, garantindo uma estrutura organizada.
  Organização por Playlist: Dentro da pasta do canal, se o link fornecido for de uma playlist, o script cria uma subpasta com o nome da playlist, onde todos os vídeos dessa playlist são armazenados.

<h2>Como Funciona</h2>

O script utiliza a biblioteca yt-dlp para realizar o download dos vídeos. Ele é capaz de extrair metadados de vídeos e playlists para organizar os arquivos localmente de forma estruturada.
Estrutura do Projeto

Quando executado, o script organiza os vídeos da seguinte forma:



    /Nome_do_Canal/
    /Nome_da_Playlist/  # Se for uma playlist
        01 - Nome_do_Vídeo.mp4
        02 - Nome_do_Vídeo.mp4
    Nome_do_Vídeo_Sem_Playlist.mp4  # Se for um vídeo avulso

<h2>Pré-requisitos</h2>

  Python 3.x
  Biblioteca yt-dlp instalada (pode ser instalada via pip)

<h2>Instalando yt-dlp</h2>

    pip install yt-dlp

<h3>Como Usar</h3>

Clone este repositório para sua máquina local:

    git clone https://github.com/SEU_USUARIO/NOME_DO_REPOSITORIO.git
    cd NOME_DO_REPOSITORIO

Execute o script passando a URL do vídeo ou da playlist do YouTube:

    python main.py "https://www.youtube.com/playlist?list=PLXXXXX"

ou para um vídeo individual:

    python main.py "https://www.youtube.com/watch?v=XXXXXX"

<h2>Tecnologias Utilizadas</h2>

    Python 3: Linguagem de programação utilizada para escrever o script.
    yt-dlp: Biblioteca Python utilizada para o download e extração de metadados dos vídeos do YouTube.

Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir uma issue ou enviar um pull request.

___________________________________________________________________________________________________________________________________________________________________


Esse texto fornece uma visão clara do que o projeto faz, como ele é estruturado, como funciona e como pode ser utilizado. Você pode personalizar as partes que desejar, como o nome do repositório, ou adicionar mais detalhes conforme necessário.
