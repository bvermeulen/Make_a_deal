from tkinter_cartesian import TkinterCartesian
from math import sin


def main():

    gui = TkinterCartesian()
    title = '     ... Display Make a Deal ...'
    gui.setup(title, gridx=400, gridy=300, cellx=2, celly=2)
    gui.controls()
    gui.setorigin(center=True)
    gui.plotgrid(gridlines=False)

    gui.colorcell((0, 0), color='white', center=True, size=(30, 30),
                  shape='rectangle')

    gui.drawline((0, 0), (10, 10), color='red', width=1)

    point1 = (-200, 50*sin(-200/20))
    for x in range(-200, 500, 2):
        y = 50*sin(x/20)+0
        point2 = (x, y)
        gui.drawline(point1, point2, color='blue', width=5)
        point1=point2

    gui.root.mainloop()

if __name__ == "__main__":
    main()
