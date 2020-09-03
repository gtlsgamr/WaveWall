from pydub import AudioSegment
from matplotlib import pyplot as plot
from PIL import Image, ImageDraw
import numpy as np
import os


class wavewall:
    def __init__(self,url):
        self.url = url

    def bg(self):
        pass

    def graph(self,src,clr):
        src = src

        audio = AudioSegment.from_file(src)
        data = np.fromstring(audio._data, np.int16)
        fs = audio.frame_rate
        COLOR = clr

        BARS = 500
        BAR_HEIGHT = 1000
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

        im.save('abc.png')


    def name(self):
        pass

    def finalimage(self):
        pass
