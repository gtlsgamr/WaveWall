import graph
from graph import wavewall
import youtube_dl

if __name__=='__main__':
    url = input()
    ydl_opts = {
    'format': '140/mp3/bestaudio',       
    'outtmpl': 't.mp3',               
    }
    ydl = youtube_dl.YoutubeDL(ydl_opts)
    ydl.download([url])
    wavewall1 = wavewall(url)
    fimg = wavewall1.graph('t.mp3', (255,255,255))
    wavewall1.finalimage(fimg)