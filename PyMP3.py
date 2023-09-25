from pytube import YouTube #Biblioteca que vai nos dar os comandos de acesso do YouTube
from pytube import Playlist #Biblioteca que vai nos permitir instalar Playlists do YouTube
import moviepy.editor as mp #Nos permite editar vídeos em Python, e está sendo apelidado de MP
import re #Biblioteca fornece funções e métodos para trabalhar com padrões de correspondência de texto.
import os #Biblioteca que nos permite utilizar as funções do sistema operacional 

link = input('Digite o Link do Vídeo: ')
path = input('Caminho de download: ')
yt = YouTube(link) #Recebe o link de vídeo do YouTube
#Fazer o dowload
ys = yt.streams.filter(only_audio=True).first().download(path)
#Converter o video(mp4) para mp3
for file in os.listdir(path):                  #For para percorrer dentro da pasta passada anteriormente
    if re.search('mp4', file):                 #If verificando se o arquivo e .MP4
        mp4_path = os.path.join(path , file)   #Cria uma variavel para armazenar o arquivo .MP4
        mp3_path = os.path.join(path, os.path.splitext(file)[0]+'.mp3') #Variavel que cria o nome do arquivo e adiciona .MP3 ao final
        new_file = mp.AudioFileClip(mp4_path)  #Cria o arquivo de áudio (.MP3)
        new_file.write_audiofile(mp3_path)     #Renomeia o arquivo, setando o nome criado anteriormente
        os.remove(mp4_path)                    #Remove o arquivo .MP4
print("Download Completo")
