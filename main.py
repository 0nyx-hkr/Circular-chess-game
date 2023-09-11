import pygame
from constants import *
import sys
from game import Game


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
            game.set_rect_background(screen)
            game.show_pieces(screen)
            if game.dragger.dragging:
                game.dragger.update_blit(screen)
            for event  in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    game.dragger.mouse_pos(event.pos)
                    clicked_row = game.dragger.mouseY// square_size_v
                    clicked_column = game.dragger.mouseX// square_size_h
                    if game.board.squares[clicked_row][clicked_column].has_piece():
                        piece = game.board.squares[clicked_row][clicked_column].piece
                        game.dragger.mouse_initial_pos(event.pos)
                        game.dragger.drag_piece(piece)
                elif event.type == pygame.MOUSEMOTION:
                    if game.dragger.dragging:
                        game.dragger.mouse_pos(event.pos)
                        game.dragger.update_blit(screen)
                elif event.type == pygame.MOUSEBUTTONUP:
                    game.dragger.undrag_piece()

                elif event.type == pygame.QUIT:
                    pygame.quit()
                    sys.quit()
            pygame.display.update()

main = Main()
main.main_loop()


