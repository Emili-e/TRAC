import os
import random


motsClefsVariables = {'int','float','double', 'Vector2','Texture2D'}
variables = {}
weAreInIf = False

def findNewVariable(mots):
    for mot in mots:
        if mot in motsClefsVariables:
            if mots[mots.index(mot)+2] == '=' and mots[mots.index(mot)+3] != 'new':
                variables[mots[mots.index(mot)+1]] = mots[mots.index(mot) + 3]
            elif mots[mots.index(mot)+2] == '=' and mots[mots.index(mot)+3] == 'new':
                variables[mots[mots.index(mot)+1]] = random.randrange(100)
            else:
                variables[mots[mots.index(mot)+1]] = 0


print(variables)
