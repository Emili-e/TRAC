import turtle
import sys
import socket
from math import *
import threading

# Création d'une socket
sockDraw = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sockDraw.bind(("127.0.0.1", 1111))

# Mise en place de la fenêtre graphique
turtle.setup(width=1000, height=650)
turtle.setworldcoordinates(0, 0, 1000, 650)
turtle.title("Live Coding Graphics")
turtle.bgcolor("black")
# Create the turtle
draw = turtle.Turtle()
# "mutex"
angle_lock = threading.Lock()

def Listen():
    global angle
    global typeT
    global new
    global info
    while True:
        try:
            # On attend de recevoir quelque chose
            infos = sockDraw.recvfrom(1024)
            #on rempli un tableau des informations importantes
            infoString = infos[0].decode().split(";") # x,y,angle,type,color,thick,value
            
            angle_lock.acquire()
            # On remplit le dictionnaire
            info["x"] = float(infoString[0])
            info["y"] = float(infoString[1])
            info["angle"] = float(infoString[2])
            info["type"] = infoString[3]
            info["color"] = infoString[4]
            info["thick"] = float(infoString[5])
            if (info["type"] == "int" or info["type"] == "bool") :
                info["value"] = int(infoString[6])
                
            #On annonce la nouvelle trame
            new = 1;
            angle_lock.release() 
        
        except socket.error:
            print("socket error")
            sys.exit()
            

# create and start the new thread
t1 = threading.Thread(target=Listen)
t1.start()


# Dessine la sinusoide correspondant à un int
def drawSinusoide() :
    # draw.pensize(3)
    draw.pencolor("LimeGreen")
    draw.pendown()
    for x in range(floor(info["x"]), floor(info["x"]+300)) :
        if x == floor(info["x"]) :
            draw.penup()
            draw.goto(x + cos(info["angle"])*distance, sin(radians(x)*2*pi*(1/(info["value"]+1)))*distance + info["y"])
            draw.pendown()
            
        y = sin(radians(x)*2*pi*(1/info["value"]))*distance + info["y"]
        x2 = x + cos(info["angle"])*distance 
        draw.goto(x2,y)
        

# Dessine le trait correspondant à une string
def drawLine():
    distance = 300
    draw.goto(info["x"], info["y"]) # go to (x,y)
    draw.pendown()
    draw.speed(5)
    draw.pencolor(info["color"])
    draw.goto(info["x"]+cos(info["angle"]*(pi/180))*distance, info["y"]+sin(info["angle"]*(pi/180))*distance)


# Dessine un zigzag de gauche à droite /\/
def drawZigZagTrue():
    draw.pencolor("DarkOrchid")
    x1, y1 = info["x"], info["y"]
    dx, dy = cos(info["angle"]*(pi/180))*distance, sin(info["angle"]*(pi/180))*distance
    x2, y2 = info["x"] + dx, info["y"] + dy
    draw.speed(5)

    for i in range(1, 10):
        
        draw.goto(x1, y1)
        draw.pendown()
        draw.pensize(info["thick"]*1.5)
        

        draw.goto(x2, y2)

        x1, x2 = x1 + 2*dx, x2 + 2*dx

        #draw.goto(x1, y1)
        #draw.goto(x2, y2)


# Dessine un zigzag de droite à gauche /\/
def drawZigZagFalse():
    draw.pencolor("DarkOrchid")
    x1, y1 = info["y"], info["x"]
    dx, dy = distance*sin(info["angle"]*(pi/180)), distance*cos(info["angle"]*(pi/180))
    x2, y2 = info["y"] + dy, info["x"] + dx

    for i in range(1, 10):
        draw.goto(x1, y1)
        draw.pendown()
        draw.pensize(info["thick"]*1.5)
        #draw.speed(1)

        draw.goto(x2, y2)

        y1, y2 = y1 + 2*dy, y2 + 2*dy

        draw.goto(x1, y1)
        draw.goto(x2, y2)

# masque la tortue
draw.hideturtle()
draw.speed(8)
distance = 30

# Dictionnaire qui se remplit quand une nouvlle trame arrive
info = {"x":0.0 , "y":0.0, "angle":0.0, "type" : " ", "color" : " ", "value":1,  "thick" : 0.0} 
# Boolean qui annonce l'arrivée de la trame
new = 0

while True:
    # Go to (x,y), but can't draw when moving
    draw.penup()
    draw.speed(0)
    draw.goto(info["x"], info["y"]) # go to (x,y)
    
    # Draw the line 
    angle_lock.acquire()
    
    if new == 1 :
        if info["color"] != "reset" :
            draw.pencolor(info["color"])
        draw.pensize(info["thick"]*1.5)
       
        if info["type"] == "int" :
            drawSinusoide()
        elif info["type"] == "string":
            if info["color"] == "reset" :
                draw.clear()
            else : 
                draw.pensize(info["thick"]*1.5)
                drawLine()
        elif info["type"] == "bool" :
            if (info["value"] == 1):
                drawZigZagTrue()
            else :
                drawZigZagFalse()

        new = 0
    
    angle_lock.release()    