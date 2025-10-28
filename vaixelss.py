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
