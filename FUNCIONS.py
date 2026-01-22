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




def placeShip3(tauler, i):
    colocat = False
    while not colocat:
        print(f"Reading the 3 positions ship number {i}")
        entrada = input("Initial box [row:column from 0 to 4]: ")
        fila = int(entrada.split(':')[0])
        columna = int(entrada.split(':')[1])
        orientacio =input("Would you like to place the boat vertically or horizontally? (v / h): ")
        if orientacio == 'v':
            if fila >= 0 and fila <= 2 and columna >= 0 and columna <= 4:
                if tauler[fila][columna] == 'W' and tauler[fila+1][columna] == 'W' and tauler[fila+2][columna] == 'W':
                    tauler[fila][columna] = 'S'
                    tauler[fila+1][columna] = 'S'
                    tauler[fila+2][columna] = 'S'
                    colocat = True
                else:
                    print("Sorry, some of the positions where you want to place this ship is already occupied or does not exist. Try again!")
            else:
                print("Sorry, some of the positions where you want to place this ship is already occupied or does not exist. Try again!")
        
        elif orientacio == 'h':
            if fila >= 0 and fila <= 4 and columna >= 0 and columna <= 2:
                if tauler[fila][columna] == 'W' and tauler[fila][columna+1] == 'W' and tauler[fila][columna+2] == 'W':
                    tauler[fila][columna] = 'S'
                    tauler[fila][columna+1] = 'S'
                    tauler[fila][columna+2] = 'S'
                    colocat = True
                else:
                    print("Sorry, some of the positions where you want to place this ship is already occupied or does not exist. Try again!")
            else:
                print("Sorry, some of the positions where you want to place this ship is already occupied or does not exist. Try again!")
        else:
            print("Sorry, some of the positions where you want to place this ship is already occupied or does not exist. Try again!")
    
    return tauler


def placeShip(tauler):
    placeShip3(tauler,1)
    placeShip3(tauler,2)
    print(placeShip3(tauler,3))

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




def placeShip3(tauler, i):
    colocat = False
    while not colocat:
        print(f"Reading the 3 positions ship number {i}")
        entrada = input("Initial box [row:column from 0 to 4]: ")
        fila = int(entrada.split(':')[0])
        columna = int(entrada.split(':')[1])
        orientacio =input("Would you like to place the boat vertically or horizontally? (v / h): ")
        if orientacio == 'v':
            if fila >= 0 and fila <= 2 and columna >= 0 and columna <= 4:
                if tauler[fila][columna] == 'W' and tauler[fila+1][columna] == 'W' and tauler[fila+2][columna] == 'W':
                    tauler[fila][columna] = 'S'
                    tauler[fila+1][columna] = 'S'
                    tauler[fila+2][columna] = 'S'
                    colocat = True
                else:
                    print("Sorry, some of the positions where you want to place this ship is already occupied or does not exist. Try again!")
            else:
                print("Sorry, some of the positions where you want to place this ship is already occupied or does not exist. Try again!")
        
        elif orientacio == 'h':
            if fila >= 0 and fila <= 4 and columna >= 0 and columna <= 2:
                if tauler[fila][columna] == 'W' and tauler[fila][columna+1] == 'W' and tauler[fila][columna+2] == 'W':
                    tauler[fila][columna] = 'S'
                    tauler[fila][columna+1] = 'S'
                    tauler[fila][columna+2] = 'S'
                    colocat = True
                else:
                    print("Sorry, some of the positions where you want to place this ship is already occupied or does not exist. Try again!")
            else:
                print("Sorry, some of the positions where you want to place this ship is already occupied or does not exist. Try again!")
        else:
            print("Sorry, some of the positions where you want to place this ship is already occupied or does not exist. Try again!")
    
    return tauler


def placeShip(tauler):
    placeShip3(tauler,1)
    placeShip3(tauler,2)
    print(placeShip3(tauler,3))



def game():
    jugadorA = startBoard()
    jugadorB = startBoard()
    print("Jugador A. On vols posar els vaixells?")
    placeShip(jugadorA)
    print("Jugador B. On vols posar els vaixells?")
    placeShip(jugadorB)
    jugador_actual = 'A'
    while not final(jugadorA) and not final(jugadorB):
        if jugador_actual == 'A':
            print("Torn del Jugador A")
            shoot = input("A quina posició del taulell del jugador B creus que hi ha un vaixell [fila:columna]: ")
            jugadorB = applyPlay(jugadorB, shoot)
            jugador_actual = 'B'
        else:
            print("Torn del Jugador B")
            shoot = input("A quina posició del taulell del jugador A creus que hi ha un vaixell [fila:columna]: ")
            jugadorA = applyPlay(jugadorA, shoot)
            jugador_actual = 'A'
    
    if final(jugadorA):
        print("El Jugador B ha guanyat!")
    else:
        print("El Jugador A ha guanyat!")

game()
