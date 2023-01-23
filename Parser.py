#import lexer

# Import data
"""
f = open("code#.cs", "r")
data = f.read()
"""
# Build lexer
#lexing = lexer.lexing(data)
# print(lexing)


# Variables
typekeywords = {'int','string', 'bool'}
intUninitialized = -1
stringUninitialized = ""
boolUninitialized = False

alphabet = {'a' : 0, 'b' : 1, 'c' : 2, 'd' : 3, 'e' : 4, 'f' : 5, 'g' : 6, 'h' : 7, 'i' : 8, 'j' : 9,
            'k' : 10, 'l' : 11, 'm' : 12, 'n' : 13, 'o' : 14, 'p' : 15, 'q' : 16, 'r' : 17, 's' : 18,
            't' : 19, 'u' : 20, 'v' : 21, 'w' : 22, 'x' : 23, 'y' : 24, 'z' : 25}
windowSize = 750
TrueFrequency = 1 
FalseFrequency = 0
thickness = [k for k in range(5)]
variables = {'int' : [], 'string' : [], 'bool' : []}



# Function

# Add variables in dict:variables
def variableIdentifier(lexing, socket):
    for i in range (len(lexing)):
        if ((lexing[i].type == "NAME") & (lexing[i].value in typekeywords)):
            if (lexing[i].value == "int"):
                addInVariables(lexing, i, "int", variables, socket)
            if (lexing[i].value == "string"):
                addInVariables(lexing, i, "string", variables, socket)
            if (lexing[i].value == "bool"):
                addInVariables(lexing, i, "bool", variables, socket)
    return variables


# Add variables in dict:variables following the type
def addInVariables(lexing, i, type, variables, socket):
    if (type == 'int'):
        # int   a   =   3   ;
        if (len(lexing) > i+4 and (lexing[i+2].type == "ASSIGN") and (lexing[i+4].type == "SCOL")):
            setNoDouble("int", lexing[i+1].value, lexing[i+3].value, variables, socket)
        # int   a   ;
        if (len(lexing) > i+2 and lexing[i+2].type == "SCOL"):
            setNoDouble("int",lexing[i+1].value, intUninitialized, variables, socket )
        # int   a   ,   b   ;
        elif len(lexing) > i+2 : 
            j = i+2
            while(lexing[j].type == "COM"):
                setNoDouble("int",lexing[j-1].value, intUninitialized, variables, socket )
                j = j + 2
            if (lexing[j].type == "SCOL"):
                setNoDouble("int",lexing[j-1].value, intUninitialized, variables, socket )
    # string sans " "
    if (type == 'string'):
        if ((len(lexing) > i+4)  and (lexing[i+2].type == "ASSIGN") and (lexing[i+4].type == "SCOL")): #and (lexing[i+3].type == "NAME") 
            setNoDouble("string",lexing[i+1].value, lexing[i+3].value, variables, socket )
        if ((len(lexing) > i+2) and (lexing[i+2].type == "SCOL")):
            setNoDouble("string",lexing[i+1].value, stringUninitialized, variables, socket )
        else : 
            j=i+2
            while((len(lexing) > j ) and lexing[j].type == "COM"):
                setNoDouble("string",lexing[j-1].value, stringUninitialized , variables, socket )
                j = j + 2
            if ((len(lexing) > j) and lexing[j].type == "SCOL"):
                setNoDouble("string",lexing[j-1].value, stringUninitialized, variables, socket )
    if (type == 'bool'):
        if ((len(lexing) > i+4) and (lexing[i+2].type == "ASSIGN") and (lexing[i+4].type == "SCOL")):
            setNoDouble("bool",lexing[i+1].value, lexing[i+3].value, variables, socket)
        if ((len(lexing) > i+2) and lexing[i+2].type == "SCOL"):
            setNoDouble("bool",lexing[i+1].value, boolUninitialized, variables, socket)
        else : 
            j = i+2
            while((len(lexing) > j) and lexing[j].type == "COM"):
                setNoDouble("bool",lexing[j-1].value, boolUninitialized, variables, socket)
                j = j + 2
            if ((len(lexing) > j) and lexing[j].type == "SCOL"):
                setNoDouble("bool",lexing[j-1].value, boolUninitialized, variables, socket)


def setNoDouble(type, nomVar, value, variables, socket) :
    for list in variables[type] :
        #si déjà dans la liste
        if list[0] == nomVar :
            #si mauvaise valeur dans la liste
            if list[1] != value :
                list[1] = value
                socket.sendto(str(type).encode(), ("127.0.0.1", 1111))
                socket.sendto(str(value).encode(), ("127.0.0.1", 1111))
            #si bonne valeur, on fait rien
            return
    #pas dans la liste
    variables[type].append([nomVar, value])
    socket.sendto(str(type).encode(), ("127.0.0.1", 1111))
    socket.sendto(str(value).encode(), ("127.0.0.1", 1111))
        

# Fonction qui prend en entrée le nom de la variable
# et qui renvoie un entier donnant la coordonnée en x
# Récupère la coordonnée x de la position initiale
# par défaut = 0
def GetDrawingX(name):
    if (name[-2] == 'a'):
        x = 0
    else:
        x = windowSize/alphabet[name[-2]]
    return x


# Fonction qui prend en entrée le nom de la variable
# et qui renvoie un entier donnant la coordonnée en y
# Récupère la coordonnée y de la position initiale
# par défaut = 0
def GetDrawingY(name):
    if (name[-1] == 'a'):
        y = 0
    else:
        y = windowSize/alphabet[name[-1]] 
    return y


# Fonction qui prend en entrée le nom de la variable
# et qui renvoie un entier correspondant à l'angle par rapport à l'horizontale
# Récupère l'angle par rapport à l'horizontale
def GetDrawingAnlge(name):
    # 1e lettre = direction : 360/value(lettre)
    if (name[0] == 'a'):
        angle = 0
    else:
        angle = 360/alphabet[name[0]]
    return angle


# Fonction qui prend en entrée la valeur de la variable
# et qui renvoie une string correspondant à la couleur
# Récupère la couleur
# par défaut = black
def GetDrawingColor(value):
    index = 0
    while (value[index] in alphabet):
        index += 1
    color = value[0:index]
    if (color == ""):
        color = "black"
    return color

'''
def IntDrawing(name, value):
    direction = GetDrawingDirection(name)
    x = GetDrawingX(name)
    y = GetDrawingY(name)
    # if (value == -1):

    # draw sinusoïde

def StringDrawing(name, value):
    direction = GetDrawingDirection(name)
    x = GetDrawingX(name)
    y = GetDrawingY(name)

    # mot = couleur
    # chiffre = épaisseur
    if (int(value[-1]) in thickness):
        number = int(value[-1])
        color = value[0:-1]
        print(color, number)
    
    # draw
    
def BoolDrawing(name, value):
    direction = GetDrawingDirection(name)
    x = GetDrawingX(name)
    y = GetDrawingY(name)

    if (value == True):
        f = TrueFrequency
    else:
        f = FalseFrequency
        
    # draw zigzag
   
def main():
    variableIdentifier(lexing)
    print(variables)
    #IntDrawing(variables["int"][0][0], variables["int"][0][1])
    #StringDrawing(variables["string"][3][0], variables["string"][3][1])
main()
'''