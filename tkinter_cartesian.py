from tkinter import ttk
from tkinter import Tk, Canvas, Button
from tkinter.ttk import Frame, Style, Button
# style=ttk.Style()
import pdb


class TkinterCartesian():
    '''  Tkinter objects and methods: '''

    def setup(self, title='...', gridx=400, gridy=300, cellx=2, celly=2):
        '''  setup of tkinter parameters '''
        # pdb.set_trace()
        self.gridx=gridx
        self.gridy=gridy
        self.cellx=cellx
        self.celly=celly
        self.axiswidth=20
        self.padding = 2
        self.aframe = (self.gridx*self.cellx, self.gridy*self.celly)
        self.dframe = (self.aframe[0]+self.axiswidth+self.padding, 50)
        self.cframe = (50, self.aframe[1]+self.axiswidth+self.padding)
        self.root = Tk()
        self.root.title(title)
        self.root.configure(background='darkblue')
        style = ttk.Style()
        self.exit=False

        style.configure("M.TFrame", background='grey')
        self.mainframe = ttk.Frame(self.root,
                                   borderwidth=2,
                                   style="M.TFrame")
        self.mainframe.grid(row=0, column=0, padx=self.padding,
                            pady=self.padding)

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

        style.configure("M.TFrame", background='grey')
        self.actionframe = ttk.Frame(self.mainframe,
                                     width=self.aframe[0],
                                     height=self.aframe[1],
                                     borderwidth=0,
                                     style='M.TFrame',)
        self.actionframe.grid(row=0, column=1, sticky='ne')

        style.configure("A.TFrame", background='green')
        self.yaxisframe = ttk.Frame(self.mainframe,
                                    width=self.axiswidth,
                                    height=self.aframe[1],
                                    borderwidth=0,
                                    style='A.TFrame')
        self.yaxisframe.grid(row=0, column=0)

        self.xaxisframe = ttk.Frame(self.mainframe,
                                    width=self.aframe[0],
                                    height=self.axiswidth,
                                    borderwidth=0,
                                    style='A.TFrame')
        self.xaxisframe.grid(row=1, column=1)

        self.aw = Canvas(self.actionframe,
                         width=self.aframe[0], height=self.aframe[1],
                         bg='black', bd=0)
        self.aw.pack()

        self.CENTER = False
        self.grid_x = list((x for x in range(0, self.aframe[0]+self.cellx,
                            self.cellx)))
        self.grid_y = list((y for y in range(0, self.aframe[1]+self.celly,
                            self.celly)))

    def setorigin(self, center=False):
        '''  set origin, if CENTER is True then origin is at the center of
             the window, if False center is in left bottom corner. '''
        self.CENTER = center

    def _cartesian(self, point):
        '''  translated the grid origin to normal cartersian '''
        if self.CENTER:
            point = (int(round(self.gridx/2 + point[0],0)),
                     int(round(self.gridy/2 - point[1],0)))
        else:
            point = (point[0], int(round(self.gridy - point[1],0)))
        return point

    def plotgrid(self, gridlines=False):
        '''  if display is not centered display grid otherwise display
             display x and y axis '''
        if self.CENTER:
            self.drawline((0, self.gridy/2), (0, -self.gridy/2),
                          color='grey', width=1)
            self.drawline((self.gridx/2, 0), (-self.gridx/2, 0),
                          color='grey', width=1)

        if gridlines:
            for x in self.grid_x:
                self.aw.create_line(x, 0, x, self.aframe[1],
                                    fill='grey', width=1)

            for y in self.grid_y:
                self.aw.create_line(0, y, self.aframe[0], y,
                                    fill='grey', width=1)

    def colorcell(self, point, color='white', center=False,
                  size=(2, 2), shape='oval'):
        ''' plots a color cell at grid point (x, y) '''
        point = self._cartesian(point)
        if center:
            offset=(0, 0)
        else:
            offset=(+self.cellx/2, -self.celly/2)

        bbox = (int(round(point[0]*self.cellx+offset[0]-size[0]/2)),
                int(round(point[1]*self.celly+offset[1]-size[1]/2)),
                int(round(point[0]*self.cellx+offset[0]+size[0]/2)),
                int(round(point[1]*self.celly+offset[1]+size[1]/2)))

        if shape == 'oval':
            self.aw.create_oval(bbox, fill=color, width=0)

        elif shape == 'rectangle':
            self.aw.create_rectangle(bbox, fill=color, width=0)

        else:
            raise ValueError("shape is either 'oval' or 'rectangle'")

    def drawline(self, point1, point2, color='white', width=2):
        '''  draws a line from point1 to point2 '''
        point1 = (self._cartesian(point1)[0]*self.cellx,
                  self._cartesian(point1)[1]*self.celly)

        point2 = (self._cartesian(point2)[0]*self.cellx,
                  self._cartesian(point2)[1]*self.celly)

        self.aw.create_line(point1, point2, fill=color, width=width)

    # def xaxis(self, tick=10, mark=10, side='bottom'):
    #     '''  draw xaxis

    def controls(self):
        '''  define control buttons and action '''
        self.root.protocol('WM_DELETE_WINDOW', self.exit_program)
        self.btn_exit = Button(self.controlframe, text='exit',
                                   command=self.exit_program)
        self.btn_exit.pack()

    def exit_program(self):
        '''  leave the program '''
        print(f'we will leave the program now ...')
        self.root.after(1000)
        self.exit=True
        self.root.destroy()
