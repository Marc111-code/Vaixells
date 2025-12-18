def startBoard():
    return[['W','W','W','W','W'],['W','W','W','W','W'],['W','W','W','W','W'],['W','W','W','W','W'],['W','W','W','W','W']]
def showBoard(disposicioTaulell):
    x = ''
    for subllista in disposicioTaulell:
        for lletra in subllista:
            x = x + lletra
        print(x)   
        x = ''
def final(taulell_enfonsat):
    x = ''
    for subllista in taulell_enfonsat:
        for lletra in subllista:
            x = x + lletra
            if x == 'OOOOO':
                return True
        x = ''
    return False


def thereIsNoNumber(s):
    """
    aquesta funció retorna True si mínim un dels dos digits("a,4") és un digit ("qwertyuiopasdfghjklñzxcvbnm")
    si les dos posicions son digits, retornarà True,pro si els dos son numeros returnarà false
    """
    if s[0] in "123456789" and s[2] in "qwertyuiopasdfghjklñzxcvbnm":
        return True
    elif s[0] in "qwertyuiopasdfghjklñzxcvbnm" and s[2] in  "qwertyuiopasdfghjklñzxcvbnm":
        return True
    elif s[0] in "qwertyuiopasdfghjklñzxcvbnm" and s[2] in "123456789":
        return True
    else:
        return False


def someBoxOccupied(b,x,y,o):
    """
    b = taulell
    x:y posició que vols comprobar(de esquerra a dreta i de  dalt a baix)
    o = vertical o horitzontal
    retornar false si  algun lloc del taulell(x,y) en posició ques estigui vertical o 
    horitzontal(depen de o) es pugui posar un vaixell de 3 pos. Si no es pot retornarà
    True
    """
    try:
        b2 = b1[x]
        if o == "H":
            if b2[y] == "W":
                if b2[y + 1] == "W":
                    if b2[y + 2] == "W":
                        return False   
        elif o == "V":
            b2 = b1[y]
            if b2[x] == "W":
                if b2[x + 1] == "W":
                    if b2[x + 2] == "W":
                        return  False
    except:
        return True


def applyPlay(taulell,shoot):
    b = shoot.split(":")
    if taulell[int(b[0])][int(b[1])] == 'X' or taulell[int(b[0])][int(b[1])] == 'O':
        print("This box has already been played! You've missed a shot!")
        return taulell
    elif taulell[int(b[0])][int(b[1])] == 'S':
        print("IMPACT!")
        taulell[int(b[0])][int(b[1])] == 'O'
        return taulell
    elif taulell[int(b[0])][int(b[1])] == 'W':
        print("WATER!")
        taulell[int(b[0])][int(b[1])] == 'X'
        return taulell




def getOrientation():
    result = input("Would you like to place the boat vertically or horizontally? (v / h) ")
    while result not in "VvhH":
        print("Sorry, this is not a valid option.")
        result = input("Would you like to place the boat vertically or horizontally? (v / h) ")
    return result.upper()




def wrongPosition(pos):
    
    a = pos.split(':')
    
    if ((int(a[0]) <= 4 and int(a[0]) >=0) and (int(a[1]) <= 4 and int(a[1]) >=0)):
        return True
    else:
        return False

def getPosition():
    result = input("Initial box [row:column from 0 to 4]: ")
    
    while not wrongPosition(result):
        print("Sorry, this is not a valid position.")
        result = input("Initial box [row:column from 0 to 4]: ")
    return result

print(getPosition())







s'ha de fer
s'ha de arreglar per fer wl while

def someBoxOccupied(b,x,y,o):
    """
    b = taulell
    x:y posició que vols comprobar(de esquerra a dreta i de  dalt a baix)
    o = vertical o horitzontal
    retornar false si  algun lloc del taulell(x,y) en posició ques estigui vertical o 
    horitzontal(depen de o) es pugui posar un vaixell de 3 pos. Si no es pot retornarà
    True
    """
    try:
       
        
        if o == "H":
            print(b[x][y], b[x][y+1], b[x][y+2])
            if b[x][y+1] == "W" and b[x][y+2] == "W":
                
                return False
                
        elif o == "V":
             if b[x+1][y] == "W" and b[x+2][y] == "W":
               
                return False
    except:
        return True

def wrongPosition(pos):
    
    a = pos.split(':')
    
    if ((int(a[0]) <= 4 and int(a[0]) >=0) and (int(a[1]) <= 4 and int(a[1]) >=0)):
        return True
    else:
        return False
def placeShip3(taulell,i):
    variable =False
    print("Reading the 3 positions ship number " + str(i))
    result1 = input("Initial box [row:column from 0 to 4]: ")
    while variable != True:
        while not wrongPosition(result1):
            print("Would you like to place the boat vertically or horizontally? (v / h) ")
            result1 = input("Initial box [row:column from 0 to 4]: ")
        z = result1.split(":")  
        result2 = input("Would you like to place the boat vertically or horizontally? (v / h) ")
        while result2 not in "VvhH":
            print("Sorry, some of the positions where you want to place this ship is already occupied or does not exist. Try again")
            result2 = input("Would you like to place the boat vertically or horizontally? (v / h) ")        
        
        if someBoxOccupied(taulell,z[0],z[1],result2) == True:
            if result2 in "vV":
                taulell[int(z[0])][int(z[1])] = 'S' 
                taulell[int(z[0])+1][int(z[1])] = 'S' 
                taulell[int(z[0])+2][int(z[1])] = 'S' 
                print(taulell)
                variable = True
            elif result2 in "hH":
                taulell[int(z[0])][int(z[1])] = 'S' 
                taulell[int(z[0])][int(z[1])+1] = 'S' 
                taulell[int(z[0])][int(z[1])+2] = 'S'        
                print(taulell)
                variable = True                
        else:
            variable= False
            print(someBoxOccupied(taulell,z[0],z[1],result2))
            print("Sorry, some of the positions where you want to place this ship is already occupied or does not exist. Try again")
placeShip3([["W","W","W","W","W",],["W","W","W","W","W",],["W","W","W","W","W",],["W","W","W","W","W",],["W","W","W","W","W",]],1)
