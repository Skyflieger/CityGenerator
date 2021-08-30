from PIL import Image
from PyQt5 import QtGui
from random import randrange
import numpy as np

class roads:
    road = Image.new('RGB', (1024, 1024), color=0)
    pixels = road.load()

    def generate(self):
        rany = self.numberlist(1, self.road.width - 2, 50, 100)
        ranx = self.numberlist(1, self.road.height - 2, 50, 100)
        for x in range(self.road.width):
            for y in range(self.road.height):
                if(y in rany):
                    self.pixels[x,y] = (255 ,255 ,255)
                elif(x in ranx):
                    rany = self.numberlist(1, self.road.width - 2, 50, 100)
                    self.pixels[x,y] = (255 ,255 ,255) 
                else:
                    self.pixels[x,y] = (0 ,0 ,0) 
                

        data = self.road.tobytes("raw","RGB")
        road = QtGui.QImage(data, self.road.size[0], self.road.size[1], QtGui.QImage.Format_RGB888)
        return road

    def numberlist(min, max, mindistance, maxdistance):
        ran = [min, max]
        start = min
        while(start + mindistance < max):
            if(start + maxdistance > max):
                ran.append((max - start) / 2 + start)
                break
            else:
                start = randrange(start + mindistance, start + maxdistance)
                ran.append(start)

        ran.sort()
        return ran