from tkinter import *
from tkinter.ttk import *
from colorthief import ColorThief
import cv2.cv2 as cv2
import numpy
import pandas
from tkinter.filedialog import *

file_path = ''

def open_file():
    # global file_path
    global file
    with open(askopenfilename(filetypes=[('Image Files', '.jpeg'), ('Image Files', '.png')]), encoding='ANSI') as f:
        file = f.read()
    if file_path is not None:
        pass



def get_colors():
        color_thief = ColorThief(file)
        dominant_color = color_thief.get_color(quality=1)
        palette = color_thief.get_palette(color_count=6)


#potential fixes
        
# index = ["color", "color_name", "hex_code", "R", "G", "B"]
# color_list = pandas.read_csv('color list.csv', names=index, header=None)



# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title('Common Colors')
window.config(padx=0, pady=0)
window.geometry('600x500')
window.resizable(width=False, height=False)


canvas = Canvas(window, width=600, height=500)
canvas.pack(fill='both', expand=True)

canvas.create_image(0, 0, anchor='nw')

upload_image = Button(window, text='Upload Image', command=lambda: open_file())
upload_window = canvas.create_window(270, 110, anchor='nw', window=upload_image)


process = Button(window, text='Process', command=lambda: get_colors())
process_window = canvas.create_window(275, 250, anchor='nw', window=process)


window.mainloop()
