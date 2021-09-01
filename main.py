from threading import Thread
import map
from PIL import Image, ImageTk
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


src_image = Image.open('map.png')


def map_gen():

    images = []

    thread_count = 10

    threads = []

    for i in range(thread_count):
        thread = Thread(target=map.generate, args=(
            thread_count, i, src_image, images))
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

image = ImageTk.PhotoImage(src_image)
imagesprite = canvas.create_image(400, 400, image=image)

button = tk.Button(root, text="yeet", command=Thread(target=map_gen).start)
button.pack()

tk.mainloop()
