from constants import *
import pygame

from board import Board
from dragger import Dragger
class Game:
    def __init__(self):
        self.board = Board()
        self.dragger = Dragger()
        pass

    ### show board  
    def set_rect_background(self,surface):
        for c in range(columns):
            for r in range(rows):
                if (r+c)%2 ==0:
                    color = (78,78,78)
                else:
                    color = (200,200,200)
                rect = (c*square_size_h,r*square_size_v,square_size_h,square_size_v)
                pygame.draw.rect(surface,color,rect)
                
    # def draw_circle(self,screen):
    #     radius = screen_width/2
    #     for col in range(columns):
    #         pygame.draw.circle(screen,(200,200,200),[screen_width/2,screen_height/2],radius,12)
    #         radius = radius - 25
    def show_pieces(self,surface):
        for r in range(rows):
            for c in range(columns):
                if self.board.squares[r][c].has_piece():
                    piece = self.board.squares[r][c].piece
                    if piece is not  self.dragger.piece:
                        img = pygame.image.load(piece.texture)
                        img_center = c*square_size_h + square_size_h //2 , r*square_size_v + square_size_v//2
                        piece.texture_rect = img.get_rect(center = img_center)
                        surface.blit(img,piece.texture_rect)




    