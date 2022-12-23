# GLOBAL VARIABLES
WIDTH = 800
HEIGHT = 500
BG_COLOR = 'white'
BUTTON_COLOR = 'grey'
BUTTON_GAP = 2
WIDTH_BUTTON = 80
DISTANCE_BW_DASHLINE_AND_BUTTON = 10
PADDING_X = 2 * BUTTON_GAP
PADDING_Y = 10
NO_OF_BUTTON = 5
INTERVAL = 5 # in seconds

# DERIVED VARIABLES
START_ANGLE = -90
ANGULAR_DISPLACEMENT = 180 // NO_OF_BUTTON

# STORAGE
ITEM_BUTTON = []
BUTTON_ACTION = [] # list of function which will execute on action
BUTTON_CLEAR = [] # list of function which will execute on lost focus

from tkinter import *
import math
from PIL import ImageTk, Image
import threading
import winsound

root = Tk()
root.wm_attributes('-transparentcolor', 'black')
canvas = Canvas(root, width = WIDTH, height = HEIGHT, borderwidth = 0, highlightthickness = 0,bg = BG_COLOR)
canvas.grid()

def _create_circle(self, x, y, r, **kwargs):
    return self.create_oval(x-r, y-r, x+r, y+r, **kwargs)
Canvas.create_circle = _create_circle

def _create_circle_arc(self, x, y, r, **kwargs):
    if "start" in kwargs and "end" in kwargs:
        kwargs["extent"] = kwargs["end"] - kwargs["start"]
        del kwargs["end"]
    return self.create_arc(x-r, y-r, x+r, y+r, **kwargs)
Canvas.create_circle_arc = _create_circle_arc

# CREATING ARC BUTTON
def button(start, end):
    return canvas.create_circle_arc(PADDING_X, HEIGHT // 2, HEIGHT // 2 - PADDING_Y, fill = BUTTON_COLOR, outline = "", start = start, end = end)

# CREATING CIRCULAR DASHED LINE
def dashed_circle(start, end, dash):
    for i in range(start, end + 1, sum(dash)):
        canvas.create_circle_arc(PADDING_X, HEIGHT // 2, HEIGHT // 2 - PADDING_Y - WIDTH_BUTTON - DISTANCE_BW_DASHLINE_AND_BUTTON, style="arc", outline = BUTTON_COLOR, width = 3, start = i, end = i + dash[0])

def on_remove(x):
    canvas.itemconfig(ITEM_BUTTON[x], fill = BUTTON_COLOR)
    if x == 0:
        canvas.delete(C1)
        canvas.delete(C2)
    elif x == 1:
        canvas.delete(C3)
        canvas.delete(C4)
    elif x == 2:
        canvas.delete(C5)
        canvas.delete(C6)
    elif x == 3:
        canvas.delete(C7)
        canvas.delete(C8)
    else:
        canvas.delete(C9)
        canvas.delete(C0)
    
    try: BUTTON_CLEAR[x]()
    except: pass
    
def on_action(x):
    try: BUTTON_ACTION[x]()
    except: pass

    if x == 0 :

        global C1 , C2
        C1 = canvas.create_rectangle(280 , 470 ,720 , 430, outline = "blue" , fill = "red" , width = 2)
        C2 = canvas.create_text(500, 450, text="HCD ACTIVATED" ,font = "black 30")
        winsound.PlaySound('m1.wav', winsound.SND_FILENAME)

    elif x==1 :

        global C3 , C4
        C3 = canvas.create_rectangle(280 , 370 ,720 , 330, outline = "blue" , fill = "red" , width = 2)
        C4 = canvas.create_text(500, 350, text="SMOKE DETECTOR ACTIVATED" , font="black 20")
        winsound.PlaySound('m2.wav', winsound.SND_FILENAME)

    elif x == 2 :

        global C5 , C6
        C5 = canvas.create_rectangle(280 , 270 ,720 , 230, outline = "blue" , fill = "red" , width = 2)
        C6 = canvas.create_text(500, 250, text="ESD ACTIVATED" , font="black 30")
        winsound.PlaySound('m3.wav', winsound.SND_FILENAME)

    elif x == 3 :

        global C7 , C8
        C7 = canvas.create_rectangle(280 , 170 ,720 , 130, outline = "blue" , fill = "red" , width = 2)
        C8 = canvas.create_text(500, 150, text="DYKE VALVE OPENED" , font="black 30")
        winsound.PlaySound('m4.wav', winsound.SND_FILENAME)

    else :

        global C9 , C0
        C9 = canvas.create_rectangle(280 , 70 ,720 , 30 , outline = "blue" , fill = "red" , width = 2)
        C0 = canvas.create_text(500, 50, text="EGKMS" , font="black 30")
        winsound.PlaySound('m1.wav', winsound.SND_FILENAME)

    canvas.itemconfig(ITEM_BUTTON[x], fill = 'blue')
    threading.Timer(INTERVAL, lambda : on_remove(x)).start()
    
# ENCOUNTER THE BUTTON CLICK
def click_event(event):
    x = (event.x - PADDING_X)
    y = (event.y - HEIGHT // 2)
    r = (x * x + y * y) ** 0.5
    if not (HEIGHT // 2 - PADDING_Y - WIDTH_BUTTON <= r <= HEIGHT // 2 - PADDING_Y): return
    theta = -(math.atan(y / x) * 180) / math.pi
    for i in range(NO_OF_BUTTON):
        start = START_ANGLE + i * ANGULAR_DISPLACEMENT + BUTTON_GAP * int(i != 0)
        end = START_ANGLE + (i + 1) * ANGULAR_DISPLACEMENT - BUTTON_GAP * int(i != NO_OF_BUTTON - 1)
        if start <= theta <= end:
            on_action(i)
            break

# CREATING BUTTONS
for i in range(NO_OF_BUTTON):
    start = START_ANGLE + i * ANGULAR_DISPLACEMENT + BUTTON_GAP * int(i != 0)
    end = START_ANGLE + (i + 1) * ANGULAR_DISPLACEMENT - BUTTON_GAP * int(i != NO_OF_BUTTON - 1)
    ITEM_BUTTON.append(button(start, end))

canvas.bind('<Button-1>', click_event)
canvas.create_circle_arc(PADDING_X, HEIGHT // 2, HEIGHT // 2 - PADDING_Y - WIDTH_BUTTON, fill= BG_COLOR, outline = "", start = -90, end = 90)


img = Image.open("HP.jpg")
w, h = img.size
img = ImageTk.PhotoImage(img)
canvas.create_image(w // 2 + PADDING_X, HEIGHT // 2, image=img)

img1 = Image.open("1.png")
img1 = ImageTk.PhotoImage(img1)
canvas.create_image(60, 60, image=img1)

img2 = Image.open("2.png")
img2 = ImageTk.PhotoImage(img2)
canvas.create_image(165, 130, image=img2)

img3 = Image.open("3.png")
img3 = ImageTk.PhotoImage(img3)
canvas.create_image(200, 250, image=img3)

img4 = Image.open("4.png")
img4 = ImageTk.PhotoImage(img4)
canvas.create_image(165, 375, image=img4)

img5 = Image.open("5.png")
img5 = ImageTk.PhotoImage(img5)
canvas.create_image(60, 440, image=img5)

dashed_circle(-90, 90, (3, 3))

root.title("HP Graphics")
root.mainloop()