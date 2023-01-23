import turtle
import sys
import socket
from math import cos, sin
import threading

# Creation d'une socket
sockDraw = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sockDraw.bind(("127.0.0.1", 1111))

# Mise en place de la fenêtre Graphique
turtle.setup(width=1200, height=600)
turtle.title("Live Coding Graphics")
turtle.bgcolor("black")
# Create the turtle
draw = turtle.Turtle()

angle_lock = threading.Lock()

def Listen():
    global angle
    global typeT
    while True:
        try:
            infos = sockDraw.recvfrom(1024)
            info = infos[0].decode().split(";") # x,y,angle,type,color

            typeT = info[3]
            angle_lock.acquire()
            angle = float(info[2])
            angle_lock.release() 

               
        except socket.error:
            print("socket error")
            sys.exit()
            

# create and start the new thread
t1 = threading.Thread(target=Listen)
t1.start()



draw.hideturtle()
draw.pencolor("red")
draw.pensize(8)
x = 100
y = 100
distance = 30

angle = 0
angle_vieux = 0

typeT = ""



while True:
    # Go to (x,y), but can't draw when moving
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


    # Show the drawing
