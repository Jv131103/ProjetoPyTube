import yt_dlp

url = input("Digite o Link do Vídeo: ")
path = input("Caminho de download: ")

ydl_opts = {
    'format': 'bestaudio/best',
    'outtmpl': f'{path}/%(title)s.%(ext)s',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])

print("Download concluído!")
