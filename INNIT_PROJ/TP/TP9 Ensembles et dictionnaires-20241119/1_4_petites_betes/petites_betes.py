"""Init Dev : TP9"""
# ==========================
# Petites bêtes
# ==========================

def toutes_les_familles(pokedex):
    """détermine l'ensemble des familles représentées dans le pokedex

    Args:
        pokedex (list): liste de pokemon, chaque pokemon est modélisé par
        un couple de str (nom, famille)

    Returns:
        set: l'ensemble des familles représentées dans le pokedex
    """
    ens = set()
    for i in range(len(pokedex)):
        ens.add(pokedex[i][1])
    return ens 

def nombre_pokemons(pokedex, famille):
    """calcule le nombre de pokemons d'une certaine famille dans un pokedex

    Args:
        pokedex (list): liste de pokemon, chaque pokemon est modélisé par
        un couple de str (nom, famille)
        famille (str): le nom de la famille concernée

    Returns:
        int: le nombre de pokemons d'une certaine famille dans un pokedex
    """
    cpt = 0
    for i in range(len(pokedex)):
        if pokedex[i][1] == famille:
            cpt +=1 
    return cpt

def frequences_famille(pokedex):
    """Construit le dictionnaire de fréqeunces des familles d'un pokedex

    Args:
        pokedex (list): liste de pokemon, chaque pokemon est modélisé par
        un couple de str (nom, famille)

    Returns:
        dict: un dictionnaire dont les clés sont le nom de familles (str)
        et la valeur associée est le nombre de représentants de la famille (int)
    """
    dico = {}
    for i in range(len(pokedex)):
        if pokedex[i][1] in dico.keys():
            dico[pokedex[i][1]] +=1 
        else:
            dico[pokedex[i][1]] = 1 
    return dico 

def dico_par_famille(pokedex):
    """Construit un dictionnaire dont les les clés sont le nom de familles (str)
    et la valeur associée est l'ensemble (set) des noms des pokemons de cette
    famille dans le pokedex

    Args:
        pokedex (list): liste de pokemon, chaque pokemon est modélisé par
        un couple de str (nom, famille)

    Returns:
        dict: un dictionnaire dont les clés sont le nom de familles (str) et la valeur associée est
        l'ensemble (set) des noms des pokemons de cette famille dans le pokedex
    """

    ens = set()
    dico = {}
    for i in range(len(pokedex)):
        for j in range(len(pokedex)):
            if pokedex[i][1] == pokedex[j][1] and j != i :
                ens.add(pokedex[i][0])
                dico[pokedex[i][1]] = ens
            elif pokedex[i][1] != pokedex[j][1]: 
                dico[pokedex[i][1]] = set([pokedex[i][0]])
    return dico 

def famille_la_plus_representee(pokedex):
    """détermine le nom de la famille la plus représentée dans le pokedex

    Args:
        pokedex (list): liste de pokemon, chaque pokemon est modélisé par
        un couple de str (nom, famille)

    Returns:
        str: le nom de la famille la plus représentée dans le pokedex
    """
    return max(frequences_famille(pokedex))
# ==========================
# Petites bêtes (la suite)
# ==========================


def toutes_les_familles_v2(pokedex):
    """détermine l'ensemble des familles représentées dans le pokedex

    Args:
        pokedex (dict): un dictionnaire dont les clés sont les noms de pokemons et la
        valeur associée l'ensemble (set) de ses familles (str)

    Returns:
        set: l'ensemble des familles représentées dans le pokedex
    """
    ens = set()
    for elem in pokedex:
        ens.update(pokedex[elem])
    return ens

def nombre_pokemons_v2(pokedex, famille):
    """calcule le nombre de pokemons d'une certaine famille dans un pokedex

    Args:
        pokedex (dict): un dictionnaire dont les clés sont les noms de pokemons et la
        valeur associée l'ensemble (set) de ses familles (str)
        famille (str): le nom de la famille concernée

    Returns:
        int: le nombre de pokemons d'une certaine famille dans un pokedex
    """
    cpt = 0
    for elem in pokedex:
        if famille in pokedex[elem]:
            cpt +=1 
    return cpt 
mon_pokedex = {"Bulbizarre":{"Plante", "Poison"},"Aeromite":{"Poison", "Insecte"}, "Abo":{"Poison"}}
def frequences_famille_v2(pokedex):
    """Construit le dictionnaire de fréqeunces des familles d'un pokedex

    Args:
        pokedex (dict): un dictionnaire dont les clés sont les noms de pokemons et la
        valeur associée l'ensemble (set) de ses familles (str)

    Returns:
        dict: un dictionnaire dont les clés sont le nom de familles (str) et la valeur
        associée est le nombre de représentants de la famille (int)
    """
    dico = {}
    listo = []
    for elem in pokedex:
        listo.extend(list(pokedex[elem]))
    for i in range(len(listo)):
        if listo[i] in dico.keys():
            dico[listo[i]] +=1 
        else:
            dico[listo[i]] = 1 
    return dico 

def dico_par_famille_v2(pokedex):
    """Construit un dictionnaire dont les les clés sont le nom de familles (str)
    et la valeur associée est l'ensemble (set) des noms des pokemons de
    cette famille dans le pokedex

    Args:
        pokedex (dict): un dictionnaire dont les clés sont les noms de pokemons et la
        valeur associée l'ensemble (set) de ses familles (str)

    Returns:
        dict: un dictionnaire dont les clés sont le nom de familles (str) et la valeur associée est
        l'ensemble (set) des noms des pokemons de cette famille dans le pokedex
    """
    dico = {}
    for elem in toutes_les_familles_v2(pokedex):
        dico[elem] = set()
        for clef in pokedex:
            if elem in pokedex[clef]:
                dico[elem].add(clef)
    return dico 

def famille_la_plus_representee_v2(pokedex):
    """détermine le nom de la famille la plus représentée dans le pokedex

    Args:
        pokedex (dict): un dictionnaire dont les clés sont les noms de pokemons et la
        valeur associée l'ensemble (set) de ses familles (str)

    Returns:
        str: le nom de la famille la plus représentée dans le pokedex
    """
    return max(frequences_famille_v2(pokedex).keys())  
