import tkinter as tk
from tkinter import  *
from tkinter import filedialog
from PIL import Image,ImageTk
import os
import turtle
from io import BytesIO
import random

root = tk.Tk()
# Entry1 = Entry(root)
# Entry1.pack()
# Entry1.focus_set()   

# Entry2 = Entry(root)
# Entry2.pack()
# Entry2.focus_set()   
all_pixels = []

def drawpixel(x, y, color, pixelsize ):
   
   #  turtle.tracer(0, 0)
   #  turtle.colormode(255)
   #  turtle.penup()
   #  turtle.setpos(x*pixelsize,y*pixelsize)
   #  turtle.color(color)
   #  turtle.pendown()
   #  turtle.begin_fill()
    
    
    turtle.tracer(0, 0)
    turtle.colormode(255)
    turtle.setpos(x*pixelsize,y*pixelsize)
    turtle.color(color)
    turtle.begin_fill()

    for i in range(4):
        turtle.forward(pixelsize)
        turtle.right(90)

    turtle.end_fill()

def showimage():
    turtle.hideturtle()
    turtle.update()


def saveModified(filepath,new_image):
   if not os.path.isdir('modified_images'):
      os.mkdir('modified_images')
   filename , ext= os.path.splitext(os.path.basename(filepath))

   new_filename = f"modified_{filename}"
   new_image.save('modified_images/'+new_filename+'.png')

def buildImage(data,file):
      mode = data.mode
      width, height = file.size
      
      # Load all pixels from the image.
      orig_pixel_map = file.load()

      # Create a new image matching the original image's color mode, and size.
      #   Load all the pixels from this new image as well. 
      new_image = Image.new(mode, (width, height))
      new_pixel_map = new_image.load()
      
      # Modify each pixel in the new image.
      for x in range(width):
         for y in range(height):
            # Copy the original pixel to the new pixel map.
            new_pixel_map[x, y] = orig_pixel_map[x, y]
            cpixel = new_pixel_map[x, y]
            all_pixels.append(cpixel)
         
      # drawpixel(x, y, cpixel , 100)

      return new_image
   
def openImage():
   # filepath  = filedialog.askopenfilename()
   # file = Image.open(filepath).convert('RGBA')
   file = Image.open(f'images/enthone2.png').convert('RGB')
   mode = file.mode
   width, height = file.size
   # Load all pixels from the image.
   orig_pixel_map = file.load()

   # Create a new image matching the original image's color mode, and size.
   # Load all the pixels from this new image as well. 
   new_image = Image.new(mode, (width, height))
   new_pixel_map = new_image.load()
   
   # Modify each pixel in the new image.
   for x in range(width):
      for y in range(height):
         # Copy the original pixel to the new pixel map.
         new_pixel_map[x, y] = orig_pixel_map[x, y]
         cpixel = new_pixel_map[x, y]
         all_pixels.append(cpixel)
         drawpixel(x,y,cpixel,1)
              
         showimage()
         
   
         
   # saveModified(filepath,new_image)

   tkimage = ImageTk.PhotoImage(file)
   img_label=tk.Label(canvas,image = tkimage)
   img_label.image = tkimage
   img_label.pack()
   file.close()



canvas = tk.Canvas(root, height=500, width=500, bg="white")
canvas.pack()

# openFile = tk.Button(canvas,text="Open File", command=openImage, pady="5", fg="white", bg="#263D42")
# openFile.pack()


# label1 = Label(canvas,bg="white", text= "Enter New Width Size"+'\n')
# label1.pack()

root.title ("Pixel Resizer")
icon = PhotoImage(file="logo.png")

# for x in range(30):
#     for y in range(30):
#         color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
#         drawpixel(x,y,color,100)
#         turtle.getscreen().getcanvas().postscript(file='outputname.ps')
# showimage()
openImage()
turtle.getscreen().getcanvas().postscript(file='outputname.ps') 
root.iconphoto(True,icon)
root.mainloop()


