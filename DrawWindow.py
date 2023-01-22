import turtle
import sys
import socket
from math import cos, sin
import threading

# Create the turtle
sockDraw = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sockDraw.bind(("127.0.0.1", 1111))


angle = 0
angle_vieux = angle
angle_lock = threading.Lock()

turtle.setup(width=300, height=300, startx=None, starty=None)

draw = turtle.Turtle()


draw.hideturtle()
draw.pencolor("red")
draw.pensize(2)
x = 300
y = 300
distance = 30

def Listen():
    global angle
    while True:
        try:
            instr= sockDraw.recvfrom(1024)
            print(instr)
            angle_lock.acquire()
            angle = int(instr[0])
            angle_lock.release()    
        except socket.error:
            print("socket error")
            sys.exit()



t1 = threading.Thread(target=Listen)

# start the new thread
t1.start()

while True:
    draw.penup()
    draw.goto(x, y)
    draw.pendown()
    # Draw the line 
    angle_lock.acquire()
    if angle_vieux != angle:
        draw.goto(x+cos(angle)*distance, y+sin(angle)*distance)
        x = x+cos(angle)*distance
        y = y+sin(angle)*distance
        angle_vieux = angle
    angle_lock.release()    

#turtle.done()

    # Show the drawing
