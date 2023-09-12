from constants  import *
from square import Square
from piece import *
from move import Move

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
    def calc_moves(self,piece,row,col):
        def pawn_valid_moves():
            # 2 steps at beginning 1 later
            steps  = 1 if piece.moved else 2
            # vertical 
            dir = 1 if piece.p_col != row//8 else -1 
            start = row + dir
            end  = row + (dir*(1+steps))
            for move_row  in range(start,end,dir):
                if self.squares[move_row][col].isempty():
                    initial = Square(row,col)
                    final = Square(move_row,col)

                    move = Move(initial,final)
                    piece.add_moves(move)
                else:
                    break
                #diagnal
            possible_move_row =  row + dir
            possible_move_col = (col-1,col+1)
            for pmc in possible_move_col:
                if  Square.in_range(pmc):
                    if self.squares[possible_move_row][pmc].has_enemy_piece(piece.color):
                        initial = Square(row,col)
                        final = Square(possible_move_row,pmc)

                        move = Move(initial,final)
                        piece.add_moves(move)

    
        def kinght_valid_moves():
            possible_moves = [
                (row-2, col+1),
                (row-1, col+2),
                (row+1, col+2),
                (row+2, col+1),
                (row+2, col-1),
                (row+1, col-2),
                (row-1, col-2),
                (row-2, col-1),
            ]
            for possible_move in possible_moves:
                possible_move_row, possible_move_col = possible_move
                possible_move_row = possible_move_row % 16 
                if Square.in_range(possible_move_col):
                        if self.squares[possible_move_row][possible_move_col].isempty_or_enemy(piece.color):
                            # create squares of the new move
                            initial = Square(row, col)
                            # final_piece = self.squares[possible_move_row][possible_move_col].piece
                            final = Square(possible_move_row, possible_move_col)
                            # create new move
                            move = Move(initial, final)
                            piece.add_moves(move)

    
        def line_moves(incs):
            for inc in incs:
                row_inc,col_inc = inc
                poss_mov_row = (row + row_inc)%16
                poss_mov_col = col  + col_inc
                while True:
                    if Square.in_range(poss_mov_col):
                        initial = Square(row,col)
                        final = Square(poss_mov_row,poss_mov_col)
                        move = Move(initial,final)

                        if self.squares[poss_mov_row][poss_mov_col].isempty():
                            piece.add_moves(move)
                        if self.squares[poss_mov_row][poss_mov_col].has_enemy_piece(piece.color):
                             piece.add_moves(move)
                             break
                        if self.squares[poss_mov_row][poss_mov_col].has_team_piece(piece.color):
                             break
                    else:
                        break
                    poss_mov_row = (poss_mov_row + row_inc)%16
                    poss_mov_col =  poss_mov_col + col_inc


        def king_valid_moves():
            pass
    
        
        if isinstance(piece,Pawn):
            pawn_valid_moves()
        if isinstance(piece,Knight):
            kinght_valid_moves()
        if isinstance(piece,Bishop):
            line_moves([
                (1,1),(-1,-1),(-1,1),(1,-1)
            ])
        
        if isinstance(piece,Rook):
            line_moves([
                (0,1),(0,-1),(-1,0),(1,0)
            ])
        if isinstance(piece,Queen):
           line_moves([
                (1,1),(-1,-1),(-1,1),(1,-1),(0,1),(0,-1),(-1,0),(1,0)
            ])
        
        if isinstance(piece,King):
            king_valid_moves()
        


        
        
        
        








