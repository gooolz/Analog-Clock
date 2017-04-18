"""Julia Foote. This program uses the operating system's time and is used to move the hands
    on the canvas in order to make a clock along with the tkinter import functions."""

from tkinter import *
from math import pi, sin, cos
from time import *
import datetime


root = Tk()
time_1 = ''
# creates the canvas, outer circle, inner small circle and title
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
canvas = Canvas(root, width=600, height=600, bg='black')
canvas.grid(column=0, row=0, sticky=(N, W, E, S))
length = 2
canvas.create_text(300, 30, text="Julia's Radical Clock", fill="limegreen", font=('fixedsys', '25', 'bold'))
canvas.create_oval(110, 120, 490, 500, outline="limegreen", width=10)
middle_circle = canvas.create_oval(315, 315, 295, 295, fill="limegreen", outline="limegreen", width=3)
canvas.tag_raise(middle_circle)


# creates the inner dashes
def create_dashes():
    new_x = 630
    new_y = 430
    x_0 = new_x / 2.1
    l_x = 9 * new_x / 20
    y_0 = new_y / 1.4
    l_y = 9 * new_y / 20
    r_0 = 0.9 * min(l_x, l_y)
    for i in range(0, 60):
        val = pi/30 * i
        x = x_0 + r_0 * sin(val)
        y = y_0 - r_0 * cos(val)
        canvas.create_line(x, y, x+length, y + length, width=3, fill='white')


# creates the outer hour numbers
def create_big_nums():
    new_x = 700
    new_y = 550
    x_0 = new_x / 2.35
    l_x = 9 * new_x / 20
    y_0 = new_y / 1.78
    l_y = 9 * new_y / 20
    r_0 = 0.9 * min(l_x, l_y)
    for i in range(1, 13):
        val = pi / 6 * i
        x = x_0 + r_0 * sin(val)
        y = y_0 - r_0 * cos(val)
        canvas.create_text(x, y, text=str(i), font=('fixedsys', '20'), fill="limegreen")


# creates the smaller numbers
def create_lil_nums():
    new_x = 600
    new_y = 400
    x_0 = new_x / 2
    l_x = 9 * new_x / 20
    y_0 = new_y / 1.3
    l_y = 9 * new_y / 20
    r_0 = 0.9 * min(l_x, l_y)
    for i in range(0, 60, 5):
        val = pi / 30 * i
        x = x_0 + r_0 * sin(val)
        y = y_0 - r_0 * cos(val)
        canvas.create_text(x, y, text=str(i), font=('fixedsys', '10'), fill="limegreen")


def timeupdate():
    # outputs hands
    new_x = 630
    new_y = 430
    x_0 = new_x / 2.1
    l_x = 9 * new_x / 20
    y_0 = new_y / 1.4
    l_y = 9 * new_y / 20
    # length of hour, min and sec hands
    r_1 = 0.35 * min(l_x, l_y)
    r_2 = 0.65 * min(l_x, l_y)
    r_3 = 0.78 * min(l_x, l_y)
    t = localtime()
    sec = t[5] 
    minute = t[4] + sec / 60  
    hour = t[3] % 12 + minute / 60  

    # hour hand
    val = pi / 6 * hour
    x = x_0 + r_1 * sin(val)
    y = y_0 - r_1 * cos(val)
    hour_hand = canvas.create_line(x_0, y_0, x, y, fill="limegreen", width=5)
    canvas.tag_lower(hour_hand)

    # minute hand
    val = pi / 30 * minute
    x = x_0 + r_2 * sin(val)
    y = y_0 - r_2 * cos(val)
    min_hand = canvas.create_line(x_0, y_0, x, y, fill="blue", width=4)
    canvas.tag_lower(min_hand)

    # second hand
    val = pi / 30 * sec
    x = x_0 + r_3 * sin(val)
    y = y_0 - r_3 * cos(val)
    sec_hand = canvas.create_line(x_0, y_0, x, y, fill="white", width=2)
    canvas.tag_lower(sec_hand)

    # deletes so hands will be at correct positions
    canvas.delete(ALL)

# re-displays everything on the canvas so the hands are at correct angles
    canvas.create_text(300, 30, text="Julia's Radical Clock", fill="limegreen", font=('fixedsys', '25', 'bold'))
    canvas.create_oval(110, 120, 490, 500, outline="limegreen", width=10)
    middle_circle = canvas.create_oval(315, 315, 295, 295, fill="limegreen", outline="limegreen", width=3)
    canvas.tag_raise(middle_circle)
    create_lil_nums()
    create_big_nums()
    create_dashes()
    # hour hand
    val = pi / 6 * hour
    x = x_0 + r_1 * sin(val)
    y = y_0 - r_1 * cos(val)
    hour_hand = canvas.create_line(x_0, y_0, x, y, fill="limegreen", width=5)
    canvas.tag_lower(hour_hand)
    # minute hand
    val = pi / 30 * minute
    x = x_0 + r_2 * sin(val)
    y = y_0 - r_2 * cos(val)
    min_hand = canvas.create_line(x_0, y_0, x, y, fill="blue", width=4)
    canvas.tag_lower(min_hand)
    # second hand
    val = pi / 30 * sec
    x = x_0 + r_3 * sin(val)
    y = y_0 - r_3 * cos(val)
    sec_hand = canvas.create_line(x_0, y_0, x, y, fill="white", width=2)
    canvas.tag_lower(sec_hand)

    root.after(500, timeupdate)


# digital clock
def digital():
    global time_1
    time_2 = datetime.datetime.now().time().strftime("%H:%M:%S")
    new_date = datetime.datetime.strptime(time_2, '%H:%M:%S').strftime('%I:%M:%S %p')
    if new_date != time_1:
        time_1 = new_date
        clock.config(text=new_date)
    clock.after(500, digital)

# label of digital clock
clock = Label(root, font=('fixedsys', 20, 'bold'), fg='limegreen', bg='black')
clock.grid(row=0, column=0)
clock.place(x=385, y=550)


# main loop and function calls
timeupdate()
digital()
create_dashes()
create_big_nums()
create_lil_nums()
root.after(500, timeupdate)
root.mainloop()
