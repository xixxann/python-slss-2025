# Pygame Drawing
# Author: Angel Li
# 5 January 2026

import pygame


def game():
    pygame.init()

    # COLOURS - (R, G, B)
    # CONSTANTS ALL HAVE CAPS FOR THEIR NAMES
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    GREY = (128, 128, 128)
    BROWN = (150, 75, 0)

    # CONSTANTS
    WIDTH = 800
    HEIGHT = 600
    SIZE = (WIDTH, HEIGHT)

    # Creating the Screen
    screen = pygame.display.set_mode(SIZE)
    pygame.display.set_caption("Beautiful Drawing")

    # Variables
    done = False
    clock = pygame.time.Clock()

    # ------------ MAIN GAME LOOP
    while not done:
        # ------ MAIN EVENT LISTENER
        # when the user does something
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        # ------ GAME LOGIC

        # ------ DRAWING TO SCREEN
        screen.fill(WHITE)
        # # draw a red rectangle in the middle of the screen
        # pygame.draw.rect(screen, RED, (WIDTH / 2 - 100, HEIGHT / 2 - 40, 200, 80))
        # # draw a blue circle on top of the red rectangle
        # pygame.draw.circle(screen, BLUE, (WIDTH / 2, HEIGHT / 2 - 70), 30)

        # # draw 6 lines from the top middle to the middle right
        # # they repeat moving down the y-axis 10 px each
        # for offset in range(5):
        #     pygame.draw.line(
        #         screen,
        #         GREEN,
        #         (WIDTH / 2 + 20, 20 + offset * 10),
        #         (WIDTH - 20, HEIGHT / 2 - 20 + offset * 10),
        #     )

        # Draw a house
        # Draw the house building
        pygame.draw.rect(screen, BROWN, (WIDTH / 2 - 150, HEIGHT / 2 - 150, 300, 300))
        # Draw the door
        pygame.draw.rect(screen, RED, (WIDTH / 2 - 25, HEIGHT / 2 + 50, 50, 100))
        # Draw 2 windows
        pygame.draw.rect(screen, BLUE, (WIDTH / 2 - 100, HEIGHT / 2 - 75, 50, 50))
        pygame.draw.rect(screen, BLUE, (WIDTH / 2 + 50, HEIGHT / 2 - 75, 50, 50))
        # Draw the roof
        pygame.draw.polygon(
            screen,
            RED,
            (
                (WIDTH / 2 - 150, HEIGHT / 2 - 150),
                (WIDTH / 2 + 150, HEIGHT / 2 - 150),
                (WIDTH / 2, HEIGHT / 2 - 300),
            ),
        )

        # Update screen
        pygame.display.flip()

        # ------ CLOCK TICK
        clock.tick(60)  # 60 fps

    pygame.quit()


if __name__ == "__main__":
    game()
