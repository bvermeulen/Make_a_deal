from tkinter import ttk
from tkinter import Tk, Canvas, Button
from tkinter.ttk import Frame, Style, Button
import numpy as np
import pdb


class TkinterCartesian():
    '''  Tkinter objects and methods: '''

    def setwindow(self, x=4, y=3, dpi=92, xmin=None, xmax=None, ymin=None,
                  ymax=None, tickx=None, markx=None, ticky=None, marky=None):
        ''' set the window boundary '''
        self.x=x
        self.y=y
        self.dpi=dpi
        self.pixelx = x*dpi
        self.pixely = y*dpi
        self.xmin = xmin
        self.xmax = xmax
        self.ymin = ymin
        self.ymax = ymax
        self.tickx = tickx
        self.markx = markx
        self.ticky = ticky
        self.marky = marky

    def _cartesian(self, point):
        '''  translate point in cartersian (x, y) to pixel grid point in
             plotwindow (px, py)'''
        px = (point[0]-self.xmin)/(self.xmax-self.xmin)*self.pixelx
        py = self.pixely*(1-(point[1]-self.ymin)/(self.ymax-self.ymin))
        px = px
        py = py
        return (px, py)

    def plotframe(self):
        '''  plot the frame  '''
        self.drawline((self.xmin, self.ymin), (self.xmax, self.ymin),
                      color='white', width=1)
        self.drawline((self.xmin, self.ymax), (self.xmax, self.ymax),
                      color='white', width=1)
        self.drawline((self.xmin, self.ymin), (self.xmin, self.ymax),
                      color='white', width=1)
        self.drawline((self.xmax, self.ymin), (self.xmax, self.ymax),
                      color='white', width=1)

    def grid(self):
        '''  if display is not centered display grid otherwise display
             display x and y axis '''
        if self.tickx:
            ticks = np.arange(self.xmin, self.xmax, self.tickx)
            for x in ticks:
                self.drawline((x, self.ymin), (x, self.ymax),
                              color='grey', width=1)

        if self.ticky:
            ticks = np.arange(self.ymin, self.ymax, self.ticky)
            for y in ticks:
                self.drawline((self.xmin, y), (self.xmax, y),
                              color='grey', width=1)

    def plotcell(self, point, color='white', center=False,
                  size=(2, 2), shape='rectangle'):
        ''' plots a color cell at grid point (x, y) '''

        if not center:
            point = list(point)
            point[0] = point[0] + 0.5
            point[1] = point[1] + 0.5

        ppoint = self._cartesian(point)

        bbox = (int(round(ppoint[0]-size[0]/2)),
                int(round(ppoint[1]-size[1]/2)),
                int(round(ppoint[0]+size[0]/2)),
                int(round(ppoint[1]+size[1]/2)))

        if shape == 'oval':
            self.pw.create_oval(bbox, fill=color, width=0)

        elif shape == 'rectangle':
            self.pw.create_rectangle(bbox, fill=color, width=0)

        else:
            raise ValueError("shape is either 'oval' or 'rectangle'")

    def drawline(self, point1, point2, color='white', width=2):
        '''  draws a line from point1 to point2 '''
        ppoint2 = self._cartesian(point2)
        if not point1:
            ppoint1 = ppoint2

        else:
            ppoint1 = self._cartesian(point1)

        self.pw.create_line(ppoint1[0], ppoint1[1], ppoint2[0], ppoint2[1],
                            fill=color, width=width)

    def refresh(self):
        '''  refresh the screen '''
        self.pw.delete('all')

    def xaxis(self):
        '''  draw x-axis '''
        if self.tickx:
            ticks = np.arange(self.xmin, self.xmax, self.tickx)
            ticksize=4
            for x in ticks:
                ppoint = list(self._cartesian((x, 0)))
                ppoint[0] = ppoint[0]+self.axiswidth
                self.aw.create_line((ppoint[0], self.pixely+1),
                                    (ppoint[0], self.pixely+1+ticksize),
                                    fill='white', width=1)

        if self.markx:
            marks = np.arange(self.xmin, self.xmax, self.markx)
            ticksize=8
            for x in marks:
                if self.markx < 10:
                    _num = str(f'{float(x):.1f}')
                else:
                    _num = str(f'{x}')
                ppoint = list(self._cartesian((x, 0)))
                ppoint[0] = ppoint[0]+self.axiswidth
                self.aw.create_text(ppoint[0], self.pixely+20, text=_num,
                                    fill='white')
                self.aw.create_line((ppoint[0], self.pixely+1),
                                    (ppoint[0], self.pixely+1+ticksize),
                                    fill='white', width=1)

    def yaxis(self):
        '''  draw y-axis '''
        if self.ticky:
            ticks = np.arange(self.ymin, self.ymax, self.ticky)
            ticksize=4
            for y in ticks:
                ppoint = self._cartesian((0, y))
                self.aw.create_line((self.axiswidth-1, ppoint[1]),
                                    (self.axiswidth-1-ticksize, ppoint[1]),
                                    fill='white', width=1)

        if self.marky:
            marks = np.arange(self.ymin, self.ymax, self.marky)
            ticksize=8
            for y in marks:
                if self.marky < 10:
                    _num = str(f'{float(y):.1f}')
                else:
                    _num = str(f'{y}')

                ppoint = self._cartesian((0, y))
                self.aw.create_text(self.axiswidth-25, ppoint[1], text=_num,
                                    fill='white')
                self.aw.create_line((self.axiswidth-1, ppoint[1]),
                                    (self.axiswidth-1-ticksize, ppoint[1]),
                                    fill='white', width=1)

    def setuptk(self, title='...'):
        self.axiswidth=46
        self.padding = 2
        self.aframe = (self.pixelx+self.axiswidth, self.pixely+self.axiswidth)
        self.pframe = (self.pixelx, self.pixely)
        self.dframe = (self.aframe[0]+self.padding, 46)
        self.cframe = (46, self.aframe[1]+self.padding)
        self.root = Tk()
        self.root.title(title)
        self.root.configure(background='darkblue')
        style = ttk.Style()
        self.exit=False

        style.configure("B.TFrame", background='yellow')
        self.displayframe = ttk.Frame(self.root,
                                      width=self.dframe[0],
                                      height=self.dframe[1],
                                      borderwidth=2,
                                      style='B.TFrame')
        self.displayframe.grid(row=1, column=0, padx=self.padding,
                               pady=self.padding, sticky='w')

        self.controlframe = ttk.Frame(self.root,
                                      width=self.cframe[0],
                                      height=self.cframe[1],
                                      borderwidth=2,
                                      style='B.TFrame')
        self.controlframe.grid(row=0, column=1, padx=self.padding,
                               pady=self.padding, sticky='n')

        self.aw = Canvas(self.root,
                         width=self.aframe[0], height=self.aframe[1],
                         bg='black', bd=0)
        self.aw.grid(row=0, column=0, padx=self.padding,
                               pady=self.padding, sticky='nw')

        self.pw = Canvas(self.root,
                         width=self.pframe[0], height=self.pframe[1],
                         bg='black', bd=0)
        self.pw.grid(row=0, column=0, padx=self.padding,
                               pady=self.padding, sticky='ne')

    def controls(self):
        '''  define control buttons and action '''
        self.root.protocol('WM_DELETE_WINDOW', self.exit_program)
        self.btn_exit = Button(self.controlframe, text='exit',
                                   command=self.exit_program)
        self.btn_exit.pack()

    def exit_program(self):
        '''  leave the program '''
        print(f'we will leave the program now ...')
        self.root.after(100)
        self.exit=True
        self.root.destroy()
