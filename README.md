# 🎵 Baixador e Conversor de Vídeos do YouTube

Este projeto contém três scripts Python com finalidades distintas, todos voltados para download de conteúdo do YouTube. Você poderá:

- 📥 Baixar vídeos de uma playlist inteira (`playlist.py`)
- 🎧 Baixar um vídeo individual e convertê-lo automaticamente para MP3 de forma moderna e confiável (`pmp3_new.py`)
- 🧪 Baixar e converter manualmente um vídeo usando Pytube e MoviePy (`PyMP3_old.py`)


### PS: Certifique-se de baixar o requirements.txt e gerar seu ambiente virtual

---

## 📁 `playlist.py` – Baixar uma Playlist do YouTube

Este script utiliza a biblioteca **Pytube** para baixar todos os vídeos de uma playlist do YouTube.

### 🚀 Como Funciona:

1. Solicita a URL da playlist do usuário.
2. Cria uma instância `Playlist` usando a biblioteca `pytube`.  
3. Mostra o número total de vídeos encontrados.  
4. Percorre cada vídeo e baixa na resolução mais alta disponível.  
5. Salva os vídeos em uma pasta com o nome definido pelo usuário.  
6. Exibe mensagens de progresso e erro.

### 📌 Observação Importante:  
> ⚠️ A biblioteca **Pytube** pode **quebrar** com frequência devido a alterações no YouTube. Ela depende da estrutura da página HTML do site, que pode mudar sem aviso. Sempre verifique a compatibilidade da versão instalada com a do YouTube.

### ✅ Pré-requisitos:

```bash
pip install pytube
```

ou

```bash
pip3 install pytube
```

## pmp3_new.py – Conversor Moderno de Vídeo para MP3 (recomendado)

Este script utiliza a poderosa biblioteca yt-dlp com ffmpeg embutido para baixar somente o áudio de um vídeo e convertê-lo automaticamente para o formato MP3 com alta qualidade (192kbps).

🚀 Como Funciona:

    1. Solicita o link do vídeo do YouTube.

    2. Pergunta o caminho onde o arquivo será salvo.

    3. Usa yt-dlp para baixar apenas o melhor áudio disponível.

    4. Converte automaticamente para .mp3 usando FFmpeg.

    5. Salva com o nome do vídeo original.

### ✅ Vantagens:

    . Compatível com versões atuais do YouTube.

    . Mais robusto que o Pytube.

    . Conversão direta, rápida e eficiente.

    . Sem necessidade de apagar o vídeo manualmente — o .mp3 já é o resultado final.

### ✅ Pré-requisitos:

```bash
pip install yt-dlp
```

ou

```bash
pip3 install yt-dlp
```

#### PS:  Requer o FFmpeg instalado no sistema. No Linux, use: sudo apt install ffmpeg. No Windows, instale e adicione ao PATH.

## PyMP3_old.py – Conversor Manual com Pytube e MoviePy

Este script também baixa vídeos do YouTube e os converte em MP3, mas usando Pytube + MoviePy. Ele realiza a conversão ao percorrer manualmente os arquivos .mp4 baixados e gerando os equivalentes .mp3.

🚀 Como Funciona:

    1. Recebe a URL do vídeo e o caminho de destino.

    2. Usa Pytube para baixar somente o áudio.

    3. Com os, re e moviepy, localiza o arquivo .mp4, converte para .mp3 e remove o original.

❌ Desvantagens:

    . Menor robustez em comparação ao yt-dlp.

    . Processo mais trabalhoso e sujeito a falhas em arquivos com nomes diferentes ou problemas na conversão.

    . Depende de múltiplas bibliotecas.

✅ Pré-requisitos:
```bash
pip install pytube
pip install moviepy
```

ou

```bash
pip3 install pytube
pip3 install moviepy
```

#### ⚠️ Assim como no playlist.py, o uso de Pytube pode não funcionar corretamente em versões recentes do YouTube.

## ⚠️ Aviso Legal

Este projeto é fornecido somente para fins educacionais.
O download ou conversão de vídeos protegidos por `direitos autorais` pode `violar os Termos de Serviço do YouTube` e legislações locais.

Você é responsável pelo uso adequado deste código.

### 📚 Referências

- [Pytube no PyPI](https://pypi.org/project/pytube/)
- [yt-dlp no GitHub](https://github.com/yt-dlp/yt-dlp)
- [MoviePy](https://zulko.github.io/moviepy/)
- [FFmpeg](https://ffmpeg.org/)
