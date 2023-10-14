from constants import *
import pygame

from Bot import Bot
from board import Board
from dragger import Dragger
class Game:
    def __init__(self):
        self.next_player = 'white'
        self.board = Board()
        self.dragger = Dragger()
        self.bot = Bot()
        pass

    ### show board  
    def set_rect_background(self,surface):
        for r in range(rows):
            for c in range(columns):
                if (r+c)%2 ==0:
                    color = (120,119,118)
                else:
                    color = (84,86,84)
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
    def show_moves(self,surface):
        if self.dragger.dragging:
            piece = self.dragger.piece
            for move in piece.moves:
                color = '#C86464' if (move.final.row+move.final.col)%2 == 0 else '#C84646'
                rect = (move.final.col*square_size_h,move.final.row*square_size_v,square_size_h,square_size_v)
                pygame.draw.rect(surface,color,rect)
    def next_turn(self):
        self.next_player= 'black' if  self.next_player == 'white' else 'white'
    
    def reset(self):
        self.__init__()

    def bot_move(self,surface):
        if self.next_player == self.bot.color:
            all_moves = self.board.generate_moves(self.bot.color)
            piece_bot,move_bot = self.bot.get_bot_moves(all_moves)
            self.board.move(piece_bot,move_bot)
            self.show_pieces(surface)
            self.set_rect_background(surface)
            self.next_turn() 



    