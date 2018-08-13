from numpy import array, arange, sin, pi
from tkinter import Tk, Frame, Button, Canvas, PhotoImage
import matplotlib as mpl
import matplotlib.backends.tkagg as tkagg
from matplotlib.backends.backend_agg import FigureCanvasAgg
import matplotlib.image as mpimg

def draw_figure(canvas, figure, loc=(0, 0)):
    """ Draw a matplotlib figure onto a Tk canvas

    loc: location of top-left corner of figure on canvas in pixels.
    Inspired by matplotlib source: lib/matplotlib/backends/backend_tkagg.py
    """
    figure_canvas_agg = FigureCanvasAgg(figure)
    figure_canvas_agg.draw()
    figure_x, figure_y, figure_w, figure_h = figure.bbox.bounds
    figure_w, figure_h = int(figure_w), int(figure_h)
    mplplot = PhotoImage(master=canvas, width=figure_w, height=figure_h)

    # Position: convert from top-left anchor to center anchor
    canvas.create_image(loc[0] + figure_w/2, loc[1] + figure_h/2, image=mplplot)

    # Unfortunately, there's no accessor for the pointer to the native renderer
    tkagg.blit(mplplot, figure_canvas_agg.get_renderer()._renderer, colormode=2)

    # Return a handle which contains a reference to the photo object
    # which must be kept live or else the picture disappears
    return mplplot


root = Tk()
width, height = 1200, 500
plotframe = Frame(root)
plotframe.pack(fill='both', expand='yes')
tkcanvas = Canvas(plotframe, width=width, height=height, bg='white')
tkcanvas.pack(anchor='w', fill='both', expand='yes')

btn_panel = Frame(root, height=45, bg='lightgreen')
btn_panel.pack(side='bottom', fill="both", expand="yes")

btn_exit = Button(btn_panel, text='exit', command=lambda: root.destroy())
btn_exit.pack(anchor='w')

image = mpimg.imread("picture.JPG")
figure = mpl.figure.Figure()

# figure.figimage(image, xo=0, yo=300)
# plot=figure.add_subplot(111)
# plot.imshow(image)
# _photo = draw_figure(tkcanvas, figure, loc=(400, 10))
# root.update()

figure.suptitle('picture', fontsize=20)
plot = figure.add_subplot(211)
plot.imshow(image)
_photo = draw_figure(tkcanvas, figure, loc=(600, 10))
root.update()
root.after(5000)


dt = 0
while True:
    figure= mpl.figure.Figure() # figsize=(6,4))
    figure.suptitle('sine wave', fontsize=20)
    plot=figure.add_subplot(111)
    t = arange(0.0, 5.0, 0.01)
    s = 10*sin(2*(pi*t+dt))
    dt += 0.05
    plot.plot(t, s)
    _placeholder = draw_figure(tkcanvas, figure, loc=(0,10))
    root.update()

root.mainloop()
