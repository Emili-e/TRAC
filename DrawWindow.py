import turtle
import sys
import socket
from math import cos, sin
import threading

# Create the turtle
sockDraw = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sockDraw.bind(("127.0.0.1", 1111))

# Mise en place de la fenêtre Graphique
turtle.setup(width=1.0, height=1.0)
turtle.title("Live Coding Graphics")
turtle.bgcolor("black")
draw = turtle.Turtle()


def Listen():
    global angle
    global typeT
    while True:
        try:
            typee = sockDraw.recvfrom(1024)
            instr = sockDraw.recvfrom(1024)
            typeT = typee
            """
            if typee[0] == "clear" :
                turtle.clear()
                """
            if typee[0] == "int" :
                angle_lock.acquire()
                angle = int(instr[0])
                angle_lock.release() 
            elif typee[0] == "string" :
                angle_lock.acquire()
                angle = angle - 3
                angle_lock.release() 
            else :
                angle_lock.acquire()
                angle = angle - 5
                angle_lock.release() 
               
        except socket.error:
            print("socket error")
            sys.exit()
            
angle_lock = threading.Lock()
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
        
        if typeT == "string" :
            draw.goto(x+distance, y+distance)
            x = x+distance
            y = y+distance
            
        elif typeT == "bool" :
            x = x+distance
            y = y+distance
            draw.goto(x+cos(45)*distance, y+sin(45)*distance)
            x = x+cos(45)*distance
            y = y+sin(45)*distance
            
        else : 
            draw.goto(x+cos(angle)*distance, y+sin(angle)*distance)
            x = x+cos(angle)*distance
            y = y+sin(angle)*distance
        angle_vieux = angle
    angle_lock.release()    


    # Show the drawing
