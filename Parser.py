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
variables = {'int' : [], 'string' : [], 'bool' : []}
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



# Function

# Add variables in dict:variables
def variableIdentifier(lexing):
    for i in range (len(lexing)):
        if ((lexing[i].type == "NAME") & (lexing[i].value in typekeywords)):
            if (lexing[i].value == "int"):
                addInVariables(lexing, i, "int", variables)
            if (lexing[i].value == "string"):
                addInVariables(lexing, i, "string", variables)
            if (lexing[i].value == "bool"):
                addInVariables(lexing, i, "bool", variables)


# Add variables in dict:variables following the type
def addInVariables(lexing, i, type, variables):
    if (len(lexing) > i+4 and type == 'int'):
        # int   a   =   3   ;
        if ((lexing[i+2].type == "ASSIGN") and (lexing[i+4].type == "SCOL")):
            setNoDouble("int", lexing[i+1].value, lexing[i+3].value)
            #variables["int"].append([lexing[i+1].value, lexing[i+3].value])
        # int   a   ;
        if (lexing[i+2].type == "SCOL"):
            setNoDouble("int",lexing[i+1].value, intUninitialized )
            #variables["int"].append([lexing[i+1].value, intUninitialized])
        # int   a   ,   b   ;
        else : 
            j = i+2
            while(lexing[j].type == "COM"):
                setNoDouble("int",lexing[j-1].value, intUninitialized )
                #variables["int"].append([lexing[j-1].value, intUninitialized])
                j = j + 2
            if (lexing[j].type == "SCOL"):
                setNoDouble("int",lexing[j-1].value, intUninitialized )
                #variables["int"].append([lexing[j-1].value, intUninitialized])

    if (type == 'string'):
        if ((len(lexing) > i+5)  and (lexing[i+2].type == "ASSIGN") and (lexing[i+3].type == "QUOT") and (lexing[i+5].type == "QUOT")):
            setNoDouble("string",lexing[i+1].value, lexing[i+4].value )
            #variables["string"].append([lexing[i+1].value, lexing[i+4].value])
        if ((len(lexing) > i+2) & (lexing[i+2].type == "SCOL")):
            setNoDouble("string",lexing[i+1].value, stringUninitialized )
            #variables["string"].append([lexing[i+1].value, stringUninitialized])
        else : 
            j = i+2
            while((len(lexing) > j ) and lexing[j].type == "COM"):
                setNoDouble("string",lexing[j-1].value, stringUninitialized )
                #variables["string"].append([lexing[j-1].value, stringUninitialized])
                j = j + 2
            if ((len(lexing) > j) and lexing[j].type == "SCOL"):
                setNoDouble("string",lexing[j-1].value, stringUninitialized )
                #variables["string"].append([lexing[j-1].value, stringUninitialized])

    if (type == 'bool'):
        if ((len(lexing) > i+4) and (lexing[i+2].type == "ASSIGN") and (lexing[i+4].type == "SCOL")):
            setNoDouble("bool",lexing[i+1].value, lexing[i+3].value)
            #variables["bool"].append([lexing[i+1].value, lexing[i+3].value])
        if ((len(lexing) > i+2) and lexing[i+2].type == "SCOL"):
            setNoDouble("bool",lexing[i+1].value, boolUninitialized)
            #variables["bool"].append([lexing[i+1].value, boolUninitialized])
        else : 
            j = i+2
            while((len(lexing) > j) and lexing[j].type == "COM"):
                setNoDouble("bool",lexing[j-1].value, boolUninitialized)
                #variables["bool"].append([lexing[j-1].value, boolUninitialized])
                j = j + 2
            if ((len(lexing) > j) and lexing[j].type == "SCOL"):
                setNoDouble("bool",lexing[j-1].value, boolUninitialized)
                #variables["bool"].append([lexing[j-1].value, boolUninitialized])


def setNoDouble(type, nomVar, value) :
    for list in variables[type] :
        #si d??j?? dans la liste
        if list[0] == nomVar :
            #si mauvaise valeur dans la liste
            if list[1] != value :
                variables[type][list][1] = value
            #si bonne valeur, on fait rien
            return
    #pas dans la liste
    else : 
        variables[type].append([nomVar, value])
        
        

# get drawing direction parameter
def GetDrawingDirection(name):
    # 1e lettre = direction : 360/value(lettre)
    if (name[0] == 'a'):
        direction = 0
    else:
        direction = 360/alphabet[name[0]]
    return direction


# get drawing x positional parameter
def GetDrawingX(name):
    if (name[-2] == 'a'):
        x = 0
    else:
        x = windowSize/alphabet[name[-2]]
    return x


# get drawing ys positional parameter
def GetDrawingY(name):
    if (name[-1] == 'a'):
        y = 0
    else:
        y = windowSize/alphabet[name[-1]] 
    return y
    

def IntDrawing(name, value):
    direction = GetDrawingDirection(name)
    x = GetDrawingX(name)
    y = GetDrawingY(name)
    # if (value == -1):

    # draw sinuso??de

def StringDrawing(name, value):
    direction = GetDrawingDirection(name)
    x = GetDrawingX(name)
    y = GetDrawingY(name)

    # mot = couleur
    # chiffre = ??paisseur
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

"""      
def main():
    variableIdentifier(lexing)
    print(variables)
    #IntDrawing(variables["int"][0][0], variables["int"][0][1])
    #StringDrawing(variables["string"][3][0], variables["string"][3][1])
main()"""