from PIL import Image
from PyQt5 import QtGui

class roads:
    def generate():
        road = Image.new('RGB', (1024, 1024), color=0)
        pixels = road.load()

        for x in range(road.width):
            for y in range(road.height):
                pixels[x,y] = (x, 0, 0) 

        data = road.tobytes("raw","RGB")
        road = QtGui.QImage(data, road.size[0], road.size[1], QtGui.QImage.Format_RGB888)
        return road