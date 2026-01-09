# Collect Blocks
# Author: Angel Li
# Date: 7 January 2026

import random
from tkinter.constants import X, Y

import pygame


class Block(pygame.sprite.Sprite):
    def __init__(self, colour: pygame.Color, width: int, height: int):
        """A block of any colour"""
        super().__init__()

        # Visual representation of our image
        self.image = pygame.Surface((width, height))
        # change the colour of self.image
        self.image.fill(colour)

        # A Rect tells you two things:
        # - how big the hitbox is (width, height)
        # - where it is (x, y)
        self.rect = self.image.get_rect()
        self.rect.centerx = 100
        self.rect.centery = 100


class Mario(pygame.sprite.Sprite):
    def __init__(self):
        """The Player"""
        super().__init__()

        self.image = pygame.image.load("assets/mario-snes.png")
        self.rect = self.image.get_rect()

    def update(self):
        """Update Mario's location based on the mouse position"""
        self.rect.center = pygame.mouse.get_pos()


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("assets/goomba-nes.png")
        self.rect = self.image.get_rect()

        self.vel_x = 0
        self.vel_y = 0

    def update(self):
        # movement in the x-axis and y-axis
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y


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

    # CONSTANTS
    WIDTH = 800
    HEIGHT = 600
    SIZE = (WIDTH, HEIGHT)

    # Creating the Screen
    screen = pygame.display.set_mode(SIZE)
    pygame.display.set_caption("Collect Blocks")

    # Variables
    done = False
    clock = pygame.time.Clock()
    num_enemies = 5

    # Create a Sprte Group
    all_sprites_group = pygame.sprite.Group()
    block_sprites_group = pygame.sprite.Group()
    enemy_sprites_group = pygame.sprite.Group()

    # Create enemies
    for _ in range(num_enemies):
        enemy = Enemy()
        # Randomize movement
        random_x = random.choice([-5, -3, -1, 1, 3, 5])
        random_y = random.choice([-5, -3, -1, 1, 3, 5])
        enemy.vel_x, enemy.vel_y = random_x, random_y
        # Start them in the middle
        enemy.rect.center = (WIDTH / 2, HEIGHT / 2)

        all_sprites_group.add(enemy)
        enemy_sprites_group.add(enemy)

    # Create 100 blocks
    # Randomly place them throughout the screen
    for _ in range(100):
        block = Block(BLUE, 20, 10)
        # Chose a random position for it
        block.rect.centerx = random.randrange(0, WIDTH)
        block.rect.centery = random.randrange(0, HEIGHT)

        all_sprites_group.add(block)
        block_sprites_group.add(block)

    # Create a player
    player = Mario()
    player.rect.center = (WIDTH / 2, HEIGHT / 2)
    # Add the player to the sprite group
    all_sprites_group.add(player)

    # # Create a block
    # block_one = Block(BLUE, 20, 10)
    # # Move the block to the middle
    # block_one.rect.centerx = WIDTH / 2

    # # Add the block to the Sprite Group
    # all_sprites_group.add(block_one)

    # ------------ MAIN GAME LOOP
    while not done:
        # ------ MAIN EVENT LISTENER
        # when the user does something
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        # ------ GAME LOGIC
        all_sprites_group.update()

        # Keep enemies in screen
        for enemy in enemy_sprites_group:
            if enemy.rect.left < 0 or enemy.rect.right > WIDTH:
                enemy.vel_x = -enemy.vel_x
            if enemy.rect.top < 0 or enemy.rect.bottom > HEIGHT:
                enemy.vel_y = -enemy.vel_y

        # TODO: Check if Mario collides with a block
        blocks_collided = pygame.sprite.spritecollide(
            player,
            block_sprites_group,
            True,
        )
        # if the blocks_collided list has something in it
        # print Mario has collided with a block!
        if blocks_collided:
            print("---")
            print("Mario has collided with a block!")
            print(blocks_collided)

        # ------ DRAWING TO SCREEN
        screen.fill(WHITE)
        all_sprites_group.draw(screen)

        # Update screen
        pygame.display.flip()

        # ------ CLOCK TICK
        clock.tick(60)  # 60 fps

    pygame.quit()


if __name__ == "__main__":
    game()
