import graph
from graph import wavewall
import youtube_dl
import os

if __name__=='__main__':
    url = input()
    ydl_opts = {
    
    'format': '140/mp3/bestaudio',       
    'outtmpl': '%(title)s.mp3',               
    }
    ydl = youtube_dl.YoutubeDL(ydl_opts)
    ydl.download([url])
    wavewall1 = wavewall(url)
    width = 1920
    height = 1080
    fimg = wavewall1.graph('t.mp3', (255,255,255))
    wavewall1.finalimage(fimg,width,height, 'S A F A R N A M A / T A M A S H A')