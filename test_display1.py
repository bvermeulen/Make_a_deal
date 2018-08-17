from tkinter_cartesian import TkinterCartesian
from math import sin, cos
import random


def main():

    xmin, xmax, ymin, ymax=-210, 500, -1.5, 1.5
    gui = TkinterCartesian()
    title = '     ... Display test display 1 ...'
    gui.setwindow(x=5, y=3, dpi=92, xmin=xmin, xmax=xmax, ymin=ymin, ymax=ymax,
                  tickx=20, markx=100, ticky=0.2, marky=0.5)
    gui.setuptk(title)
    gui.controls()

    dx = 0
    while not gui.exit:
        gui.refresh()
        gui.grid()
        gui.frame()
        gui.xaxis()
        gui.yaxis()
        amp = 1 #random.randint(-10, 10)
        point1 = ''
        for x in range(xmin, xmax, 1):
            y = amp*sin((x+dx)/20)+0
            point2= (x, y)
            gui.drawline(point1, point2, color='red', width=2)
            point1=point2

        dx += 2
        gui.root.update()
        gui.root.after(10)


if __name__ == "__main__":
    main()
