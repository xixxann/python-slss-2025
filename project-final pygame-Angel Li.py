# Trying Code
# Author: Angel Li
# Date: Jan 14

import random

import pygame

# COLOURS - (R, G, B)
# CONSTANTS ALL HAVE CAPS FOR THEIR NAMES
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GREY = (128, 128, 128)


class Cookie(pygame.sprite.Sprite):
    def __init__(self):
        """The player"""
        super().__init__()

        # Right version of Cookie and Left version
        self.image_right = pygame.image.load("assets/mcookie.png")
        self.image_right = pygame.transform.scale_by(self.image_right, 0.3)
        self.image_left = pygame.transform.flip(self.image_right, True, False)

        self.image = self.image_right
        self.rect = self.image.get_rect()

        self.previous_x = 0
        self.points = 0
        self.health = 100

    def calc_damage(self, amt: int) -> int:
        """Decrease player health by amt
        Returns:
            Remaining health"""
        self.health -= amt
        return self.health

    def calc_health(self, amt: int) -> int:
        """Increase player health by amt
        Returns:
            Remaining health"""
        self.health += amt
        return self.health

    def incr_score(self, amt: int) -> int:
        """Increases player score by amt
        Returns:
            Score"""
        self.points += amt
        return self.points

    def get_damage_percentage(self) -> float:
        return self.health / 100

    def update(self):
        """Update Cookie's location based on the mouse pos
        Update Cookie's image based on where he's going"""
        self.rect.center = pygame.mouse.get_pos()

        # If Cookie's previous x less than current x
        #   Then Cookie is facing Right
        # If Cookie's previous x is greater than current x
        #   Then Cookie is facing Left
        if self.previous_x < self.rect.x:
            self.image = self.image_right
        elif self.previous_x > self.rect.x:
            self.image = self.image_left

        self.previous_x = self.rect.x


class Coin(pygame.sprite.Sprite):
    def __init__(self):
        """A coin"""
        super().__init__()

        self.imageold = pygame.image.load("assets/coin.png")
        self.image = pygame.transform.scale_by(self.imageold, 0.02)

        self.rect = self.image.get_rect()
        self.rect.centerx = 100
        self.rect.centery = 100

        self.point_value = 1

    def level_up(self, val: int):
        """Incr point value"""
        self.point_value *= val


class Potion(pygame.sprite.Sprite):
    def __init__(self):
        """A Potion to gain health status"""
        super().__init__()

        self.imageold = pygame.image.load("assets/potion.png")
        self.image = pygame.transform.scale_by(self.imageold, 0.2)
        self.rect = self.image.get_rect()

        self.vel_x = 0
        self.vel_y = 0

        self.rect.centerx = 100
        self.rect.centery = 100

        self.health = 20

    def update(self):
        # movement in the x- and y-axis
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        """An easy enemy"""
        super().__init__()

        self.imageold = pygame.image.load("assets/enemy1.png")
        self.image = pygame.transform.scale_by(self.imageold, 0.3)

        self.vel_x = 0
        self.vel_y = 0

        self.rect = self.image.get_rect()

        self.damage = 1

    def update(self):
        # movement in the x- and y-axis
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y

    def level_up(self):
        # increase damage
        self.damage *= 1.5


class Enemy2(pygame.sprite.Sprite):
    def __init__(self):
        """A harder enemy"""
        super().__init__()

        self.imageold = pygame.image.load("assets/enemy2.png")
        self.image = pygame.transform.scale_by(self.imageold, 0.4)

        self.vel_x = 0
        self.vel_y = 0

        self.damage = 2

        self.rect = self.image.get_rect()

    def update(self):
        # movement in the x- and y-axis
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y

    def level_up(self):
        # increase damage
        self.damage *= 2


class HealthBar(pygame.Surface):
    def __init__(self, width: int, height: int):
        self._width = width
        self._height = height
        super().__init__((width, height))

        self.fill(RED)

    def update_info(self, percentage: float):
        """Updates the healthbar with the given percentage"""
        self.fill(RED)
        pygame.draw.rect(self, GREEN, (0, 0, percentage * self._width, self._height))


def game():
    pygame.init()

    # CONSTANTS
    WIDTH = 800
    HEIGHT = 600
    SIZE = (WIDTH, HEIGHT)

    # Creating the Screen
    screen = pygame.display.set_mode(SIZE)
    pygame.display.set_caption("Final Project")

    # Variables
    done = False
    clock = pygame.time.Clock()
    num_enemies = 1
    level = 1
    health_bar = HealthBar(200, 10)
    num_potions = 1
    num_coins = random.randint(50, 100)

    # Create a Sprite Group
    all_sprites_group = pygame.sprite.Group()
    enemy_sprites_group = pygame.sprite.Group()
    coin_sprites_group = pygame.sprite.Group()
    potion_sprites_group = pygame.sprite.Group()

    # Create a player
    player = Cookie()
    player.rect.center = (WIDTH / 2, HEIGHT / 2)

    all_sprites_group.add(player)

    # Create a potion
    for _ in range(num_potions):
        potion = Potion()
        random_x = random.choice([-5, -3, -1, 1, 3, 5])
        random_y = random.choice([-5, -3, -1, 1, 3, 5])
        potion.vel_x, potion.vel_y = random_x, random_y
        potion.rect.center = (WIDTH / 2, HEIGHT / 2)

        all_sprites_group.add(potion)
        potion_sprites_group.add(potion)

    # Create blocks and place them throughout the screen
    for _ in range(num_coins):
        coin = Coin()
        # Choose a random position for it
        coin.rect.centerx = random.randrange(0, WIDTH)
        coin.rect.centery = random.randrange(0, HEIGHT)

        all_sprites_group.add(coin)
        coin_sprites_group.add(coin)

    # Create Enemy #1
    for _ in range(num_enemies):
        # Create an enemy
        enemy = Enemy()
        # Randomize Movement
        random_x = random.choice([-5, -3, -1, 1, 3, 5])
        random_y = random.choice([-5, -3, -1, 1, 3, 5])
        enemy.vel_x, enemy.vel_y = random_x, random_y
        # Start at random position at the top of the screen
        enemy.rect.centerx = random.randrange(0, WIDTH - 100)

        all_sprites_group.add(enemy)
        enemy_sprites_group.add(enemy)

    # Create Enemy #2
    for _ in range(num_enemies):
        enemy2 = Enemy2()
        # Randomize Movement
        random_x = random.choice([-7, -5, 5, 7])
        random_y = random.choice([-7, -5, 5, 7])
        enemy2.vel_x, enemy2.vel_y = random_x, random_y
        # Start in the middle of the screen
        enemy2.rect.center = (WIDTH / 2, HEIGHT / 2)

        all_sprites_group.add(enemy2)
        enemy_sprites_group.add(enemy2)

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

        # Keep potion in screen
        for potion in potion_sprites_group:
            if potion.rect.left < 0 or potion.rect.right > WIDTH:
                potion.vel_x = -potion.vel_x
            if potion.rect.top < 0 or potion.rect.bottom > HEIGHT:
                potion.vel_y = -potion.vel_y

        # Collision between Player and Coins
        coins_collided = pygame.sprite.spritecollide(player, coin_sprites_group, True)
        # print Cookie has gained with a coin!
        for coin in coins_collided:
            if type(coin) is Coin:
                print("Player score: ", player.incr_score(coin.point_value))

        # Fill blocks if block list is empty
        # Add more blocks and add 2 enemies
        if not coin_sprites_group:
            level += 1

            for _ in range(num_coins):
                coin = Coin()
                # Choose a random position for it
                coin.rect.centerx = random.randrange(0, WIDTH)
                coin.rect.centery = random.randrange(0, HEIGHT)

                coin.level_up(level)

                all_sprites_group.add(coin)
                coin_sprites_group.add(coin)

            enemy = Enemy()
            random_x = random.choice([-5, -3, -1, 1, 3, 5])
            random_y = random.choice([-5, -3, -1, 1, 3, 5])
            enemy.vel_x, enemy.vel_y = random_x, random_y
            # Start at random position at the top of the screen
            enemy.rect.centerx = random.randrange(0, WIDTH - 100)
            all_sprites_group.add(enemy)
            enemy_sprites_group.add(enemy)

            for enemy in enemy_sprites_group:
                enemy.level_up()

            enemy2 = Enemy2()
            random_x = random.choice([-7, -5, 5, 7])
            random_y = random.choice([-7, -5, 5, 7])
            enemy2.vel_x, enemy2.vel_y = random_x, random_y
            # Start in the middle of the screen
            enemy2.rect.center = (WIDTH / 2, HEIGHT / 2)
            all_sprites_group.add(enemy2)
            enemy_sprites_group.add(enemy2)

            for enemy2 in enemy_sprites_group:
                enemy2.level_up()

            potion = Potion()
            potion.rect.centerx = 100
            potion.rect.centery = 100
            all_sprites_group.add(potion)
            potion_sprites_group.add(potion)

        # Collision between Player and Enemies
        enemies_collided = pygame.sprite.spritecollide(
            player, enemy_sprites_group, False
        )
        for enemy in enemies_collided:
            # decrease Cookie's life
            player.calc_damage(enemy.damage)

        for enemy2 in enemies_collided:
            # decrease Cookie's life
            player.calc_damage(enemy2.damage)

        health_bar.update_info(player.get_damage_percentage())

        # Collision between Player and Potion
        potion_collided = pygame.sprite.spritecollide(
            player, potion_sprites_group, True
        )
        for potion in potion_collided:
            # increase Cookie's ife
            player.calc_health(potion.health)

        health_bar.update_info(player.get_damage_percentage())

        # Game ends when Player's health is zero or less
        if player.health <= 0:
            done = True

        # ------ DRAWING TO SCREEN
        screen.fill(WHITE)
        all_sprites_group.draw(screen)
        screen.blit(health_bar, (10, 10))

        # Update screen
        pygame.display.flip()

        # ------ CLOCK TICK
        clock.tick(60)  # 60 fps

    # Display final score:
    print("Thanks for playing!")
    print("Final score is:", player.points)

    pygame.quit()


if __name__ == "__main__":
    game()
