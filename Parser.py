import os



motsClefs = {}
variableInt = {}
variableString = {}
variableFloat = {}
variableBool = {}

def findDecInt(mots):
    for mot in mots:
        if mot =='int':
            if mots[mots.index('int')+2] == '=':
                variableInt[mots[mots.index('int')+1]] = mots[mots.index('int') + 3]
            else:
                variableInt[mots[mots.index('int')+1]] = 0


f = open("code#.cs", "r")
chaine = f.read()

lignes = chaine.split('\n')
for ligne in lignes:
    mots = ligne.split(' ')

    mots = list(filter(None, mots))
    for mot in mots:
        if mot == '//':
            del mots[mots.index('//'):]
        findDecInt(mots)
print(variableInt)
