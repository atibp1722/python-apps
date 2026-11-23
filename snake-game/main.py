# import libraries for game
import pygame, time, random, math
from pygame.locals import *
# game screen dimensions
screen_width_height = 1200, 1200
# fps for game loop
fps = 60.0
# speed counter
moving_speed = 1
# frame to delay for game
frames_to_delay = 3
# color of food and snake
food_color = pygame.Color(255, 0, 0)
snake_color = pygame.Color(0, 255, 0)
# cell size
block_size = 50

# class for single game block
class Block:
    # constructor for block properties
    def __init__(self):
        self.color = pygame.color(255, 0, 0)
        self.square_size = block_size
        self.pos = [0, 0]
    # create block on game screen
    def draw(self):
        rect = Rect(self.pos[0], self.pos[1], block_size, block_size)
        screen.fill(self.color, rect)

# class for snake body segment
class BodySegment:
    # constructor with position
    def __init__(self, pos):
        Block.__init__(self)
        self.color = pygame.Color(200, 200, 200)
        self.pos = pos
    # method to move to new position    
    def move(self, newPos):
        # update position
        self.pos = newPos

# class for wall segment inherit from Block
class WallSegment(Block):
    # same constrcutor as body segment class
    def __init__(self, pos):
        Block.__init__(self)
        self.color = pygame.Color(200, 200, 200)
        self.pos = pos

# class for sanke food
# inherits from block
class Food(Block):
    # constructor with food properties
    def __init__(self):
        Block.__init__(self)
        self.color = pygame.Color(255, 0, 0)
        self.randomize()
    # random position in game screen    
    def randomize(self):
        for i, widthOrHeight in enumerate(self.pos):
            self.pos[i] = random.choice(range(block_size, screen_width_height[0] - block_size, block_size))

# class to make multiple body segments chainable to one
class Chainable:
    # method to draw all segments on game screen
    def draw(self, screen):
        for seg in self.segments:
            seg.draw(screen)

# class to create chainable sequances to create game wall
class Wall(Chainable):
    # constructor to build 4 wall borders
    def __init__(self):
        self.segments = []
        # draw top and horizontal rows
        for x in range(0, screen_width_height[0], block_size):
            # top wall border
            self.segments.append( WallSegment([x, 0]) )
            # bottom wall border
            self.segments.append( WallSegment([x, screen_width_height[1] - block_size]) )
        for y in range(0, screen_width_height[1] - block_size, block_size):
            # left wall border
            self.segments.append( WallSegment([0, y]) )
            # top wall border
            self.segments.append( WallSegment([screen_width_height[1] - block_size, y]) )
    # method to check whether snake head collides with wall
    def checkWallCollison(self, snake):
        # boundary of snake head
        rect1 = Rect(snake.head.pos[0], snake.head.pos[1], block_size, block_size)
        # check collision at all borders
        for seg in self.segments:
            # boundary of current border
            rect2 = Rect(seg.pos[0], seg.pos[1], block_size, block_size)
            # check overlap between head and border
            if (checkCollison(rect1, rect2)):
                return True
        return False

# class to create a chainable snake
class Snake(Chainable):
    # consructor to initialize snake
    def __init__(self):
        # intial snake properties
        self.direction = "right"
        self.moveDist = block_size * moving_speed
        self.segments = []
        self.size = 0
        # check snake segment
        for i in range(2):
            if i == 0:
                # first segment is head
                self.segments.append( BodySegment([block_size, 200]) )
                self.head = self.segments[0]
            # second segment behind head becomes body
            else:
                self.segments.append( BodySegment([0, 200]) )
    # update snake direction
    def changeDirection(self, direction):
        # prevent right -> left turn
        if (self.direction == "right" and direction == "left"):
            pass
        # prevent left -> right turn
        if (self.direction == "left" and direction == "right"):
            pass
        # prevent up -> left down
        if (self.direction == "up" and direction == "down"):
            pass
        # prevent down -> up turn
        if (self.direction == "down" and direction == "up"):
            pass
        # update direction
        else:
            self.direction = direction
    # check snake head collide with tail
    def checkTailCollison(self):
        # iterate and move to next segment 
        for i, seg in enumerate(self.segments):
            if i == 0:
                continue
            # bind head
            rect1 = Rect(self.head.pos[0], self.head.pos[1], block_size, block_size)
            # bind snake body
            rect2 = Rect(seg.pos[0], seg.pos[1], block_size, block_size)
            # check whether head and body are in same coordinates
            if (checkCollison(rect1, rect2)):
                return True
        return False
    # method to move the snake
    def move(self):
        # snake current length
        segmentsLen = len(self.segments)
        # head position reference
        head = self.segments[0]
        # new head position
        newHeadPos = []
        # move up decrease position in y
        if (self.direction == "up"):
            newHeadPos = [head.pos[0], head.pos[1] - self.moveDist]
        # move down increase y
        if (self.direction == "down"):
            newHeadPos = [head.pos[0], head.pos[1] + self.moveDist]
        # move left decrease x
        if (self.direction == "left"):
            newHeadPos = [head.pos[0] - self.moveDist, head.pos[1]]
        else:
            newHeadPos = [head.pos[0] + self.moveDist, head.pos[1]]
        # save last segment position
        self.tailLastPos = self.segments[segmentsLen - 1].pos
        # set position of each segment to next
        for i in range(segmentsLen - 1, 0, -1):
            self.segments[1].move( self.segments[i - 1].pos )
        # move head to new position
        self.segments[0].move( newHeadPos )
    # grow snake by adding new segment
    def addNewSegment(self):
        # append new segment to tail
        self.segments.append( BodySegment(self.tailLastPos) )
        # increase snake size
        self.size += 1

# function to check whether 2 rectangle overlap
def checkCollison(rect1, rect2):
    # check for exact coordinates match
    if (rect1.x == rect2.x and rect1.y == rect2.y):
        return True
    else:
        return False