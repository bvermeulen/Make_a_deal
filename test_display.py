from tkinter_cartesian import TkinterCartesian
from math import sin, cos
import random


def main():

    gui = TkinterCartesian()
    title = '     ... Display Make a Deal ...'
    gui.setup(title, gridx=400, gridy=300, cellx=2, celly=2)
    gui.controls()
    gui.setorigin(center=True)

    dx1 = 0
    dx2 = 0
    while True:
        gui.refresh()
        gui.plotgrid(gridlines=False)
        point1 = (-200, 50*sin(-200/20))
        for x in range(-200, 500, 2):
            amp = random.randint(-75, 75)
            y1 = amp*sin((x+dx1)/20)+0
            amp = random.randint(-5, 5)
            y2 = amp*cos((x+dx2)/20)+0
            point2 = (x, y1+y2)
            gui.drawline(point1, point2, color='red', width=2)
            point1=point2

        dx1 += random.randint(-10, 10)
        dx2 += random.randint(-2, 2)
        gui.root.update()

    gui.root.mainloop()

if __name__ == "__main__":
    main()
