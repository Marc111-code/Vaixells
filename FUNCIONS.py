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
