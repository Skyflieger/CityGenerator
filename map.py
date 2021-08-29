from PIL import Image, ImageTk
from PyQt5 import QtGui
import numpy as np
import random
import progressbar

class map:
    def generate():
        image = Image.open('map.png')
        image = image.convert('RGB')

        processed = Image.new('RGB', (image.width, image.height), color=0)
        pixels = processed.load()

        noise = np.random.normal(0,5,100)

        widgets = [
            'Scanning Map',
            progressbar.Bar(marker=progressbar.AnimatedMarker(
                fill='█',
            )),
            progressbar.Percentage(),
        ]

        bar = progressbar.ProgressBar(
                widgets=widgets,
                max_value=image.width,
            ).start()

        for x in range(image.width):
            for y in range(image.height):
                r, g, b = image.getpixel((x,y))
                if(r == 255 and g == 114 and b == 0): #Land
                    pixels[x,y] = (255 + round(noise[random.randint(0, 99)]), 114 + round(noise[random.randint(0, 99)]), 00  + round(noise[random.randint(0, 99)]))
                elif(r == 255 and g == 16 and b == 0): #MainStreet
                    pixels[x,y] = (255 + round(noise[random.randint(0, 99)]), 16 + round(noise[random.randint(0, 99)]), 0  + round(noise[random.randint(0, 99)]))
                elif(r == 132 and g == 0 and b == 0): #water
                    pixels[x,y] = (132 + round(noise[random.randint(0, 99)]), 0 + round(noise[random.randint(0, 99)]), 0  + round(noise[random.randint(0, 99)]))
                elif(r == 0 and g == 0 and b == 0): #water
                    pixels[x,y] = (0 + round(noise[random.randint(0, 99)]), 0 + round(noise[random.randint(0, 99)]), 0  + round(noise[random.randint(0, 99)]))        
            bar.update(x + 1)

        bar.finish()
        data = processed.tobytes("raw","RGB")
        out = QtGui.QImage(data, processed.size[0], processed.size[1], QtGui.QImage.Format_RGB888)
        return out