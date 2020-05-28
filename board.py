<<<<<<< HEAD
from piece import *
coord=[
'a8','b8','c8','d8','e8','f8','g8','h8',
'a7','b7','c7','d7','e7','f7','g7','h7',
'a6','b6','c6','d6','e6','f6','g6','h6',
'a5','b5','c5','d5','e5','f5','g5','h5',
'a4','b4','c4','d4','e4','f4','g4','h4',
'a3','b3','c3','d3','e3','f3','g3','h3',
'a2','b2','c2','d2','e2','f2','g2','h2',
'a1','b1','c1','d1','e1','f1','g1','h1'
]
echequier={}  #position des pieces sur l echequier
tab120 = (
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
tab64 = (
    21, 22, 23, 24, 25, 26, 27, 28,
    31, 32, 33, 34, 35, 36, 37, 38,
    41, 42, 43, 44, 45, 46, 47, 48,
    51, 52, 53, 54, 55, 56, 57, 58,
    61, 62, 63, 64, 65, 66, 67, 68,
    71, 72, 73, 74, 75, 76, 77, 78,
    81, 82, 83, 84, 85, 86, 87, 88,
    91, 92, 93, 94, 95, 96, 97, 98
)
FEN = {'ROI blanc': K, 'ROI noir': k, 'DAME blanc':Q, 'DAME noir':q, 'TOUR blanc':R, /
'TOUR noir':r, 'FOU blanc':B, 'FOU noir':b, 'CAVALIER blanc':N, 'CAVALIER noir':n, 'PION blanc':P, 'PION noir':p} #defini l etat dune ligne de l echequier pour la fonction set board
K = roi blanc k = roi noir Q = dame blanche q = dame noire
R = tour blanche r = tour noire B = fou blanc b = fou noir
N = cavalier blanc n = cavalier noir P = pion blanc p:pion noir
class Echequier(object):
        
    def __init__(self):
        "Init the chess board at starting position"
        # Chessboard has 64 squares, numbered from 0 to 63 (a8 to h1)
        # Placing pieces ('cases' is 'square' in french :)
        self.cases :[
            Piece('TOUR','noir'),Piece('CAVALIER','noir'),Piece('FOU','noir'),
            Piece('DAME','noir'),Piece('ROI','noir'),Piece('FOU','noir'),
            Piece('CAVALIER','noir'),Piece('TOUR','noir'),
            Piece('PION','noir'),Piece('PION','noir'),Piece('PION','noir'),
            Piece('PION','noir'),Piece('PION','noir'),Piece('PION','noir'),
            Piece('PION','noir'),Piece('PION','noir'),Piece('PION','noir'),
            Piece(),Piece(),Piece(),Piece(),Piece(),Piece(),Piece(),Piece(),
            Piece(),Piece(),Piece(),Piece(),Piece(),Piece(),Piece(),Piece(),
            Piece(),Piece(),Piece(),Piece(),Piece(),Piece(),Piece(),Piece(),
            Piece(),Piece(),Piece(),Piece(),Piece(),Piece(),Piece(),Piece(),
            Piece('PION','blanc'),Piece('PION','blanc'),Piece('PION','blanc'),
            Piece('PION','blanc'),Piece('PION','blanc'),Piece('PION','blanc'),
            Piece('PION','blanc'),Piece('PION','blanc'),
            Piece('TOUR','blanc'),Piece('CAVALIER','blanc'),Piece('FOU','blanc'),
            Piece('DAME','blanc'),Piece('ROI','blanc'),Piece('FOU','blanc'),
            Piece('CAVALIER','blanc'),Piece('TOUR','blanc')
        ]
        for num, in coord.keys():
            echequier[num] = self.cases[num] 
        self.echequier = echequier

    def gen_moves_list(self,color='',dontCallIsAttacked=False):
        """Returns all possible moves for the requested color.
    If color is not given, it is considered as the side to move.
    dontCallIsAttacked is a boolean flag to avoid recursive calls,
    due to the actually wrotten is_attacked() function calling
    this gen_moves_list() function.
    A move is defined as it :
    - the number of the starting square (pos1)
    - the number of the destination square (pos2)
    - the name of the piece to promote '','q','r','b','n'
    (queen, rook, bishop, knight)
    """
        for name in nomPiece:
            self.pos1[name][color] =  tab64[] #jsuis bloque
        self.pos2 = self.pos1 + #faut les fonctions pour les deplacements possibles dans piece.py
    def setboard(self,fen):
        """Set the board to the FEN position given. i.e. :
    rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - - 0
    Returns TRUE or FALSE if done or not.
    If not : print errors.
    """
    try:
    def getboard(self):
        """Returns the FEN notation of the current board. i.e. :
    rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - - 0
    """
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
        "Undo the last move in history"
    def changeTrait(self):
        "Change the side to move"
    def oppColor(self,c):
        "Returns the opposite color of the 'c' color given"
    def in_check(self,couleur):
        """Returns TRUE or FALSE
    if the KING of the given 'color' is in check"""
    def is_attacked(self,pos,couleur):
        """Returns TRUE or FALSE if the square number 'pos' is a
    destination square for the color 'couleur'.
    If so we can say that 'pos' is attacked by this side.
    This function is used for 'in check' and for castle moves."""
    def render(self):
        "Display the chessboard in console mode"
    def caseStr2Int(self,c):
        """'c' given in argument is a square name like 'e2'
    "This functino returns a square number like 52"""
    def caseInt2Str(self,i):
        """Given in argument : an integer between 0 and 63
    Returns a string like 'e2'"""
    def showHistory(self):
        "Displays the history of the moves played"
    def evaluer(self):
        """A wonderful evaluate() function
    returning actually only the material score"""`
=======
from piece import*
>>>>>>> a3353be6800821caba9c2acb2d127a4330d1a847
