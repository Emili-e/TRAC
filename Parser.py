#import lexer

# Import data
"""
f = open("code#.cs", "r")
data = f.read()
"""
# Build lexer
#lexing = lexer.lexing(data)
# print(lexing)


# Variables ------------------------------------------------------------------------- #

typekeywords = {'int','string', 'bool'}
variables = {'int' : [], 'string' : [], 'bool' : []}
alphabet = {'a' : 0, 'b' : 1, 'c' : 2, 'd' : 3, 'e' : 4, 'f' : 5, 'g' : 6, 'h' : 7, 'i' : 8, 'j' : 9,
            'k' : 10, 'l' : 11, 'm' : 12, 'n' : 13, 'o' : 14, 'p' : 15, 'q' : 16, 'r' : 17, 's' : 18,
            't' : 19, 'u' : 20, 'v' : 21, 'w' : 22, 'x' : 23, 'y' : 24, 'z' : 25, 
            'A' : 0, 'B' : 1, 'C' : 2, 'D' : 3, 'E' : 4, 'F' : 5, 'G' : 6, 'H' : 7, 'I' : 8, 'J' : 9,
            'K' : 10, 'L' : 11, 'M' : 12, 'N' : 13, 'O' : 14, 'P' : 15, 'Q' : 16, 'R' : 17, 'S' : 18,
            'T' : 19, 'U' : 20, 'V' : 21, 'W' : 22, 'X' : 23, 'Y' : 24, 'Z' : 25}

# Valeurs par défaut des variables
intUninitialized = -1
stringUninitialized = ""
boolUninitialized = False


# Fonctions ------------------------------------------------------------------------- #

# Fonction qui prend en entrée le résultat du lexing et une socket
# et qui renvoie le dict:variables
# Identifie la déclaration de variables
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


# Fonction qui prend en entrée le résultat du lexing, la position, le type de la variable,
# le dict:variables et une socket
# Ajoute les variables au dict:variables selon les types
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


# Fonction qui prend en entrée le type, le nom, la valeur de la variable,
# le dict:variables et une socket
# Ajoute les variables au dict:variables sans doublons
def setNoDouble(type, nomVar, value, variables, socket) :
    for list in variables[type] :
        # si déjà dans la liste
        if list[0] == nomVar :
            # si mauvaise valeur dans la liste
            if list[1] != value :
                list[1] = value
                value = convertBoolInt(type, value)
                socket.sendto(infos.encode(), ("127.0.0.1", 1111))
            # si bonne valeur, on fait rien
            return
    # pas dans la liste
    variables[type].append([nomVar, value])
    value = convertBoolInt(type, value)
    infos = getDrawingInfo(nomVar, type, value)
    socket.sendto(infos.encode(), ("127.0.0.1", 1111))
        

# Fonction qui prend en entrée le nom de la variable, son type et sa valeur
# et qui renvoie un dictionnaire contenant x, y, angle, type, couleur
# Récupère les informations nécessaires au tracé
def getDrawingInfo(name, type, value) :
    x = GetDrawingX(name)
    y = GetDrawingY(name)
    angle = GetDrawingAngle(name)
    color = GetDrawingColor(value, type)
    thick = GetDrawingThickness(value, type)
    return f"{x};{y};{angle};{type};{color};{thick};{value}"


# Fonction qui prend en entrée le nom de la variable
# et qui renvoie un entier donnant la coordonnée en x
# Récupère la coordonnée x de la position initiale
# par défaut = 0
def GetDrawingX(name):
    x = (1200/25)*alphabet[name[-2]]
    return x


# Fonction qui prend en entrée le nom de la variable
# et qui renvoie un entier donnant la coordonnée en y
# Récupère la coordonnée y de la position initiale
# par défaut = 0
def GetDrawingY(name):
    y = (600/25)*alphabet[name[-1]]
    return y


# Fonction qui prend en entrée le nom de la variable
# et qui renvoie un entier correspondant à l'angle par rapport à l'horizontale
# Récupère l'angle par rapport à l'horizontale
def GetDrawingAngle(name):
    angle = 15*alphabet[name[0]]
    return angle


# Fonction qui prend en entrée la valeur de la variable
# et qui renvoie une string correspondant à la couleur  et le type de la variable
# Récupère la couleur
# par défaut = black
def GetDrawingColor(value, type):
    color = "white"
    if (type == "string"):
        index = 0
        while (value[index] in alphabet):
            index += 1
            color = value[0:index]
    return color

# Fonction qui prend en entrée la valeur de la variable et le type de la variable
# et qui renvoie un entier correspondant à l'épaisseur
# Récupère l'épaisseur (0 à 9)
# par défaut = 1
def GetDrawingThickness(value, type):
    thick = 3
    if (type == "string"):
        thick = int(value[-1])
    return thick


# Fonction qui prend en entrée le type et la valeur d'une variable
# et qui renvoie un entier correspondant à la valeur booléenne
# Convertir False en 0 et True en 1
def convertBoolInt(type, value):
    if (type == "bool"):
        if (value == False):
            value = 0
        else:
            value = 1
    return value

'''
def IntDrawing(name, value):
    direction = GetDrawingDirection(name)
    x = GetDrawingX(name)
    y = GetDrawingY(name)
    # if (value == -1):

    # draw sinusoïde
    
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
