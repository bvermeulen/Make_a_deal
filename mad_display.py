from tkinter_cartesian import TkinterCartesian
import random

def pickset(doors, doors_to_open):
    doors_set = set(range(1, doors+1))
    price_set = set(random.sample(doors_set, 1))
    choice1_set = set(random.sample(doors_set, 1))
    open_set = set(random.sample(doors_set.difference(price_set).
                   difference(choice1_set), doors_to_open))
    choice2_set = set(random.sample(doors_set.difference(open_set).
                      difference(choice1_set), 1))
    win_1 = choice1_set.issubset(price_set)
    win_2 = choice2_set.issubset(price_set)

    return win_1, win_2


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
    title = '     ... Display Make a Deal ...'
    gui.setup(title, gridx=120, gridy=100, cellx=5, celly=5)
    gui.controls()
    gui.setorigin(center=True)

    doors = 80
    mad = []
    while not gui.exit:
        gui.aw.delete('all')
        gui.plotgrid()
        for i in range(1, doors+1):
            row = []
            for j in range(1, doors-1):
                if j<=i-2:
                    theoratic = (i-1)/i*(1/(i-j-1))
                    _, win2 = pickset(i, j)
                    difference = abs(10*theoratic - win2)
                    rgb = min(int(difference*100), 255)
                    color = hex_color((rgb, int(rgb), int(rgb)))
                    gui.colorcell((i, j), color=color, center=False,
                                  size=(5, 5), shape='oval')
                    row.append(_)

                else:
                    row.append(0)

            mad.append(row)

        gui.root.update()


if __name__ == "__main__":
    main()
