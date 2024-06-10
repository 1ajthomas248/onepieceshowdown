"""
this files contains the Moves class and all the variables
that contain the moves used in the game
"""

import time
import pygame
import math
import button
import random

length, height = 800, 600
window = pygame.display.set_mode((length, height))

black = (0, 0, 0)
white = (255, 255, 255)
blue = (0, 0, 200)


def display_message(message):
    # draw a white box with black border
    pygame.draw.rect(window, white, (0, 410, 800, 250))
    pygame.draw.rect(window, blue, (0, 410, 800, 250), 3)

    # display the message
    font = pygame.font.Font('text/High Speed.ttf', 20)
    text = font.render(message, True, black)
    text_rect = text.get_rect()
    text_rect.x = 30
    text_rect.y = 450
    window.blit(text, text_rect)

    pygame.display.update()


class Moves:

    def __init__(self, name, damage, reset, character, atk_up, def_up, spd_up, eva_up, special, button):
        self.name = name
        self.damage = damage
        self.reset = reset
        self.character = character
        self.atk_up = atk_up
        self.def_up = def_up
        self.spd_up = spd_up
        self.eva_up = eva_up
        self.special = special
        self.button = button

    def use_move(self, fighter, opponent):
            x = random.randint(1, opponent.evasive)
            display_message(f'{self.character} used {self.name}!')
            if x > 10 and self.damage > 0:
                self.damage = 0
                display_message(f'{self.character} used {self.name}!')
                time.sleep(1)
                display_message(f'{self.character} missed!')
            if self.special == 1 and opponent.df == True:
                self.damage += 20
            if self.special == 2:
                display_message(f'{self.character} used {self.name}!')
                fighter.current_hp += 25
                display_message(f'{self.character} healed some HP!')
                time.sleep(1)
            opponent.current_hp -= math.floor(self.damage * fighter.attack / opponent.defense)
            self.damage = self.reset
            if opponent.current_hp < 0:
                opponent.current_hp = 0
            time.sleep(1)

            if self.atk_up != 1:
                if self.atk_up > 1:
                    fighter.attack *= self.atk_up
                    display_message(f"{self.character}'s attack rose!")
                    time.sleep(1)
                if self.atk_up < 1:
                    fighter.attack *= self.atk_up
                    display_message(f"{self.character}'s attack dropped!")
                    time.sleep(1)
            if self.def_up != 1:
                if self.def_up > 1:
                    fighter.defense *= self.def_up
                    display_message(f"{self.character}'s defense rose!")
                    time.sleep(1)
                if self.def_up < 1:
                    fighter.defense *= self.def_up
                    display_message(f"{self.character}'s defense dropped!")
                    time.sleep(1)
            if self.spd_up != 1:
                if self.spd_up > 1:
                    fighter.speed *= self.spd_up
                    display_message(f"{self.character}'s speed rose!")
                    time.sleep(1)
                if self.spd_up < 1:
                    fighter.speed *= self.spd_up
                    display_message(f"{self.character}'s speed dropped!")
                    time.sleep(1)
            if self.eva_up != 1:
                if self.eva_up > 1:
                    fighter.evasive += 2
                    display_message(f"{self.character}'s evasiveness rose!")
                    time.sleep(1)
                if self.eva_up < 1:
                    fighter.evasive -= 2
                    display_message(f"{self.character}'s evasiveness dropped!")
                    time.sleep(1)


# moves

gatling1 = Moves('Gomu Gomu no Gatling', 50, 50, 'Luffy', 1, .8, 1, 1, 0, button.gatling_button)
redhawk1 = Moves('Gomu Gomu no Red Hawk', 60, 60, 'Luffy', .8, 1, 1, 1, 0, button.redhawk_button)
battleaxe1 = Moves('Gomu Gomu no Battle Axe', 45, 45, 'Luffy', 1, 1, 1, 1, 0, button.battleaxe_button)
armament1 = Moves('Armament Haki', 0, 0, 'Luffy', 1.25, 1.25, 1, 1, 0, button.armament_button)
cannon1 = Moves('Bara Bara no Cannon', 40, 40, 'Buggy', 1, 1, 1, 1, 0, button.cannon_button)
festival1 = Moves('Bara Bara no Festival', 50, 50, 'Buggy', 1, 1, 1, 1, 0, button.festival_button)
bomb1 = Moves('Buggy Bomb', 65, 65, 'Buggy', 1, .8, .8, 1, 0, button.bomb_button)
escape1 = Moves('Bara Bara no Emergency Escape', 0, 0, 'Buggy', 1, 1, 1.25, 1.25, 0, button.escape_button)
whiteout1 = Moves('White Out', 20, 20, 'Smoker', 1, 1, 1, 1.24, 0, button.whiteout_button)
launcher1 = Moves('White Launcher', 35, 35, 'Smoker', 1, 1, 1.25, 1, 0, button.launcher_button)
blow1 = Moves('White Blow', 45, 45, 'Smoker', 1, 1, 1, 1, 0, button.blow_button)
swing1 = Moves('Brutal Jitte Swing', 40, 40, 'Smoker', 1, 1, 1, 1, 1, button.swing_button)
mizu1 = Moves('Shoryo no Mizu', 45, 45, 'Arlong', 1, 1, 1, 1, 0, button.mizu_button)
darts1 = Moves('Shark Darts', 30, 30, 'Arlong', 1, 1, 1.25, 1, 0, button.darts_button)
tooth1 = Moves('Tooth Attack', 15, 15, 'Arlong', 1.25, 1, 1, 1, 0, button.tooth_button)
kiribachi1 = Moves('Kiribachi Slice', 55, 55, 'Arlong', 1, 1, .8, 1, 0, button.kiribachi_button)

# boss moves
blast = Moves('Blast Breath', 60, 60, 'Zoan Kaido', 1, 1, 1, 1, 0, None)
twister = Moves('Dragon Twister', 50, 50, 'Zoan Kaido', 1, 1, 1.25, 1, 0, None)
gust = Moves('Demolition Gust', 55, 55, 'Zoan Kaido', 1, 1, 1, 1, 0, None)
crunch = Moves('Zoan Crunch', 45, 45, 'Zoan Kaido', 1, 1, 1, 1, 0, None)
thunder = Moves('Thunder Bagua', 55, 55, 'Kaido', 1, 1, 1, 1, 0, None)
smash = Moves('Downward Smash', 45, 45, 'Kaido', 1, 1, 1, 1, 0, None)
future = Moves('Future Sight', 0, 0, 'Kaido', 1, 1, 1, 1.24, 0, None)
drink = Moves('Sake Overflow', 0, 0, 'Kaido', 1, 1, 1, 1, 2, None)
color = Moves('Color of the Supreme King', 0, 0, 'Man Beast Kaido', 1.3, 1.1, 1, 1, 0, None)
conqueror = Moves("Conqueror of Three World's Ragnaraku ", 80, 80, 'Man Beast Kaido', 1, 1, 1, 1, 0, None)
bagua = Moves('Destroyer of Death Thunder Bagua', 70, 70, 'Man Beast Kaido', 1, 1, 1, 1, 0, None)
arrow = Moves('Varja Arrow', 55, 55, 'Man Beast Kaido', 1, 1, 1, 1, 0, None)