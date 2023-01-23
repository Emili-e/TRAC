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
    global new
    global info
    while True:
        try:
            infos = sockDraw.recvfrom(1024)
            #on rempli un tableau des informations importantes
            infoString = infos[0].decode().split(";") # x,y,angle,type,color
            
            angle_lock.acquire()
            #On remplit le dictionnaire
            info["x"] = float(infoString[0])
            info["y"] = float(infoString[1])
            info["angle"] = float(infoString[2])
            info["type"] = infoString[3]
            info["color"] = infoString[4]
            #On annonce la nouvelle trame
            new = 1;
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

#Dictionnaire qui se remplit quand une nouvlle trame arrive
info = {"x":0.0 , "y":0.0, "angle":0.0, "type" : " ", "color" : " "} 
#Boolean qui annonce l'arrivée de la trame
new = 0

while True:
    # Go to (x,y), but can't draw when moving
    draw.penup()
    draw.goto(info["x"], info["y"]) #go to (x,y)
    draw.pendown()
    
    # Draw the line 
    angle_lock.acquire()
    
    if new == 1 :
        draw.goto(x+cos(info["angle"])*distance, y+sin(info["angle"])*distance)
        x = x+cos(info["angle"])*distance
        y = y+sin(info["angle"])*distance
        new = 0
    
    angle_lock.release()    


    # Show the drawing
