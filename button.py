"""
this file contains the Button class and all the variables
that contain the buttons for the game
"""
import pygame
import pics

# button.py

import pygame

class Button():
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    def draw(self, surface):
        action = False

        # get mouse position
        pos = pygame.mouse.get_pos()

        # check mouseover and clicked conditions
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        # draw button on screen
        surface.blit(self.image, (self.rect.x, self.rect.y))

        return action

    def clear_events():
        pygame.event.clear()



# button
start_button = Button(200, 330, pics.start_image, .9)
solo_button = Button(70, 260, pics.solo_image, .9)
squad_button = Button(70, 370, pics.squad_image, .9)
boss_button = Button(70, 480, pics.boss_image, .9)
yes_button = Button(164, 151, pics.yes, 1)
no_button = Button(500, 151, pics.no, 1)
fight_button = Button(0, 410, pics.fight, 1)
switch_button = Button(40, 355, pics.switch, .7)

# fighters
luffy_button = Button(183, 141, pics.luffy_image, .4)
buggy_button = Button(461, 141, pics.buggy_image, .4)
smoker_button = Button(183, 332, pics.smoker_image, .4)
arlong_button = Button(461, 332, pics.arlong_image, .4)
luffy_switch = Button(60, 69, pics.luffy_switch, .7)
buggy_switch = Button(60, 69, pics.buggy_switch, .7)
smoker_switch = Button(60, 69, pics.smoker_switch, .7)
arlong_switch = Button(60, 69, pics.arlong_switch, .7)

# moves
redhawk_button = Button(0, 410, pics.red_hawk, 1)
gatling_button = Button(400, 410, pics.gatling, 1)
battleaxe_button = Button(0, 505, pics.battleaxe, 1)
armament_button = Button(400, 505, pics.armament, 1)
cannon_button = Button(0, 410, pics.cannon, 1)
festival_button = Button(400, 410, pics.festival, 1)
bomb_button = Button(0, 505, pics.bomb, 1)
escape_button = Button(400, 505, pics.escape, 1)
whiteout_button = Button(0, 410, pics.whiteout, 1)
launcher_button = Button(400, 410, pics.launcher, 1)
blow_button = Button(0, 505, pics.blow, 1)
swing_button = Button(400, 505, pics.swing, 1)
mizu_button = Button(0, 410, pics.mizu, 1)
darts_button = Button(400, 410, pics.darts, 1)
tooth_button = Button(0, 505, pics.tooth, 1)
kiribachi_button = Button(400, 505, pics.kiribachi, 1)