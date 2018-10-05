## Problème 16

def solve(nombre):
    iterable = str(nombre)
    somme = 0
    for chiffre in iterable:
        somme += int(chiffre)
    return somme

assert solve(2**15) == 26

print(solve(2**1000))


## Problème 22

fichier = open("p022_names.txt", "r")
for ligne in fichier :
    l = ligne
l = l.replace('"','') #retire les " en trop sinon le split met des doubles quotes
l = l.split(',') #crée une liste à partir du fichier
fichier.close()
def solve(l):
    resultat = 0
    l = sorted(l)
    for indice,nom in enumerate(l):
        somme = 0
        for char in nom :
            somme += ord(char)-64 #ord renvoie le numéro associé au charactère, pour a : ord('A') = 65, d'où le -64. 
        resultat += somme*(indice+1) #le +1 est pour adapter la numérotation utilisé par python à celle de la consigne
    return resultat
    
assert solve(['A']) == 1

print(solve(l))

## Problème 55

def palindrome(nombre) : 
    '''prend en entrée un nombre et répond si c'est un palindrome'''
    iterable = str(nombre)
    bool = True
    indice = 0
    while indice <= (len(iterable)//2) and bool:
        if iterable[indice] != iterable[-indice-1] : #l'indice symétrique à l'indice n est l'indice -n-1 (0->-1, 1->-2 etc...)
            bool = False
        indice += 1
    return bool
    
def creeinverse(nombre) : 
    '''prend en entrée un nombre et renvoie son inverse'''
    iterable = str(nombre)
    resultat = ''
    for chiffre in iterable:
        resultat = chiffre + resultat
    return(int(resultat))

def solve(max):
    resultat = 0
    for nombre in range(1,max+1):
        calcul = nombre + creeinverse(nombre)
        nombre_de_test = 1
        while not palindrome(calcul) and nombre_de_test < 50:
            calcul = calcul + creeinverse(calcul)
            nombre_de_test += 1
        if nombre_de_test >= 50 :
            resultat += 1
    return resultat
    
assert palindrome(123321)

assert creeinverse(123) == 321

print(solve(10000))