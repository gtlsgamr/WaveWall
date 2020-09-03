from pydub import AudioSegment
from matplotlib import pyplot as plot
from PIL import Image, ImageDraw
import numpy as np
import os


class wavewall:
    def __init__(self,url):
        self.url = url

    def bg(self,url):
        pass

    def graph(self,name,color):
        src = name

        audio = AudioSegment.from_file(src)
        data = np.fromstring(audio._data, np.int16)
        fs = audio.frame_rate
        COLOR = color

        BARS = 10000
        BAR_HEIGHT = 8000
        LINE_WIDTH = 5

        length = len(data)
        RATIO = length/BARS

        count = 0
        maximum_item = 0
        max_array = []
        highest_line = 0

        for d in data:
            if count < RATIO:
                count = count + 1

                if abs(d) > maximum_item:
                    maximum_item = abs(d)
            else:
                max_array.append(maximum_item)

                if maximum_item > highest_line:
                    highest_line = maximum_item

                maximum_item = 0
                count = 1

        line_ratio = highest_line/BAR_HEIGHT

        im = Image.new('RGBA', (BARS * LINE_WIDTH, BAR_HEIGHT), (255,0,0,1))
        draw = ImageDraw.Draw(im)

        current_x = 1
        for item in max_array:
            item_height = item/line_ratio

            current_y = (BAR_HEIGHT - item_height)/2
            draw.line((current_x, current_y, current_x, current_y + item_height), fill=COLOR, width=4)

            current_x = current_x + LINE_WIDTH

        return im


    def finalimage(self,fimg):
        BGWIDTH = 1920  
        BGHEIGHT = 1080
        finalimg = Image.new('RGB', (BGWIDTH, BGHEIGHT), (265,165,0))
        forgimg = fimg
        nfwidth = BGWIDTH * 0.4
        fwidth = forgimg.size[0]
        fheight = forgimg.size[1]
        nfheight = (nfwidth * fheight) / fwidth
        forgimg = forgimg.resize((int(nfwidth),int(nfheight)), Image.ANTIALIAS)
        posx = round((BGWIDTH/2)-(nfwidth/2))
        posy = round((BGHEIGHT/2)-(nfheight/2))
        finalimg.paste(forgimg, (posx,posy), forgimg)
        finalimg.save('finalresult.jpg', quality=200)



