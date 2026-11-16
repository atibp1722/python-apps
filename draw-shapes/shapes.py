import numpy as np
from PIL import Image
import os

# class for canvas
class Canvas:

    # define the height, width and color of canvas
    def __init__(self, height, width, color):
        self.height = height
        self.width = width
        self.color = color
        # numpy 3D (heightXwidthXrgb) array with 0's
        self.data = np.zeros((self.height, self.width,3),dtype=np.uint8)
        self.data[:] = self.color

    # actual canvas
    def create_canvas(self,image_path):
        # directory to save the image file
        dir_name = os.path.dirname(image_path)
        if dir_name:
            os.makedirs(dir_name, exist_ok=True)
        # convert numpy pixel to image  
        image = Image.fromarray(self.data,'RGB')
        image.save(image_path)

# class for rectangle
class Rectangle:
    # define rectangle properties
    def __init__(self, x, y, height, width, color):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.color = color

    def draw_rectangle(self, canvas):
        # array slicing for pixel color values 
        canvas.data[self.y:self.y+self.height, self.x:self.x+self.width] = self.color

# class for square
class Square:
    # define square properties
    def __init__(self, x, y, side, color):
        self.x = x
        self.y = y
        self.side = side
        self.color = color

    def draw_square(self, canvas):
        # array slicing to color square in canvas
        canvas.data[self.y:self.y+self.side, self.x:self.x+self.side] = self.color

# canvas dimensions from user
cnvs_hgt = int(input('Enter canvas height: '))
cnvs_wdt = int(input('Enter canvas width: '))

# black or white canvas color user option
colors = {'white':(255,255,255), 'black':(0,0,0)}
cnvs_clr = input('Select canvas color[white/black]: ')

# initialize canvas 
test = Canvas(height=cnvs_hgt, width=cnvs_wdt, color=colors[cnvs_clr])

# shape drawing loop
while True:
    shape = input("Enter shape[Square/Rectangle], type quit to exit: ")
    # user inputs to draw rectangle
    if shape.lower() == 'rectangle':
        # rectangle dimensions
        rect_x = int(input('Enter X coord for rectangle: '))
        rect_y = int(input('Enter Y coord for rectangle: '))
        rect_hgt = int(input('Enter rectangle height: '))
        rect_wdt = int(input('Enter rectangle width: '))
        # rectangle colors
        red = int(input('How red would you like?[0-255]: '))
        green = int(input('How green would you like?[0-255]: '))
        blue = int(input('How blue would you like?[0-255]: '))
        # create object to draw rectangle on the canvas
        rect = Rectangle(x=rect_x, y=rect_y, height=rect_hgt, width=rect_wdt, color=(red, green, blue))
        rect.draw_rectangle(test)
    # user inputs to draw square
    elif shape.lower() == 'square':
        # square dimensions
        sqr_x = int(input('Enter X coord for square: '))
        sqr_y = int(input('Enter Y coord for square: '))
        sqr_side = int(input('Enter side of the square: '))
        # square colors
        red = int(input('How red would you like?[0-255]: '))
        green = int(input('How green would you like?[0-255]: '))
        blue = int(input('How blue would you like?[0-255]: '))
        # create object to draw square on the canvas
        sqr = Square(x=sqr_x, y=sqr_y, side=sqr_side, color=(red, green, blue))
        sqr.draw_square(test)
    # exit
    elif shape.lower() == 'quit':
        break

# save image
test.create_canvas('image.png')