from tkinter_cartesian import TkinterCartesian
from math import sin, cos
import random


def main():

    gui = TkinterCartesian()
    title = '     ... Display test display 1 ...'
    gui.setwindow(x=6, y=4, dpi=92, xmin=-210, xmax=500, ymin=-1.5, ymax=1.5,
                  tickx=20, markx=100, ticky=0.2, marky=0.5)
    gui.setuptk(title)
    gui.controls()
    gui.xaxis()
    gui.yaxis()
    # gui.plotframe()

    dx = 0
    while not gui.exit:
        gui.refresh()
        gui.grid()
        amp = 1 #random.randint(-10, 10)
        point1 = ''
        for x in range(-250, 500, 2):
            y = amp*sin((x+dx)/20)+0
            point2= (x, y)
            gui.drawline(point1, point2, color='red', width=2)
            point1=point2

        dx += 2
        gui.root.update()
        gui.root.after(10)


if __name__ == "__main__":
    main()
