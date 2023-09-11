import pygame
import math

# Constants
SCREEN_SIZE = (600, 600)
RADIUS = 250
NUM_ROWS = 8
NUM_COLS = 8
SQUARE_SIZE = 2 * RADIUS // max(NUM_ROWS, NUM_COLS)

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
LIGHT_COLOR = (225, 225, 225)
DARK_COLOR = (100, 100, 100)

def draw_chess_board(screen, center):
    for row in range(NUM_ROWS):
        for col in range(NUM_COLS):
            angle = math.pi * 2 / NUM_COLS * col
            distance = RADIUS - SQUARE_SIZE // 2 - (row * SQUARE_SIZE)
            x = center[0] + int(distance * math.cos(angle))
            y = center[1] + int(distance * math.sin(angle))

            # Check if the square should be light or dark
            if (row + col) % 2 == 0:
                color = LIGHT_COLOR
            else:
                color = DARK_COLOR

            pygame.draw.rect(screen, color, (x - SQUARE_SIZE // 2, y - SQUARE_SIZE // 2, SQUARE_SIZE, SQUARE_SIZE))

def main():
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE)
    pygame.display.set_caption("Circular Chess Board")
    
    clock = pygame.time.Clock()
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(WHITE)
        center = (SCREEN_SIZE[0] // 2, SCREEN_SIZE[1] // 2)
        pygame.draw.circle(screen, BLACK, center, RADIUS, 3)
        draw_chess_board(screen, center)
        
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
