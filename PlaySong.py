import sys
import socket
from math import *
import threading
import mido
import random
import time

nbParamWind = 1
nbParamRain = 1
nbParamBubble = 5
nbParamBell = 4
nbParamFlute = 4

borneMidi = (10,110)

# Création d'une socket
sockSong = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sockSong.bind(("127.0.0.1", 1112))

angle_lock = threading.Lock()

def initSong():
    for i in range(100):
        outPortMidi.send(mido.Message('control_change',control=i, value=0))
    
    outPortMidi.send(mido.Message('control_change',control=23, value=1))

    for i in range(nbParamBell):
        value = random.randint(borneMidi[0], borneMidi[1])
        outPortMidi.send(mido.Message('control_change',control=i+2, value=value))
 


def Listen():
    global angle
    global typeT
    global new
    global info
    while True:
        try:
            # On attend de recevoir quelque chose
            infos = sockSong.recvfrom(1024)
            #on rempli un tableau des informations importantes
            infoString = infos[0].decode().split(";") # x,y,angle,type,color,thick,value

            angle_lock.acquire()
            # On remplit le dictionnaire
            info["type"] = infoString[0]
            info["scol"] = bool(infoString[1])

            #On annonce la nouvelle trame
            new = 1
            angle_lock.release() 
        
        except socket.error:
            print("socket error")
            sys.exit()

# bubble      
def playBubble():
    while True:
        wait = random.randint(2,15)
        numParam = random.randint(0,nbParamBubble)
        value = random.randint(borneMidi[0], borneMidi[1])

        time.sleep(wait)
        outPortMidi.send(mido.Message('control_change',control=numParam+12, value=value))
        outPortMidi.send(mido.Message('control_change',control=11, value=0))
        outPortMidi.send(mido.Message('control_change',control=11, value=127))
  
# create and start the new thread
t1 = threading.Thread(target=Listen)
t1.start()
t2 = threading.Thread(target=playBubble)
t2.start()

# wind
def playInt() :
    value = random.randint(borneMidi[0], borneMidi[1])
    outPortMidi.send(mido.Message('control_change',control=32, value=value))

        

# flute
def playString():
    numParam = random.randint(0,nbParamFlute)
    value = random.randint(borneMidi[0], borneMidi[1])
    outPortMidi.send(mido.Message('control_change',control=numParam+42, value=value))


# rain
def playBool():
    numParam = random.randint(0,nbParamFlute)
    value = random.randint(borneMidi[0], borneMidi[1])
    outPortMidi.send(mido.Message('control_change',control=numParam+22, value=value))
# bell
def playScol():
    outPortMidi.send(mido.Message('control_change',control=1, value=0))
    outPortMidi.send(mido.Message('control_change',control=1, value=127))




# Dictionnaire qui se remplit quand une nouvlle trame arrive

info = { "type" : " ", "scol" : False} 
# Boolean qui annonce l'arrivée de la trame
new = 0
portsMidi = mido.get_output_names()
outPortMidi = mido.open_output(portsMidi[1])
initSong()
while True:

    angle_lock.acquire()
    
    if new == 1 :
        if info["type"] == "int" :
            playInt()
        elif info["type"] == "string":
            playString()
        elif info["type"] == "bool" :
            playBool()

        if info["scol"] == True:
            playScol()
            
        new = 0
        print(info)

    
    angle_lock.release()    