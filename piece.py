
class ChessError(Exception):
    """
    Cette classe retourne des erreurs
    lorsque le jeu Chess a des problèmes

    """


class Piece():
    """[Cette classe permet de gerer le comportement des pieces de l'echec]
    """

    def __init__(self, nom="", couleur=""):
        """Creating a piece object, with its attributes :
    - 'nom' as name (ROI, DAME...);
    - 'couleur' as color (blanc,noir);
    - 'valeur' as its value"""
        # initialisation des elements importants
        VIDE = ''
        nomPiece = [VIDE, 'ROI', 'DAME', 'TOUR', 'CAVALIER', 'FOU', 'PION']
        valeurPiece = [0, 0, 9, 5, 3, 3, 1]

        # verifications et erreurs de  création

        if not couleur in ["blanc", "noir", ""]:
            # si la couleur n'est ni du blanc ni du noir ni vide
            raise ChessError("La couleur entrée n'est ni du blanc ni du noir")
        if not nom in nomPiece:
            raise ChessError(
                'Le nom de votre piece ne correspond à aucun nom prédéfini')
        if nom == VIDE and (not couleur == VIDE):
            raise ChessError('pas de piece, pas de couleur!!!')
        if (not nom == VIDE) and couleur == VIDE:
            raise ChessError('pas de piece, pas de couleur!!!')

        # creation des instances de la classe
        self.nom = nom
        self.couleur = couleur
        self.valeur = valeurPiece[nomPiece.index(self.nom)]
        self.already_moved = False
        # creation des tableaux de verification
        self.tab120 = (
            -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
            -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
            -1, 0, 1, 2, 3, 4, 5, 6, 7, -1,
            -1, 8, 9, 10, 11, 12, 13, 14, 15, -1,
            -1, 16, 17, 18, 19, 20, 21, 22, 23, -1,
            -1, 24, 25, 26, 27, 28, 29, 30, 31, -1,
            -1, 32, 33, 34, 35, 36, 37, 38, 39, -1,
            -1, 40, 41, 42, 43, 44, 45, 46, 47, -1,
            -1, 48, 49, 50, 51, 52, 53, 54, 55, -1,
            -1, 56, 57, 58, 59, 60, 61, 62, 63, -1,
            -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
            -1, -1, -1, -1, -1, -1, -1, -1, -1, -1
        )
        self.tab64 = (
            21, 22, 23, 24, 25, 26, 27, 28,
            31, 32, 33, 34, 35, 36, 37, 38,
            41, 42, 43, 44, 45, 46, 47, 48,
            51, 52, 53, 54, 55, 56, 57, 58,
            61, 62, 63, 64, 65, 66, 67, 68,
            71, 72, 73, 74, 75, 76, 77, 78,
            81, 82, 83, 84, 85, 86, 87, 88,
            91, 92, 93, 94, 95, 96, 97, 98
        )

    def isEmpty(self):
        """Returns TRUE or FALSE if this piece object is defined,
            As any square on board can have a piece on it, or not,
            we can set a null piece on a square.
        """
        return (self.nom == "")

    def pos2_roi(self,pos1):
        """[Me permet de generer les d"placements possibles pour le ROI]
        """
        if self.nom != 'ROI':
            raise ChessError(
                "désolé, cette pièce n'est pas un Roi mais un", self.nom)
        # je m'assure que la position entrée est valide
        if not pos1 in self.tab64:
            raise ChessError("Cette position n'existe pas")
        move_liste = []
        #deplacement banal sur une case autour de roi
        for i in [-10,10,-1,1,-11,-9,11,9]:
            move_liste.append(pos1+i) 
            

        

    def pos2_tour(self, pos1):
        """Returns the list of moves for a ROOK :
        - at square number 'pos1' (0 to 63)
        - opponent color is cAd (blanc,noir)
        """
        if not (self.nom in ['TOUR', "DAME"]):
            raise ChessError(
                "désolé, cette pièce n'est pas une TOUR mais un", self.nom)
        # je m'assure que la position entrée est valide
        if not pos1 in self.tab64:
            raise ChessError("Cette position n'existe pas")
        #construction de la liste
        deplacements_tour = (-10,10,-1,1) # depl. vertical et horizontal
        liste_move = [[] for i in range(len(deplacements_tour))]
        for i, x in enumerate(deplacements_tour):
            pos = pos1
            while self.tab120[pos+x] != -1:
                liste_move[i].append(pos+x)
                pos = pos+x
        return liste_move

    def pos2_cavalier(self, pos1):
        """Returns the list of moves for a KNIGHT :
        - at square number 'pos1' (0 to 63)
        - opponent color is cAd (blanc,noir)
        """
        # je m'assure que seul le Cabvalier peut utiliser cette méthode
        if not self.nom in ["CAVALIER", "DAME"]:
            raise ChessError(
                "désolé, cette pièce n'est pas un CAVALIER mais un", self.nom)
        # je m'assure que la position entrée est valide
        if not pos1 in self.tab64:
            raise ChessError("Cette position n'existe pas")
        # construction de l'ensemble des mouvements
        deplacements_cavalier = (-12, -21, -19, -8, 12, 21, 19, 8)
        liste_move = []
        for x in deplacements_cavalier:
            if self.tab120[pos1+x] != -1:
                liste_move.append(pos1+x)
        return liste_move

    def pos2_fou(self, pos1):
        """Returns the list of moves for a BISHOP :
        - at square number 'pos1' (0 to 63)
        - opponent color is cAd (blanc,noir)
        """
        if not (self.nom in ['FOU', "DAME"]):
            raise ChessError(
                "désolé, cette pièce n'est pas un FOU mais un", self.nom)
        # je m'assure que la position entrée est valide
        if not pos1 in self.tab64:
            raise ChessError("Cette position n'existe pas")
        #construction de l'ensemble des mouvements
        deplacements_fou = (-11,-9,11,9)
        liste_move = [[] for i in range(len(deplacements_fou))]
        for i, x in enumerate(deplacements_fou):
            pos = pos1
            while self.tab120[pos+x] != -1:
                liste_move[i].append(pos+x)
                pos = pos+x
        return liste_move
        

    def pos2_pion(self, pos1):
        """Returns the list of moves for a PAWN :
        - at square number 'pos1' (0 to 63)
        - opponent color is cAd (blanc,noir)
        """
        if self.nom != 'PION':
            raise ChessError(
                "désolé, cette pièce n'est pas un PION mais un", self.nom)
        # je m'assure que la position entrée est valide
        if not pos1 in self.tab64:
            raise ChessError("Cette position n'existe pas")
        tab = {"noir": -8, "blanc": 8}
        tab_spec = {"noir": -16, "blanc": 16}
        liste_move = [tab[self.couleur]]
        if not self.already_moved:
            liste_move.append(tab_spec[self.couleur])
        return liste_move

        
    def pos2_dame(self,pos1):
        """Returns the list of moves for a PAWN :
        - at square number 'pos1' (0 to 63)
        - opponent color is cAd (blanc,noir)
        """
        return self.pos2_tour(pos1)+self.pos2_fou(pos1)
        
    
    def position(self, pos):
        dico = {'TOUR': self.pos2_tour, 'PION':self.pos2_pion, "DAME": self.pos2_dame, "ROI":self.pos2_roi,
                "FOU": self.pos2_fou, "CAVALIER": self.pos2_cavalier}
        return dico[self.nom](pos)
        
        
