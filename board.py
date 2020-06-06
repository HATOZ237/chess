from piece import *
from random import choice
 # defini l etat dune ligne de l echequier pour la fonction set board


class Echequier():

    def __init__(self):
        "Init the chess board at starting position"
        # Chessboard has 64 squares, numbered from 0 to 63 (a8 to h1)
        # Placing pieces ('cases' is 'square' in french :)
        self.cases = [
            Piece('TOUR', 'noir'), Piece(
                'CAVALIER', 'noir'), Piece('FOU', 'noir'),
            Piece('DAME', 'noir'), Piece('ROI', 'noir'), Piece('FOU', 'noir'),
            Piece('CAVALIER', 'noir'), Piece('TOUR', 'noir'),
            Piece('PION', 'noir'), Piece(
                'PION', 'noir'), Piece('PION', 'noir'),
            Piece('PION', 'noir'), Piece(
                'PION', 'noir'), Piece('PION', 'noir'),
            Piece('PION', 'noir'), Piece(
                'PION', 'noir'), Piece('PION', 'noir'),
            Piece(), Piece(), Piece(), Piece(), Piece(), Piece(), Piece(), Piece(),
            Piece(), Piece(), Piece(), Piece(), Piece(), Piece(), Piece(), Piece(),
            Piece(), Piece(), Piece(), Piece(), Piece(), Piece(), Piece(), Piece(),
            Piece(), Piece(), Piece(), Piece(), Piece(), Piece(), Piece(), Piece(),
            Piece('PION', 'blanc'), Piece(
                'PION', 'blanc'), Piece('PION', 'blanc'),
            Piece('PION', 'blanc'), Piece(
                'PION', 'blanc'), Piece('PION', 'blanc'),
            Piece('PION', 'blanc'), Piece('PION', 'blanc'),
            Piece('TOUR', 'blanc'), Piece(
                'CAVALIER', 'blanc'), Piece('FOU', 'blanc'),
            Piece('DAME', 'blanc'), Piece(
                'ROI', 'blanc'), Piece('FOU', 'blanc'),
            Piece('CAVALIER', 'blanc'), Piece('TOUR', 'blanc')
        ]
        self.coord = [
        ['a', 8], ['b', 8], ['c', 8], ['d', 8], [
            'e', 8], ['f', 8], ['g', 8], ['h', 8],
        ['a', 7], ['b', 7], ['c', 7], ['d', 7], [
            'e', 7], ['f', 7], ['g', 7], ['h', 7],
        ['a', 6], ['b', 6], ['c', 6], ['d', 6], [
            'e', 6], ['f', 6], ['g', 6], ['h', 6],
        ['a', 5], ['b', 5], ['c', 5], ['d', 5], [
            'e', 5], ['f', 5], ['g', 5], ['h', 5],
        ['a', 4], ['b', 4], ['c', 4], ['d', 4], [
            'e', 4], ['f', 4], ['g', 4], ['h', 4],
        ['a', 3], ['b', 3], ['c', 3], ['d', 3], [
            'e', 3], ['f', 3], ['g', 3], ['h', 3],
        ['a', 2], ['b', 2], ['c', 2], ['d', 2], [
            'e', 2], ['f', 2], ['g', 2], ['h', 2],
        ['a', 1], ['b', 1], ['c', 1], ['d', 1], [
            'e', 1], ['f', 1], ['g', 1], ['h', 1]
        ]
        self.echequier = {}  # position des pieces sur l echequier
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
        self.trait = choice([0, 1])#0 pour noir et 1 pour blanc
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
        """self.FEn = {'ROI blanc': k, 'ROI noir': K, 'DAME blanc':q, 'DAME noir':Q, 'TOUR blanc':r,
        'TOUR noir':R, 'FOU blanc':b, 'FOU noir':B, 'CAVALIER blanc':n, 'CAVALIER noir':N, 'PION blanc':p, 'PION noir':P}
        for num in coord.keys():
            self.echequier[num] = self.cases[num] """

    def gen_moves_list(self, color='', dontCallIsAttacked=False):
        """Returns all possible moves for the requested color.If color is not given, it is considered as the side to move.
        dontCallIsAttacked is a boolean flag to avoid recursive calls,
        due to the actually wrotten is_attacked() function calling
        this gen_moves_list() function.
        A move is defined as it :
        - the number of the starting square (pos1)
        - the number of the destination square (pos2)
        - the name of the piece to promote '','q','r','b','n'
        (queen, rook, bishop, knight)"""
        
        couleur = ["noir", "blanc"]
        if color == '':
            color = couleur[self.trait]
        elif not color in couleur:
            raise ChessError('Soit du noir, soit du blanc!!!')
            
        
        
            
        

    def setboard(self,fen):
        """Set the board to the FEN position given. i.e. :
    rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - - 0
    Returns TRUE or FALSE if done or not.
    If not : print errors.
    """
        pass

            


    def getboard(self):
        """Returns the FEN notation of the current board. i.e. :
    rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - - 0
    """
        """FEN = ''
        for num, vale in self.echequier: 
            for cle, valeur in self.FEn.items():
                if vale.nom + ' ' + vale.couleur == cle:
                    self.FEN+= valeur
                else:
                    if self.FEN[len(self.FEN)-1]  in [1,2,3,4,5,6,7]:
                        self.FEN = FEN[0: len(self.FEN)-1] + str(int (FEN[len(self.FEN)-1)]) + 1)"""
        
            
                 
                
    def domove(self,depart,arrivee,promote):
        """Move a piece on the board from the square numbers
    'depart' to 'arrivee' (0..63) respecting rules :
    - prise en passant
    - promote and under-promote
    - castle rights
    Returns :
    - TRUE if the move do not let king in check
    - FALSE otherwise and undomove is done.
    """

    def undomove(self):
        """Undo the last move in history"""
        pass

    def changeTrait(self):
        "Change the side to move"
        pass
    
    def oppColor(self,c):
        "Returns the opposite color of the 'c' color given"
        pass
    
    def in_check(self,couleur):
        """Returns TRUE or FALSE
        if the KING of the given 'color' is in check"""
        pass
    
    def is_attacked(self,pos,couleur):
        """Returns TRUE or FALSE if the square number 'pos' is a
        destination square for the color 'couleur'.
        If so we can say that 'pos' is attacked by this side.
        This function is used for 'in check' and for castle moves."""
        pass
    
    def render(self):
        """Display the chessboard in console mode"""
        pass
    def caseStr2Int(self,c):
        """'c' given in argument is a square name like 'e2'
        "This functino returns a square number like 52"""
        pass
    
    def caseInt2Str(self,i):
        """Given in argument : an integer between 0 and 63
        Returns a string like 'e2'"""
        pass
    
    def showHistory(self):
        """Displays the history of the moves played"""
        pass
    
    def evaluer(self):
        """A wonderful evaluate() function
        returning actually only the material score"""
        pass

def move_cavalier_enable(liste_move:list, cases:list, table:tuple, color:str):
    """Cette fonction trie parmi les futures positions possibles 
    d'un Cavalier, celles qui peuvent être jouées

    Args:
        liste_move (list): liste des positions générées par la methode pos2_cavalier
        cases (list): liste representant la disposition des pieces sur l'echiquier
        table (tuple): Il s'agit de la table64 qui fait la correspondance entre les pieces de l'echiquier et leurs positions
        color (str): couleur du cavalier
    """
    liste = []
    for x in liste_move:
        if cases[table.index(x)].isEmpty() or cases[table.index(x)].couleur != color:
            liste.append(x)
    return liste
            