from threading import Thread
import map
from PIL import Image
from random import randrange
import tkinter as tk


def number_list(minimum, maximum, min_distance, max_distance):
    ran = [minimum, maximum]
    start = minimum
    while start + min_distance < maximum:
        if start + max_distance > maximum:
            ran.append((maximum - start) / 2 + start)
            break
        else:
            start = randrange(start + min_distance, start + max_distance)
            ran.append(start)

    ran.sort()
    return ran


def map_gen():
    image = Image.open('map.png')
    image = image.convert('RGB')

    images = []

    thread_count = 100

    threads = []

    for i in range(thread_count):
        thread = Thread(target=map.generate, args=(
            thread_count, i, image, images))
        threads.append(thread)
        thread.start()

    for t in threads:
        t.join()

    out = images[0]

    for i in range(len(images)):
        out.paste(images[i], (0, 0), images[i])

    out.show()


root = tk.Tk()
canvas = tk.Canvas(root,
                   width=500,
                   height=500)
canvas.pack()

print(type(canvas))


def add_pixel(x, y):
    canvas.create_rectangle(x, y, x, y, outline="white")


def test():
    for i in range(500):
        for j in range(500):
            print(i, j)
            add_pixel(i, j)


button = tk.Button(root, text="yeet", command=test).pack()

tk.mainloop()
