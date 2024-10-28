import yt_dlp
import argparse
import os

def baixar_video_ou_playlist(url):
    try:
        # Primeiro, extrai informações sem baixar
        ydl_opts_info = {'extract_flat': True, 'quiet': True}
        with yt_dlp.YoutubeDL(ydl_opts_info) as ydl_info:
            info_dict = ydl_info.extract_info(url, download=False)
            canal_nome = info_dict.get('uploader', 'Canal_Desconhecido')
        
        # Cria o diretório com o nome do canal
        if not os.path.exists(canal_nome):
            os.makedirs(canal_nome)
        
        # Define opções para baixar com o diretório do canal
        ydl_opts = {
            'format': 'best',
            'outtmpl': f'{canal_nome}/%(playlist_title)s/%(playlist_index)s - %(title)s.%(ext)s' if 'entries' in info_dict else f'{canal_nome}/%(title)s.%(ext)s',
            'noplaylist': False
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            # Verifica se é uma playlist
            if 'entries' in info_dict:
                print(f"Baixando playlist: {info_dict['title']} com {len(info_dict['entries'])} vídeos")
                # Baixa a playlist inteira
                ydl.download([url])
            else:
                print(f"Baixando vídeo: {info_dict['title']}")
                ydl.download([url])

    except Exception as e:
        print(f"Ocorreu um erro: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Download de vídeos do YouTube usando yt-dlp")
    parser.add_argument("url", help="URL do vídeo ou playlist do YouTube para download")
    args = parser.parse_args()

    baixar_video_ou_playlist(args.url)
