from PIL import Image
import numpy as np
import random


def generate(threads, thread_number, image, images):

    processed = Image.new('RGBA', (image.width, image.height), color=0)
    pixels = processed.load()

    noise = np.random.normal(0, 5, 100)

    for x in range(thread_number, image.width, threads):
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

    images.append(processed)
