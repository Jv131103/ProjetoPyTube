# Baixador de Playlist do YouTube

Este código Python utiliza a biblioteca Pytube para baixar vídeos de uma playlist do YouTube. Ele solicitará a URL da playlist e um nome para a pasta de destino onde os vídeos serão salvos.

## Funcionamento

O código funciona da seguinte maneira:

1. Solicita a URL da playlist do usuário.

2. Cria uma instância de `Playlist` do Pytube com a URL da playlist.

3. Obtém o número total de vídeos na playlist.

4. Itera sobre os vídeos na playlist e baixa cada um deles em alta resolução.

5. Salva os vídeos na pasta de destino especificada pelo usuário.

6. Exibe mensagens de status durante o processo.

7. Informa quando o download da playlist é concluído.

## Uso

Para usar o código, siga estas etapas:

1. Execute o código Python.

2. Digite a URL da playlist do YouTube quando solicitado.

3. Especifique um nome para a pasta onde os vídeos serão salvos.

4. Aguarde até que o download da playlist seja concluído.

Lembre-se de que a biblioteca Pytube pode não funcionar corretamente em todos os casos, devido a alterações no site do YouTube. Certifique-se de usar o código de acordo com as políticas e termos de serviço do YouTube.

## Pré-requisitos

Certifique-se de ter a biblioteca Pytube instalada em seu ambiente Python. Você pode instalá-la usando o seguinte comando:

```Terminal Windows / Linux
pip install pytube
```
ou
```Terminal Windows / Linux
pip3 install pytube
```

# Conversor de Vídeo para MP3

Este código Python usa a biblioteca Pytube para baixar um vídeo do YouTube, converter o vídeo baixado em um arquivo MP3 e salvá-lo no caminho especificado pelo usuário.

## Funcionamento

O código funciona da seguinte maneira:

1. Solicita ao usuário que insira o link do vídeo do YouTube.

2. Solicita ao usuário que especifique o caminho onde o vídeo será salvo.

3. Baixa o vídeo do YouTube no caminho especificado.

4. Converte o vídeo para um arquivo MP3.

5. Salva o arquivo MP3 no mesmo diretório onde o vídeo foi baixado.

6. Remove o arquivo de vídeo original (opcional).

7. Exibe uma mensagem indicando que o download e a conversão foram concluídos com sucesso.

## Uso

Para usar o código, siga estas etapas:

1. Execute o código Python.

2. Insira o link do vídeo do YouTube quando solicitado.

3. Especifique o caminho onde o vídeo será salvo.

4. Aguarde até que o download e a conversão sejam concluídos.

Lembre-se de que a qualidade do áudio no arquivo MP3 dependerá da qualidade do vídeo original.

## Pré-requisitos

Certifique-se de ter as bibliotecas Pytube, moviepy e re instaladas em seu ambiente Python. Você pode instalá-las usando os seguintes comandos:

``` Terminal Windows / Linux
pip install pytube
pip install moviepy
```
ou
``` Terminal Windows / Linux
pip3 install pytube
pip3 install moviepy
```


## Aviso

Este código é fornecido apenas para fins educacionais e de aprendizado. O download e a conversão de conteúdo protegido por direitos autorais podem violar os termos de serviço do YouTube e as leis de direitos autorais. Respeite todas as leis e regulamentações ao usar este código.

---

*Nota: Este código é fornecido como está, e o funcionamento da biblioteca Pytube pode mudar ao longo do tempo devido a atualizações no YouTube. Verifique a documentação da biblioteca Pytube para obter informações atualizadas sobre seu uso.*

