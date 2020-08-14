from piece import *
from random import choice
 # defini l etat dune ligne de l echequier pour la fonction set board

couleurs = ["noir", "blanc"]

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
        'a8','b8','c8','d8','e8','f8','g8','h8',
        'a7','b7','c7','d7','e7','f7','g7','h7',
        'a6','b6','c6','d6','e6','f6','g6','h6',
        'a5','b5','c5','d5','e5','f5','g5','h5',
        'a4','b4','c4','d4','e4','f4','g4','h4',
        'a3','b3','c3','d3','e3','f3','g3','h3',
        'a2','b2','c2','d2','e2','f2','g2','h2',
        'a1','b1','c1','d1','e1','f1','g1','h1'
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
        self.trait = choice([1, 2])#0 pour noir et 1 pour blanc
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
        self.FEn = {'ROI blanc': k, 'ROI noir': K, 'DAME blanc':q, 'DAME noir':Q, 'TOUR blanc':r,
        'TOUR noir':R, 'FOU blanc':b, 'FOU noir':B, 'CAVALIER blanc':n, 'CAVALIER noir':N, 'PION blanc':p, 'PION noir':P}
        for num, val in enumerate(self.coord):
            for Num, Val in enumerate(self.tab64):
                if Num == num:
                    self.echequier[Val] = self.cases[num]
        

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
        all_list_move = []
        
        
        couleurs = ["noir", "blanc"]
        if color == '':
            raise ChessError('vous devez entrer une couleur')
        elif not color in couleurs:
            raise ChessError('Soit du noir, soit du blanc!!!')
        for a, b in self.echequier.items:
            if b.couleur == self.color:
                if b.nom == 'ROI':
                    listPiece = b.position(a)
                    all_list_move.append(move_roi_enable(listPiece, self.echequier, table64, self.color ))
                if b.nom == 'PION':
                    listPiece = b.position(a)
                    all_list_move.append(move_pion_enable(listPiece, self.echequier, table64, self.color))
                if b.nom == 'TOUR':
                    listPiece = b.position(a)
                    all_list_move.append(move_tour_enable(listPiece, self.echequier, table64, self.color))
                if b.nom == 'FOU':
                    listPiece = b.position(a)
                    all_list_move.append(move_fou_enable(listPiece, self.echequier, table64, self.color))
                if b.nom == 'CAVALIER':
                    listPiece = b.position(a)
                    all_list_move.append(move_cavalier_enable(listPiece, self.echequier, table64, self.color))
                if b.nom == 'DAME':
                    listPiece = b.position(a)
                    all_list_move.append(move_dame_enable(listPiece, self.echequier, table64, self.color))
        return all_list_move
                 

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
        FEN = ''
        for num, vale in self.echequier: 
            for cle, valeur in self.FEn.items():
                if vale.nom + ' ' + vale.couleur == cle:
                    self.FEN+= valeur
                else:
                    if self.FEN[len(self.FEN)-1]  in [1,2,3,4,5,6,7]:
                        self.FEN = FEN[0: len(self.FEN)] + str(int (FEN[len(self.FEN)-1]) + 1)
                    else:
                        self.FEN+= '1'  
            if (num+1)//8 == (num+1)/8 and num < 63:
                FEN += '/'
                             
                
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
        pass


    def undomove(self):
        """Undo the last move in history"""
        pass

    def changeTrait(self):
        "Change the side to move"
        if self.trait == 1:
            self.trait = 2
        if self.trait == 2:
            self.trait == 1
    
    def oppColor(self,c):
        "Returns the opposite color of the 'c' color given"
        
        if not c in ["blanc", "noir"]:
            return ChessError("Cette couleur n'existe pas")
        if c == "blanc":
            return "noir"
        if c == "noir":
            return "blanc"
        
    
    def in_check(self,couleur):
        """Returns TRUE or FALSE
        if the KING of the given 'color' is in check"""
        pos_roi = 0
        for a, b in self.echequier.items():
            if b.couleur == couleur & b.nom == 'roi':
                pos_roi = a
        return self.is_attacked(pos_roi, self.oppColor(couleur))               
        
    
    def is_attacked(self,pos,couleur):
        """Returns TRUE or FALSE if the square number 'pos' is a
        destination square for the color 'couleur'.
        If so we can say that 'pos' is attacked by this side.
        This function is used for 'in check' and for castle moves."""
        pion_couleur = []
        for a,b in self.echequier.items():
            if b.coleur == couleur:
                pion_couleur.append(a)
        if pos in pion_couleur:
            ChessError("le pion ne peut pas etre attaque par un de mm couleur")
        for a, b in enumerate(self.gen_moves_list(couleur)):
            if b == pos:
                bol = True
        return bol    
    def render(self):
        """Display the chessboard in console mode"""
        pass
    def caseStr2Int(self,c):
        """'c' given in argument is a square name like 'e2'
        "This functino returns a square number like 52"""
        if not c in self.coord:
            raise ChessError("la case", c, " n appartient pas a l echequier")
        s_number = 0
        for num, val in enumerate(self.coord):
            if val == c:
                s_number = num
        return s_number
    
    def caseInt2Str(self,i):
        """Given in argument : an integer between 0 and 63
        Returns a string like 'e2'"""
        if not i in list(range(0,63)):
            raise ChessError("la case", i, " n appartient pas a l echequier")
        s_string = ''
        for num, val in enumerate(self.coord):
            if num == i:
                s_string = val
        return s_string    
    def showHistory(self):
        """Displays the history of the moves played"""
        pass
    
    def evaluer(self):
        """A wonderful evaluate() function
        returning actually only the material score"""
        pass


def move_cavalier_enable(liste_move:list, cases:dict, table:tuple, color:str):
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

def move_fou_enabled(liste_move:list, cases:dict, table:tuple, color:str):
    """Cette fonction trie parmi les futures positions possibles 
        d'un fou ou d'une tour, celles qui peuvent être jouées

        Args:
                
            liste_move (list): liste des positions générées par la methode pos2_fou ou pos2_tour
                    
            cases (list): liste representant la disposition des pieces sur l'echiquier
                    
            table (tuple): Il s'agit de la table64 qui fait la correspondance entre les pieces de l'echiquier et leurs positions
                    
            color (str): couleur du cavalier
                """
    liste = [[] for i in range(4)]
    for i, mini_liste in enumerate(liste_move):
        for pos in mini_liste:
            if cases[table.index(pos)].isEmpty():
                liste[i].append(pos)
            else:
                if cases[table.index(pos)].couleur != color:
                    liste[i].append(pos)
                    break
                else:
                    break
    return liste
def move_pion_enable(liste_move:list, cases:dict, table:tuple, color:str):
    liste = []
    #code
    return liste
                
def move_tour_enable(liste_move:list, cases:dict, table:tuple, color:str):
    liste = []
        #code...
    return liste
def move_roi_enable(liste_move:list, cases:dict, table:tuple, color:str):
    liste = []
        #code...
    return liste            
def move_dame_enable(liste_move:list, cases:dict, table:tuple, color:str):
     
     pass

            
