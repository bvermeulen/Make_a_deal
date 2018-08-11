from tkinter_cartesian import TkinterCartesian
import random
import PIL
from PIL import Image
from math import sin
import random


def hex_color(color):
    ''' converts color (R, G, B) to a Hex string for tkinter
    '''
    if color != '':
        hcolor = f'#{color[0]:02x}{color[1]:02x}{color[2]:02x}'
    else:
        hcolor = ''

    return hcolor


def main():

    gui = TkinterCartesian()
    title='     ... Display a picture ...'
    gridx, gridy=300, 320
    gui.setup(title, gridx=gridx, gridy=gridy, cellx=2, celly=2)
    gui.controls()
    gui.setorigin(center=True)
    gui.plotgrid(gridlines=False)

    img = Image.open('picture.JPG').convert('L')  # convert image to 8-bit grayscale
    WIDTH, HEIGHT = img.size
    print(f'WIDTH: {WIDTH}, HEIGHT: {HEIGHT}')
    data = list(img.getdata()) # convert image data to a list of integers
    # convert that to 2D list (list of lists of integers)
    offset=0
    matrix=[]
    for i in range(0, HEIGHT):
        row=[]
        for j in range(offset, offset+WIDTH):
            row.append(data[j])
        matrix.append(row)
        offset=offset+WIDTH

    # data = [data[offset:offset+WIDTH] for offset in range(0, WIDTH*HEIGHT, WIDTH)]

    dx=0
    while True:
        gui.refresh()
        for i in range(HEIGHT):
            for j in range(WIDTH):
                rgb= matrix[i][j]
                color = hex_color((rgb, rgb, 255))
                gui.colorcell((j, gridy/2-i), color=color, center=False,
                              size=(5, 5), shape='oval')


        point1 = (-200, 50*sin(-200/20))
        for x in range(-200, 500, 2):
            y = 50*sin((x+dx)/20)+0
            point2 = (x, y)
            gui.drawline(point1, point2, color='red', width=5)
            point1=point2

        dx += 5
        gui.root.update()


    gui.root.mainloop()


if __name__ == "__main__":
    main()
