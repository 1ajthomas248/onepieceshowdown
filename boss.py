import random
import fighters
import pygame
import moves
import pics

black = (0, 0, 0)
white = (255, 255, 255)
blue = (0, 0, 200)
red = (152, 5, 5)
green = (26, 100, 5)


class Boss:

    def __init__(self, name, max_hp, current_hp, attack, defense, speed, evasive,
                 move1, move2, move3, move4, x, y,  hp_x, hp_y, sprite, df):
        # Pokemon stats
        self.name = name
        self.max_hp = max_hp
        self.current_hp = current_hp
        self.attack = attack
        self.defense = defense
        self.speed = speed
        self.evasive = evasive
        self.df = df
        # moves
        self.move1 = move1
        self.move2 = move2
        self.move3 = move3
        self.move4 = move4

        # sprites
        self.sprite = sprite
        self.x = x
        self.y = y

        # HP
        self.hp_x = hp_x
        self.hp_y = hp_y

    def ai(self, p1, p2):
        computer = random.randint(1, 4)
        if computer == 1:
            self.move1.use_move(p1, p2)
        if computer == 2:
            self.move2.use_move(p1, p2)
        if computer == 3:
            self.move3.use_move(p1, p2)
        if computer == 4:
            self.move4.use_move(p1, p2)

    def set_sprite(self):

        # set the pokemon's sprite
        if self.name == fighters.rival_state:
            fighters.window.blit(self.sprite, (self.x, self.y))

    def draw_hp(self):

        # display the health bar
        bar_scale = 200 // self.max_hp
        for i in range(self.max_hp):
            bar = (self.hp_x + bar_scale * i, self.hp_y, bar_scale, 20)
            pygame.draw.rect(fighters.window, red, bar)

        for i in range(self.current_hp):
            bar = (self.hp_x + bar_scale * i, self.hp_y, bar_scale, 20)
            pygame.draw.rect(fighters.window, green, bar)

        # display "HP" text
        font = pygame.font.Font('text/High Speed.ttf', 12)
        text = font.render(f'HP: {self.current_hp} / {self.max_hp}', True, white)
        text_rect = text.get_rect()
        text_rect.x = self.hp_x - 30
        text_rect.y = self.hp_y
        fighters.window.blit(text, text_rect)


zoan = Boss('Zoan Kaido', 200, 200, 1, 1, 110, 1, moves.blast, moves.twister, moves.crunch,
            moves.gust, 448, 24, 530, 270, pics.zoan_sprite, True)
kaido = Boss('Kaido', 200, 200, 1, 1, 110, 1, moves.future, moves.thunder, moves.drink,
             moves.smash, 448, 24, 530, 270, pics.kaido_sprite, True)
beast = Boss('Man Beast Kaido', 200, 200, 1, 1.1, 125, 1, moves.color, moves.conqueror, moves.bagua,
             moves.arrow, 448, 24, 530, 280, pics.beast_sprite, True)
