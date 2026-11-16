from random import randint
import turtle

class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def is_rectangle(self, rectangle):
        if rectangle.left.x<self.x<rectangle.right.x and rectangle.left.y<self.y<rectangle.right.y:
            return True
        else:
            return False
    
    def calculate_distance(self, point):
        return ( (self.x-point.x) ** 0.5 + (self.y-point.y) ** 0.5 ) ** 0.5
    
class Rectangle:

    def __init__(self, left, right):
        self.left = left
        self.right = right
    
    def calculate_area(self):
        return (self.right.x-self.left.x) * (self.right.y-self.left.y)
    
    def calculate_perimeter(self):
        return ( 2*( (self.right.x-self.left.x) + (self.right.y-self.left.y)) )
    
class Draw_Rectangle(Rectangle):

    def draw(self,canvas):
        canvas.penup()
        canvas.goto(self.left.x, self.left.x)

        canvas.pendown()
        canvas.forward(self.right.x-self.left.x)
        canvas.left(90)
        canvas.forward(self.right.y-self.left.y)
        canvas.left(90)
        canvas.forward(self.right.x-self.left.x)
        canvas.left(90)
        canvas.forward(self.right.y-self.left.y)

class Rectangle_Points(Point):

    def draw(self,canvas, size=16, color='red'):
        canvas.penup()
        canvas.goto(self.x, self.y)
        canvas.pendown()
        canvas.dot(size,color)

# initial test call 
# pnt = Point(3, 5)
# print(pnt.is_rectangle((2, 4),(5, 7)))

# advance method call
rect = Draw_Rectangle(Point(randint(0, 0), randint(0, 50)), Point(randint(51, 125), randint(51, 125)))

print("Coordinates Left Side:", rect.left.x,",", rect.left.y)
print("Coordinates Right Side:", rect.right.x,",", rect.right.y)

points=Rectangle_Points(int(input("Enter X: ")), int(input("Enter Y: ")))

print('Your X and Y guess is inside rectangle:', points.is_rectangle(rect))

area=int(input("Guess the area: "))
print('You missed area by:', rect.calculate_area() - area)

perimeter=int(input("Guess the perimeter: "))
print('You missed perimeter by:', rect.calculate_perimeter() - perimeter)

trtl=turtle.Turtle()
rect.draw(canvas=trtl)
points.draw(canvas=trtl)
turtle.done()