from tkinter_cartesian import TkinterCartesian
import numpy as np
from scipy.misc import imread

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
    title = '     ... Display test display 3 (picture)...'
    # gui.setwindow(x=4, y=4, dpi=92, xmin=-10, xmax=10, ymin=-10, ymax=10,
    #               tickx=1, markx=3, ticky=0.5, marky=3)
    gui.setwindow(x=5, y=5, dpi=92, xmin=0, xmax=180, ymin=0, ymax=200,
                  tickx=10, markx=50, ticky=10, marky=50)

    gui.setuptk(title)
    gui.controls()
    gui.xaxis()
    gui.yaxis()

    size = np.array([1, 1])
    img = imread('picture.JPG')
    HEIGHT=img.shape[0]
    WIDTH=img.shape[1]
    print(f'width: {WIDTH}, height: {HEIGHT}')
    while not gui.exit:
        gui.refresh()
        gui.grid()
        gui.frame()

        for i in range(HEIGHT):
            for j in range(WIDTH):
                rgb= (img[i, j, 0], img[i, j, 1], img[i, j, 2])
                color = hex_color(rgb)
                gui.plotcell((j, HEIGHT-i), color=color, center=False,
                              size=size*3, shape='rectangle')
        gui.root.update()


if __name__ == "__main__":
    main()
