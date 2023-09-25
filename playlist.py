from pytube import YouTube, Playlist

playlist_url = input("Digite a URL da playlist aqui: ")
nome_play = input("Qual o nome da sua playlist: ")

try:
    playlist = Playlist(playlist_url)
    print(f"Total de vídeos na playlist: {len(playlist)}")
    
    for url in playlist:
        print(f"Baixando o vídeo: {url}...")
        try:
            video = YouTube(url)
            stream = video.streams.get_highest_resolution()
            stream.download(output_path=nome_play)
            print(f"Vídeo {url} baixado com sucesso!")
        except Exception as e:
            print(f"Erro ao baixar o vídeo {url}: {str(e)}")
    
    print("Download da playlist concluído!")
    
except Exception as e:
    print(f"Ocorreu um erro ao processar a playlist: {str(e)}")
