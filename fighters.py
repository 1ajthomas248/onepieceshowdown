"""
this file contains the Fighters class and variables
that contain all fighters in the game
"""

import pygame
import random
import button
import moves
import pics
import boss

length, height = 800, 600
window = pygame.display.set_mode((length, height))

black = (0, 0, 0)
white = (255, 255, 255)
blue = (0, 0, 200)
red = (152, 5, 5)
green = (26, 100, 5)

menu_state = "mode"
start_menu = True
mode_menu = False
character_select = False
boss1 = False
squad = False
fighter_state = ''
opponent_state = ''
captain_state = ''
crew_state = ''
rival_state = ''
rcrew_state = ''
temp = ''
p1 = ''
p2 = ''
boss_crew = [boss.zoan, boss.kaido, boss.beast]
characters = []
crew = []
rival_crew = []

class Fighters:

    def __init__(self, name, max_hp, current_hp, attack, defense, speed, evasive, button1, button2, button3, button4,
                 switch, move1, move2, move3, move4, x, y, x2, y2, hp_x, hp_y, hp_x2, hp_y2, frontsprite, backsprite, df):
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

        # buttons
        self.button1 = button1
        self.button2 = button2
        self.button3 = button3
        self.button4 = button4
        self.switch = switch

        # sprites
        self.frontsprite = frontsprite
        self.backsprite = backsprite
        self.x = x
        self.y = y
        self.x2 = x2
        self.y2 = y2

        # HP
        self.hp_x = hp_x
        self.hp_y = hp_y
        self.hp_x2 = hp_x2
        self.hp_y2 = hp_y2

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
        if self.name == fighter_state:
            window.blit(self.backsprite, (self.x, self.y))
        if self.name == captain_state:
            window.blit(self.backsprite, (self.x, self.y))
        if self.name == opponent_state:
            window.blit(self.frontsprite, (self.x2, self.y2))
        if self.name == rival_state:
            window.blit(self.frontsprite, (self.x2, self.y2))


    
    def draw_hp(self):

        if self.name == fighter_state:
            self.hp_x = self.hp_x
            self.hp_y = self.hp_y
        if self.name == captain_state:
            self.hp_x = self.hp_x
            self.hp_y = self.hp_y
        if self.name == opponent_state:
            self.hp_x = self.hp_x2
            self.hp_y = self.hp_y2
        if self.name == rival_state:
            self.hp_x = self.hp_x2
            self.hp_y = self.hp_y2

        # display the health bar
        bar_scale = 200 // self.max_hp
        for i in range(self.max_hp):
            bar = (self.hp_x + bar_scale * i, self.hp_y, bar_scale, 20)
            pygame.draw.rect(window, red, bar)

        for i in range(self.current_hp):
            bar = (self.hp_x + bar_scale * i, self.hp_y, bar_scale, 20)
            pygame.draw.rect(window, green, bar)

        # display "HP" text
        font = pygame.font.Font('text/High Speed.ttf', 12)
        if self.name == fighter_state:
            text = font.render(f'HP: {self.current_hp} / {self.max_hp}', True, white)
            text_rect = text.get_rect()
            text_rect.x = self.hp_x - 30
            text_rect.y = self.hp_y
            window.blit(text, text_rect)
        if self.name == captain_state:
            text = font.render(f'HP: {self.current_hp} / {self.max_hp}', True, white)
            text_rect = text.get_rect()
            text_rect.x = self.hp_x - 30
            text_rect.y = self.hp_y
            window.blit(text, text_rect)
        if self.name == opponent_state:
            text = font.render(f'HP', True, white)
            text_rect = text.get_rect()
            text_rect.x = self.hp_x - 30
            text_rect.y = self.hp_y
            window.blit(text, text_rect)
        if self.name == rival_state:
            text = font.render(f'HP', True, white)
            text_rect = text.get_rect()
            text_rect.x = self.hp_x - 30
            text_rect.y = self.hp_y
            window.blit(text, text_rect)


# fighters
luffy1 = Fighters('Luffy', 150, 150, 1, 1, 100, 1, button.redhawk_button,
                 button.gatling_button, button.battleaxe_button, button.armament_button, button.luffy_switch,
                 moves.redhawk1, moves.gatling1, moves.battleaxe1, moves.armament1, 158,
                 190, 490, 85, 205, 376, 550, 269, pics.luffy_frontsprite, pics.luffy_backsprite, True)

buggy1 = Fighters('Buggy', 150, 150, 1, 1, 85, 1, button.cannon_button,
                 button.festival_button, button.bomb_button, button.escape_button, button.buggy_switch,moves.cannon1,
                 moves.festival1, moves.bomb1, moves.escape1, 151, 178, 495, 75, 210, 373, 575, 280,
                 pics.buggy_frontsprite, pics.buggy_backsprite, True)

smoker1 = Fighters('Smoker', 150, 150, 1, 1, 90, 1, button.whiteout_button,
                 button.launcher_button, button.blow_button, button.swing_button, button.smoker_switch,
                 moves.whiteout1, moves.launcher1, moves.blow1, moves.swing1, 156,
                 170, 505, 65, 205, 373, 550, 265, pics.smoker_frontsprite, pics.smoker_backsprite, True)

arlong1 = Fighters('Arlong', 150, 150, 1, 1, 95, 1, button.mizu_button,
                     button.darts_button, button.tooth_button, button.kiribachi_button, button.arlong_switch,
                     moves.mizu1, moves.darts1, moves.tooth1, moves.kiribachi1, 140,
                     150, 480, 35, 194, 373, 530, 260, pics.arlong_frontsprite, pics.arlong_backsprite, False)

luffy_reset = Fighters('Luffy', 150, 150, 1, 1, 100, 1, button.redhawk_button,
                 button.gatling_button, button.battleaxe_button, button.armament_button, button.luffy_switch,
                 moves.redhawk1, moves.gatling1, moves.battleaxe1, moves.armament1, 158,
                 190, 490, 85, 205, 376, 550, 269, pics.luffy_frontsprite, pics.luffy_backsprite, True)

buggy_reset = Fighters('Buggy', 150, 150, 1, 1, 85, 1, button.cannon_button,
                 button.festival_button, button.bomb_button, button.escape_button, button.buggy_switch,moves.cannon1,
                 moves.festival1, moves.bomb1, moves.escape1, 151, 178, 495, 75, 210, 373, 575, 280,
                 pics.buggy_frontsprite, pics.buggy_backsprite, True)

smoker_reset = Fighters('Smoker', 150, 150, 1, 1, 90, 1, button.whiteout_button,
                 button.launcher_button, button.blow_button, button.swing_button, button.smoker_switch,
                 moves.whiteout1, moves.launcher1, moves.blow1, moves.swing1, 156,
                 170, 505, 65, 205, 373, 550, 265, pics.smoker_frontsprite, pics.smoker_backsprite, True)

arlong_reset = Fighters('Arlong', 160, 160, 1, 1, 95, 1, button.mizu_button,
                     button.darts_button, button.tooth_button, button.kiribachi_button, button.arlong_switch,
                     moves.mizu1, moves.darts1, moves.tooth1, moves.kiribachi1, 140,
                     150, 480, 35, 194, 373, 530, 260, pics.arlong_frontsprite, pics.arlong_backsprite, False)

