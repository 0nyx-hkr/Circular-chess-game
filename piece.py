import os

class Piece :

    def __init__(self,name,color,value,texture =None,texture_rect=None):
        self.name = name
        self.color = color
        self.moved = False
        value_sign = 1 if color=="white" else  -1
        self.value = value * value_sign
        self.texture  = texture
        self.set_texture()
        self.texture_rect = texture_rect
        self.moves = []
    def set_texture(self):
        self.texture = os.path.join(f'D:/circular_chess/Circular-chess-game/pictures/{self.color}_{self.name}.png')

    def add_moves(self,move):
        self.moves.append(move)
    def clear_moves(self):
        self.moves = []

    

class Pawn(Piece):

    def __init__(self,color):
        self.p_col = 1 if color=='white' else 0
        self.dir = 0
        super().__init__('pawn',color,1.0)



class Knight(Piece):

    def __init__(self,color):
        super().__init__('knight',color,3.0)




class Bishop(Piece):

    def __init__(self,color):
        super().__init__('bishop',color,3.1)





class Rook(Piece):

    def __init__(self,color):
        super().__init__('rook',color,5.0)

class Queen(Piece):

    def __init__(self,color):
        super().__init__('queen',color,9.0)

class King(Piece):

    def __init__(self,color):
        super().__init__('king',color,10000.0)



