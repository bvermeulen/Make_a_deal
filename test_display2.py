from tkinter_cartesian import TkinterCartesian
from math import sin, cos
import random


def main():

    gui = TkinterCartesian()
    title = '     ... Display test display 2 ...'
    # gui.setwindow(x=4, y=4, dpi=92, xmin=-10, xmax=10, ymin=-10, ymax=10,
    #               tickx=1, markx=3, ticky=0.5, marky=3)
    gui.setwindow(x=4, y=4, dpi=92, xmin=-10, xmax=10, ymin=-10, ymax=10,
                  tickx=1, markx=2, ticky=1, marky=2)

    gui.setuptk(title)
    gui.controls()

    dx = 0
    while not gui.exit:
        gui.refresh()
        gui.grid()
        gui.frame()
        gui.xaxis()
        gui.yaxis()

        for x in range(-11, 11):
            gui.plotcell((x, x), color='yellow', center=False,
                         size=(20, 20), shape='oval')

        gui.root.update()
        gui.root.after(10)


if __name__ == "__main__":
    main()
