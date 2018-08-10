from tkinter import Tk, Canvas, Frame

class TkinterCartesian():
    '''  Tkinter objects and methods: '''

    def setup(self, title='...', gridx=400, gridy=300, cellx=2, celly=2):
        '''  setup of tkinter parameters '''
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

        self.mainframe = Frame(self.root,
                               bd=0,
                               bg='grey')
        self.mainframe.grid(row=0, column=0, padx=self.padding,
                            pady=self.padding)

        self.displayframe = Frame(self.root,
                                  width=self.dframe[0], height=self.dframe[1],
                                  bd=2,
                                  bg='yellow')
        self.displayframe.grid(row=1, column=0, padx=self.padding,
                               pady=self.padding)

        self.controlframe = Frame(self.root,
                                  width=self.cframe[0], height=self.cframe[1],
                                  bd=2,
                                  bg='blue')
        self.controlframe.grid(row=0, column=1, padx=self.padding,
                               pady=self.padding)

        self.actionframe = Frame(self.mainframe,
                                 width=self.aframe[0], height=self.aframe[1],
                                 bd=0,
                                 bg='grey',)
        self.actionframe.grid(row=0, column=1, sticky='ne')

        self.yaxisframe = Frame(self.mainframe,
                                width=self.axiswidth, height=self.aframe[1],
                                bd=0,
                                bg='green')
        self.yaxisframe.grid(row=0, column=0)

        self.xaxisframe = Frame(self.mainframe,
                                width=self.aframe[0], height=self.axiswidth,
                                bd=0,
                               bg='green')
        self.xaxisframe.grid(row=1, column=1)

        self.aw = Canvas(self.actionframe,
                         width=self.aframe[0], height=self.aframe[1],
                         bg='black')
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
            point = (int(self.gridx/2 + point[0]),
                     int(self.gridy/2 - point[1]))
        else:
            point = (point[0], self.gridy - point[1])
        return point

    def plotgrid(self):
        '''  display grid '''
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
        point1 = (int(self._cartesian(point1)[0]*self.cellx),
                  int(self._cartesian(point1)[1]*self.celly))

        point2 = (int(self._cartesian(point2)[0]*self.cellx),
                  int(self._cartesian(point2)[1]*self.celly))

        self.aw.create_line(point1, point2, fill=color, width=width)

    # def xaxis(self, tick=10, mark=10, side='bottom'):
    #     '''  draw xaxis
