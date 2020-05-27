class ChessError(Exception):
    """
    Cette classe retourne des erreurs
    lorsque la classe Quoridor a des problèmes
    """


class Piece():
    """[Cette classe permet de gerer le comportement des pieces de l'echec]
    """

    def __init__(self, nom, couleur):
        """Creating a piece object, with its attributes :
    - 'nom' as name (ROI, DAME...);
    - 'couleur' as color (blanc,noir);
    - 'valeur' as its value"""
        pass

    def isEmpty(self):
        """Returns TRUE or FALSE if this piece object is defined,
            As any square on board can have a piece on it, or not,
            we can set a null piece on a square."""
        pass

    def pos2_roi(self):
        pass

    def pos2_tour(self, pos1, cAd, echiquier):
        """Returns the list of moves for a ROOK :
        - at square number 'pos1' (0 to 63)
        - opponent color is cAd (blanc,noir)"""
        pass

    def pos2_cavalier(self, pos1, cAd, echiquier):
        """Returns the list of moves for a KNIGHT :
        - at square number 'pos1' (0 to 63)
        - opponent color is cAd (blanc,noir)"""
        pass

    def pos2_fou(self, pos1, cAd, echiquier):
        """Returns the list of moves for a BISHOP :
        - at square number 'pos1' (0 to 63)
        - opponent color is cAd (blanc,noir)"""
        pass

    def pos2_pion(self, pos1, couleur, echiquier):
        """Returns the list of moves for a PAWN :
        - at square number 'pos1' (0 to 63)
        - opponent color is cAd (blanc,noir)"""
        pass
