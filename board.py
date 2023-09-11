from constants  import *
from square import Square
from piece import *

class Board:

    def __init__(self):
        self.squares = [[0,0,0,0] for row in range(rows)]
        self._create()
        self._add_pieces('white')
        self._add_pieces('black')
    def _create(self):
        for row in range(rows):
            for col in range(columns):
                self.squares[row][col] = Square(row,col)
    
    def _add_pieces(self,color):
        if color == 'white':
            pawn_rows = (1,-2)
            other_rows  =(0,-1)
        else:
            pawn_rows =   (6,9)
            other_rows = (8,7)
        for  row in pawn_rows:
            for col in range(columns):
                self.squares[row][col] = Square(row,col,Pawn(color))
        for row in other_rows:
            # rook
            self.squares[row][3] = Square(row,3,Rook(color))  
            self.squares[row][2] = Square(row,2,Knight(color))
            self.squares[row][1] = Square(row,1,Bishop(color))
        self.squares[other_rows[0]][0] = Square(other_rows[0],0,Queen(color))
        self.squares[other_rows[1]][0] = Square(other_rows[1],0,King(color))
    def calc_moves(self,piece,move,bool=False):
        def pawn_valid_moves():
            pass
    
        def kinght_valid_moves():
            pass
    
        def bishiop_valid_moves():
            pass
    
        def rook_valid_moves():
            pass
    
        def queen_valid_moves():
            pass
    
        def king_valid_moves():
            pass
    
        
        if isinstance(piece,Pawn):
            pawn_valid_moves()
        if isinstance(piece,Knight):
            kinght_valid_moves()
        if isinstance(piece,Bishop):
            bishiop_valid_moves()
        
        if isinstance(piece,Rook):
            rook_valid_moves()
        if isinstance(piece,Queen):
            queen_valid_moves()
        
        if isinstance(piece,King):
            king_valid_moves()
        


        
        
        
        








