from PIL import Image
import numpy as np
import random
from random import randrange
import progressbar


def numberList(minimum, maximum, minDistance, maxDistance):
    ran = [minimum, maximum]
    start = minimum
    while start + minDistance < maximum:
        if start + maxDistance > maximum:
            ran.append((maximum - start) / 2 + start)
            break
        else:
            start = randrange(start + minDistance, start + maxDistance)
            ran.append(start)

    ran.sort()
    return ran


def generate():
    print('yeet')
    image = Image.open('map.png')
    image = image.convert('RGB')

    processed = Image.new('RGB', (image.width, image.height), color=0)
    pixels = processed.load()

    noise = np.random.normal(0, 5, 100)

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

    randY = numberList(1, image.width - 2, 10, 30)
    randX = numberList(1, image.height - 2, 10, 30)

    for x in range(image.width):
        for y in range(image.height):
            r, g, b = image.getpixel((x, y))
            if r == 255 and g == 114 and b == 0:  # Land
                pixels[x, y] = (
                    255 + round(noise[random.randint(0, 99)]), 114 + round(noise[random.randint(0, 99)]),
                    00 + round(noise[random.randint(0, 99)]))
            elif r == 255 and g == 16 and b == 0:  # MainStreet
                pixels[x, y] = (255 + round(noise[random.randint(0, 99)]), 16 + round(noise[random.randint(0, 99)]),
                                0 + round(noise[random.randint(0, 99)]))
            elif r == 0 and g == 0 and b == 0:  # water
                pixels[x, y] = (0 + round(noise[random.randint(0, 99)]), 0 + round(noise[random.randint(0, 99)]),
                                0 + round(noise[random.randint(0, 99)]))
            elif r == 132 and g == 0 and b == 0:  # CityStreet
                if y in randY:
                    pixels[x, y] = (255, 255, 255)
                elif x in randX:
                    randY = numberList(1, image.width - 2, 10, 30)
                    pixels[x, y] = (255, 255, 255)
                else:
                    pixels[x, y] = (0, 0, 0)

        bar.update(x + 1)

    bar.finish()

    processed.show()
