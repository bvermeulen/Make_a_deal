import numpy as np
import random
from scipy.misc import imread, imsave, imresize
from tkinter_cartesian import TkinterCartesian
from math import sin


def hex_color(color):
    ''' converts color (R, G, B) to a Hex string for tkinter
    '''
    color = list(color)
    color[0]=int(round(color[0],0))
    color[1]=int(round(color[1],0))
    color[2]=int(round(color[2],0))

    if color != '':
        hcolor = f'#{color[0]:02x}{color[1]:02x}{color[2]:02x}'
    else:
        hcolor = ''

    return hcolor

def main():
    gui = TkinterCartesian()
    title='     ... display a picture ...'
    gridx, gridy=300, 320
    cellx, celly=2, 2
    gui.setup(title, gridx=gridx, gridy=gridy, cellx=cellx, celly=celly)
    gui.controls()
    gui.setorigin(center=False)
    gui.xaxis()
    gui.yaxis()

    img = imread('picture.JPG')
    HEIGHT=img.shape[0]
    WIDTH=img.shape[1]
    img = imresize(img, (HEIGHT,WIDTH))

    size=np.array([cellx,celly])
    while not gui.exit:
        gui.refresh()
        gui.plotgrid(gridlines=False)

        for i in range(HEIGHT):
            for j in range(WIDTH):
                rgb= (img[i, j, 0], img[i, j, 1], img[i, j, 2])
                color = hex_color(rgb)
                gui.colorcell((j, gridy/2-i), color=color, center=False,
                              size=size*1, shape='rectangle')
        gui.root.update()

if __name__ == "__main__":
    main()
