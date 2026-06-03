#graphe pondéré 
graph = { 
    "A": ["B", "C"], 
    "B": ["D", "E"], 
    "C": ["F", "G"], 
    "D": ["H"], 
    "E": ["I", "J"], 
    "F": ["K"], 
    "G": ["L"], 
    "H": [], 
    "I": [], 
    "J": [], 
    "K": [], 
    "L": [] 
}

#heuristique
heuristic = { 
    "A": 10, 
    "B": 8, 
    "C": 5, 
    "D": 7, 
    "E": 6, 
    "F": 3, 
    "G": 2, 
    "H": 9, 
    "I": 4, 
    "J": 6, 
    "K": 1, 
    "L": 0 
}

def  GREEDY_BEST_SEARCH(Graphe, Heuristique, Départ, Objectif):
    OPEN =[Départ]
    VISITED=[]
    