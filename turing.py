class Turing:
    def __init__(self, position_lecture, bande, graphe):
        self.position_lecture = position_lecture
        self.bande = bande
        self.graphe = graphe
        self.etat = graphe.get("initial", 0)  # au cas où il n'est pas présent

    def etape(self):
        # return 0 ou 1

        if self.graphe[self.etat] == None: # état final
            return False # il n'y a plus d'étapes
        
        transition = self.graphe[self.etat][self.bande[self.position_lecture]]

        if transition[1] != None: # écrire qqch si on le veut vraiment
            self.bande[self.position_lecture] = transition[1]
        
        if transition[2] == 'L':
            self.position_lecture -= 1
        elif transition[2] == 'R':
            self.position_lecture += 1
            # augmenter la taille du ruban si besoin
            if self.position_lecture == len(self.bande):
                self.bande += ['B' for _ in range(16)]
        else:
            raise RuntimeError(f"Déplacement inconnu: {transition[2]} (possibles: L, R)")

        self.etat = transition[0]
        if self.etat not in self.graphe:
            raise RuntimeError(f"L'état demandé {self.etat} n'est pas dans le graphe (possibles: {', '.join(k for k in self.graphe.keys())})")

        return True # encore des étapes