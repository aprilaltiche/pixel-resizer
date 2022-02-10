# Imports
import os
import tkinter as tk
from tkinter import filedialog
from tkinter import  *
from turtle import Turtle, Screen
from PIL import Image,ImageTk
import tkinter as tk

from numpy import int64

root = tk.Tk()


wn = Screen()
wn.colormode(255)
wn.tracer(0,0)

turtle = Turtle()
turtle.speed("fastest")
# turtle.down() # Lift pen so there is no streak across the window
wn.title("Pixel Builder")
if not os.path.isdir('images'):
        os.mkdir('images')
def mkDir():
    
    if not os.path.isdir('resized_images'):
        os.mkdir('resized_images')
    if not os.path.isdir('ps'):
        os.mkdir('ps')


# Load Image
def buildImage():
 try:
#    get input values
    new_image_size=int(Entry1.get())
    pixelsize=int(Entry2.get())
        # select file then convert to rgb 
    filepath  = filedialog.askopenfilename()
    file = Image.open(filepath).convert('RGB')
    filename , ext= os.path.splitext(os.path.basename(filepath))    
    width, height = file.size
    # set window size and location
    
    # if image is less than 48px resize it
    if width > 48 and height > 48:
        img = file.resize((new_image_size,new_image_size), Image.ANTIALIAS)
        img.save(f'images/{filename}.png') 
        
    # for image in os.listdir('images'):
        im = Image.open(f"images/{filename}.png").convert("RGB")            
        wn.reset() 
        resizePixel(im,pixelsize,filename)
        
    resizePixel(file,pixelsize,filename)
    
    
 except Exception as e: print(e)
def resizePixel(file,pixelsize,filename):
    pix = file.load()    
    # Loop through the Y of the image
    width, height = file.size
    wn.setup(width *pixelsize, height *pixelsize,startx=None,starty=None)
    for y in range(height):
        
        turtle.sety((height/2 - y)*pixelsize)
        
        # Loop through the X of the image
        for x in range(width):
            # Get color of pixel, set color of turtle
            turtle.color(pix[x, y])
            # Move turtle
            
            turtle.penup()
            turtle.setx((x - width/2)*pixelsize)
            turtle.begin_fill()
            for i in range(4):
                # motion
                turtle.forward(pixelsize)
                turtle.right(90)  
                
            turtle.end_fill()
    mkDir()
    turtle.getscreen().getcanvas().postscript(file= f'ps/{filename}.ps') 
    
    psimage=Image.open(f'ps/{filename}.ps')
    psimage.save(f'resized_images/{filename}.png')
    wn.hideturtle()
    # Update the window
    wn.update()
    file.close()
     
# def buttonclick(x,y):
#     print("You clicked at this coordinate({0},{1})".format(x,y))
    
# wn.onscreenclick(buttonclick,1)
# wn.listen()  # listen to incoming connections


canvas = tk.Canvas(root, height=500, width=500, bg="white")
canvas.pack()

label1 = Label(canvas,bg="white", text= "Enter New Image size"+'\n')
label1.pack()
Entry1 = Entry(canvas)
Entry1.insert(END, '32')
Entry1.pack()
Entry1.focus_set() 
 
label2 = Label(canvas,bg="white", text= "Enter New Pixel Size"+'\n')
label2.pack()
Entry2 = Entry(canvas)
Entry2.insert(END, '12')
Entry2.pack()
Entry2.focus_set() 

label3 = Label(canvas,bg="white", text= "Enter New Pixel Depth"+'\n')
label3.pack()
Entry3 = Entry(canvas)
Entry3.insert(END, '8')
Entry3.pack()
Entry3.focus_set() 

# buildImage()
openFile = tk.Button(canvas,text="Open File", command=buildImage, pady="5", fg="white", bg="#263D42")
openFile.pack()

root.title ("Pixel Resizer")
icon = PhotoImage(file="logo.png")
wn.mainloop()