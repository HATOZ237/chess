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

        # verification et erreurs de  création

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

    def isEmpty(self):
        """Returns TRUE or FALSE if this piece object is defined,
            As any square on board can have a piece on it, or not,
            we can set a null piece on a square.
        """
        return (self.nom == "")

    def pos2_roi(self):
        """[Me permet de generer les d"placements possibles pour le ROI]
        """
        if self.nom != 'ROI':
            raise ChessError(
                "désolé, cette pièce n'est pas un Roi mais un", self.nom)

    def pos2_tour(self, pos1, cAd, echiquier):
        """Returns the list of moves for a ROOK :
        - at square number 'pos1' (0 to 63)
        - opponent color is cAd (blanc,noir)
        """
        if self.nom != 'ROI':
            raise ChessError(
                "désolé, cette pièce n'est pas un Roi mais un", self.nom)

    def pos2_cavalier(self, pos1, cAd, echiquier):
        """Returns the list of moves for a KNIGHT :
        - at square number 'pos1' (0 to 63)
        - opponent color is cAd (blanc,noir)
        """
        if self.nom != 'CAVALIER':
            raise ChessError(
                "désolé, cette pièce n'est pas un CAVALIER mais un", self.nom)

    def pos2_fou(self, pos1, cAd, echiquier):
        """Returns the list of moves for a BISHOP :
        - at square number 'pos1' (0 to 63)
        - opponent color is cAd (blanc,noir)
        """
        if self.nom != 'FOU':
            raise ChessError(
                "désolé, cette pièce n'est pas un FOU mais un", self.nom)

    def pos2_pion(self, pos1, couleur, echiquier):
        """Returns the list of moves for a PAWN :
        - at square number 'pos1' (0 to 63)
        - opponent color is cAd (blanc,noir)
        """
        if self.nom != 'PION':
            raise ChessError(
                "désolé, cette pièce n'est pas un PION mais un", self.nom)
