import pygame
from constants import *
import sys
from game import Game
from square import Square
from move import Move

class Main:
    def __init__(self) :
        pygame.init()
        self.screen = pygame.display.set_mode((screen_width,screen_height))
        pygame.display.set_caption("chess")
        self.game = Game()
    def main_loop(self):
        screen = self.screen
        game = self.game
        while True:
            game.bot_move(screen)
            game.set_rect_background(screen)
            game.show_pieces(screen)
            if game.dragger.dragging:
                game.dragger.update_blit(screen)
                game.show_moves(screen)
            for event  in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    game.dragger.mouse_pos(event.pos)
                    clicked_row = game.dragger.mouseY// square_size_v
                    clicked_column = game.dragger.mouseX// square_size_h
                    if game.board.squares[clicked_row][clicked_column].has_piece():
                        piece = game.board.squares[clicked_row][clicked_column].piece
                        # valid color
                        if piece.color == game.next_player:
                            game.board.calc_moves(piece,clicked_row,clicked_column,bool=True)
                            game.dragger.mouse_initial_pos(event.pos)
                            game.dragger.drag_piece(piece)
                            game.show_moves(screen)
                            game.show_pieces(screen)
                elif event.type == pygame.MOUSEMOTION:
                    if game.dragger.dragging:
                        game.dragger.mouse_pos(event.pos)
                        game.show_moves(screen)
                        game.show_pieces(screen)
                        game.dragger.update_blit(screen)
                elif event.type == pygame.MOUSEBUTTONUP:
                    if game.dragger.dragging:
                        game.dragger.mouse_pos(event.pos)
                        released_row = game.dragger.mouseY// square_size_v
                        released_column = game.dragger.mouseX// square_size_h
                        initial = Square(game.dragger.initial_row,game.dragger.initial_col)
                        final = Square(released_row,released_column)
                        move = Move(initial,final)

                        if game.board.valid_move(game.dragger.piece,move):
                            game.board.move(game.dragger.piece,move)
                            game.show_pieces(screen)
                            game.set_rect_background(screen)
                            game.next_turn()


                    game.dragger.undrag_piece()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        game.reset()
                        game = self.game
                        

                elif event.type == pygame.QUIT:
                    pygame.quit()
                    sys.quit()
            pygame.display.update()

main = Main()
main.main_loop()


