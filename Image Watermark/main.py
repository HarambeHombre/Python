import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

def open_file():
    types = ('*.JPG' ,'*.jpg; *.png; *.bmp')
    file_open = tk.filedialog.askopenfile(initialdir='.', filetypes=[types])
    if file_open:
        image = Image.open(file_open.name).convert('RGBA')
        resized = image.resize((800, 600))
        image_overlay = Image.open('overlay.png').convert('RGBA')
        resized_overlay = image_overlay.resize((800, 600))
        resized.paste(resized_overlay, mask=resized_overlay)
        resized.show()

window = tk.Tk()
window.title("Image Viewer w/ Watermark")
window.geometry('400x100')

label = tk.Label(window, text='Click the button below to open an image with a watermark applied.')
label.pack(padx= 20, pady=20,)
button = tk.Button(window, text="Choose Image", command=open_file)
button.pack(padx= 20,)

window.mainloop()