from random import randint
import turtle

# class to initialize a point
class Point:
    # point coordinates
    def __init__(self, x, y):
        self.x = x
        self.y = y
    # check whether point is inside rectangle
    def is_rectangle(self, rectangle):
        # point coordinates fall between rectangle's right and left
        if rectangle.left.x<self.x<rectangle.right.x and rectangle.left.y<self.y<rectangle.right.y:
            return True
        else:
            return False
    # distance between points
    def calculate_distance(self, point):
        return ( (self.x-point.x) ** 2 + (self.y-point.y) ** 2 ) ** 0.5

# class for rectangle    
class Rectangle:
    # rectangle left and right properties
    def __init__(self, left, right):
        self.left = left
        self.right = right
    # rectangle area calculation
    def calculate_area(self):
        return (self.right.x-self.left.x) * (self.right.y-self.left.y)
    # rectangle perimeter calculation
    def calculate_perimeter(self):
        return ( 2*( (self.right.x-self.left.x) + (self.right.y-self.left.y)) )

# draw inherited rectangle   
class Draw_Rectangle(Rectangle):
    # canvas for rectangle
    def draw(self, canvas):
        canvas.penup()
        canvas.goto(self.left.x, self.left.y)
        # draw rectabgle in bottom, right, top, left directions
        canvas.pendown()
        canvas.forward(self.right.x-self.left.x)
        # 90 degree left turn
        canvas.left(90)
        canvas.forward(self.right.y-self.left.y)
        # 90 degree left turn
        canvas.left(90)
        canvas.forward(self.right.x-self.left.x)
        # 90 degree left turn
        canvas.left(90)
        canvas.forward(self.right.y-self.left.y)

# class to draw user guessed dot by inheriting from points
class Rectangle_Points(Point):
    # move to coordinates
    def draw(self,canvas, size=16, color='red'):
        canvas.penup()
        canvas.goto(self.x, self.y)
        canvas.pendown()
        canvas.dot(size,color)

# initial test call 
# pnt = Point(3, 5)
# print(pnt.is_rectangle((2, 4),(5, 7)))

# advance method call
# draw random rectangle with random coordinates
rect = Draw_Rectangle(Point(randint(0, 0), randint(0, 50)), Point(randint(51, 125), randint(51, 125)))

# print cooridnates on console terminal
print("Coordinates Left Side:", rect.left.x,",", rect.left.y)
print("Coordinates Right Side:", rect.right.x,",", rect.right.y)

# prompt user for X, Y coordinates
points = Rectangle_Points(int(input("Enter X: ")), int(input("Enter Y: ")))
# check user guess inside random rectangle
print('Your X and Y guess is inside rectangle:', points.is_rectangle(rect))

# prompt user to guess area and calculate difference
area=int(input("Guess the area: "))
print('You missed area by:', rect.calculate_area() - area)

# prompt user to guess permieter and calculate difference
perimeter=int(input("Guess the perimeter: "))
print('You missed perimeter by:', rect.calculate_perimeter() - perimeter)

# intialize turtle to draw rectagle and user guessed dot
trtl=turtle.Turtle()
rect.draw(canvas=trtl)
points.draw(canvas=trtl)
turtle.done()