import pygame
import button
import time
import pics
import moves
import fighters
import battle

pygame.init()
pygame.font.init()
pygame.mixer.init()

length, height = 800, 600
window = pygame.display.set_mode((length, height))
pygame.display.set_caption('One Piece Showdown!')

# colors
white = (255, 255, 255)
black = (0, 0, 0)
blue = (0, 0, 200)
red = (255, 0, 0)
green = (15, 54, 5)

# misc
fps = 60
font = pygame.font.SysFont('text/High Speed.ttf', 40)
# onepiece_logo coors (161, 102)

# game variables
menu_state = "mode"
start_menu = True
mode_menu = False
character_select = False
squad = False
fighters.fighter_state = ''
fighters.opponent_state = ''
p1 = ''
p2 = ''


# music
if menu_state == 'mode':
    pygame.mixer.music.load('audio/We-Are.ogg')
    pygame.mixer.music.play(-1)
elif menu_state == 'fight':
    pygame.mixer.music.stop()
    pygame.mixer.music.unload()
    pygame.mixer.music.load('audio/FightTheme.ogg')
    pygame.mixer.music.play(-1)

luffy = fighters.luffy1
buggy = fighters.buggy1
smoker = fighters.smoker1
arlong = fighters.arlong1
characters = [luffy, buggy, smoker, arlong]



clock = pygame.time.Clock()
running = True

while running:
    clock.tick(fps)
    window.blit(pics.background, (0, 0))

    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            button.Button.clear_events()
            running = False
            # start game
        if events.type == pygame.KEYDOWN:
            if events.key == pygame.K_SPACE:
                button.Button.clear_events()
                mode_menu = True

    # check if game has started
    if mode_menu:
        # check menu state
        if fighters.menu_state == 'mode':

            # draw mode screen buttons
            window.blit(pics.background_select, (0, 0))
            if button.solo_button.draw(window):
                fighters.menu_state = 'characters'
                button.Button.clear_events()
            if button.squad_button.draw(window):
                fighters.menu_state = 'captain'
                fighters.squad = True
                button.Button.clear_events()
            if button.boss_button.draw(window):
                fighters.menu_state = 'captain'
                fighters.boss1 = True
                fighters.squad = True
                button.Button.clear_events()
        
        # check character screen state
        if fighters.menu_state == 'characters':
            window.blit(pics.background_character, (0, 0))
            button.Button.clear_events()
            if button.luffy_button.draw(window):
                fighters.fighter_state = 'Luffy'
                fighters.menu_state = 'opponent'
                button.Button.clear_events()

            if button.buggy_button.draw(window):
                fighters.fighter_state = 'Buggy'
                fighters.menu_state = 'opponent'
                button.Button.clear_events()

            if button.smoker_button.draw(window):
                fighters.fighter_state = 'Smoker'
                fighters.menu_state = 'opponent'
                button.Button.clear_events()

            if button.arlong_button.draw(window):
                fighters.fighter_state = 'Arlong'
                fighters.menu_state = 'opponent'
                button.Button.clear_events()

            battle.reset_fighters()
            characters = [luffy, buggy, smoker, arlong]

            for i in characters:
                if i.name == fighters.fighter_state:
                    fighters.p1 = i

        if fighters.menu_state == 'captain':
            window.blit(pics.background_captain, (0, 0))
            button.Button.clear_events()
            if button.luffy_button.draw(window):
                fighters.captain_state = 'Luffy'
                if fighters.boss1 == True:
                    fighters.menu_state = 'boss crew'
                else:
                    fighters.menu_state = 'crew'
                    button.Button.clear_events()

            if button.buggy_button.draw(window):
                fighters.captain_state = 'Buggy'
                if fighters.boss1 == True:
                    fighters.menu_state = 'boss crew'
                else:
                    fighters.menu_state = 'crew'
                    button.Button.clear_events()

            if button.smoker_button.draw(window):
                fighters.captain_state = 'Smoker'
                if fighters.boss1 == True:
                    fighters.menu_state = 'boss crew'
                else:
                    fighters.menu_state = 'crew'
                    button.Button.clear_events()

            if button.arlong_button.draw(window):
                fighters.captain_state = 'Arlong'
                if fighters.boss1 == True:
                    fighters.menu_state = 'boss crew'
                else:
                    fighters.menu_state = 'crew'
                    button.Button.clear_events()

            battle.reset_fighters()
            characters = [luffy, buggy, smoker, arlong]

            for i in characters:
                if i.name == fighters.captain_state:
                    fighters.crew.append(i)

        if fighters.menu_state == 'boss crew':
            window.blit(pics.background_crew, (0, 0))
            button.Button.clear_events()
            battle.reset_fighters()

            if button.luffy_button.draw(window):
                fighters.crew.append(luffy)
                button.Button.clear_events()
            if button.buggy_button.draw(window):
                fighters.crew.append(buggy)
                button.Button.clear_events()
            if button.smoker_button.draw(window):
                fighters.crew.append(smoker)
                button.Button.clear_events()
            if button.arlong_button.draw(window):
                fighters.crew.append(arlong)
                button.Button.clear_events()

            if len(fighters.crew) == 4:
                fighters.menu_state = 'squadset'

        if fighters.menu_state == 'crew':
            window.blit(pics.background_crew, (0, 0))
            button.Button.clear_events()
            if button.luffy_button.draw(window):
                fighters.crew_state = 'Luffy'
                fighters.menu_state = 'rival'
                button.Button.clear_events()

            if button.buggy_button.draw(window):
                fighters.crew_state = 'Buggy'
                fighters.menu_state = 'rival'
                button.Button.clear_events()

            if button.smoker_button.draw(window):
                fighters.crew_state = 'Smoker'
                fighters.menu_state = 'rival'
                button.Button.clear_events()

            if button.arlong_button.draw(window):
                fighters.crew_state = 'Arlong'
                fighters.menu_state = 'rival'
                button.Button.clear_events()

            battle.reset_fighters()
            characters = [luffy, buggy, smoker, arlong]

            for i in characters:
                if i.name == fighters.crew_state:
                    fighters.crew.append(i)

        if fighters.menu_state == 'rival':
            window.blit(pics.background_opponent, (0, 0))
            button.Button.clear_events()
            if button.luffy_button.draw(window):
                fighters.rival_state = 'Luffy'
                fighters.menu_state = 'rcrew'
                button.Button.clear_events()

            if button.buggy_button.draw(window):
                fighters.rival_state = 'Buggy'
                fighters.menu_state = 'rcrew'
                button.Button.clear_events()

            if button.smoker_button.draw(window):
                fighters.rival_state = 'Smoker'
                fighters.menu_state = 'rcrew'
                button.Button.clear_events()

            if button.arlong_button.draw(window):
                fighters.rival_state = 'Arlong'
                fighters.menu_state = 'rcrew'
                button.Button.clear_events()

            battle.reset_fighters()
            characters = [luffy, buggy, smoker, arlong]

            for i in characters:
                if i.name == fighters.rival_state:
                    fighters.rival_crew.append(i)

        if fighters.menu_state == 'rcrew':
            window.blit(pics.background_rivalcrew, (0, 0))
            button.Button.clear_events()
            if button.luffy_button.draw(window):
                fighters.rcrew_state = 'Luffy'
                fighters.menu_state = 'squadset'
                button.Button.clear_events()

            if button.buggy_button.draw(window):
                fighters.rcrew_state = 'Buggy'
                fighters.menu_state = 'squadset'
                button.Button.clear_events()

            if button.smoker_button.draw(window):
                fighters.rcrew_state = 'Smoker'
                fighters.menu_state = 'squadset'
                button.Button.clear_events()

            if button.arlong_button.draw(window):
                fighters.rcrew_state = 'Arlong'
                fighters.menu_state = 'squadset'
                button.Button.clear_events()

            battle.reset_fighters()
            characters = [luffy, buggy, smoker, arlong]

            for i in characters:
                if i.name == fighters.rcrew_state:
                    fighters.rival_crew.append(i)

        # check opponent screen state
        if fighters.menu_state == 'opponent':
            window.blit(pics.background_opponent, (0, 0))
            button.Button.clear_events()
            if button.luffy_button.draw(window):
                fighters.menu_state = 'prefight'
                fighters.opponent_state = 'Luffy'
                button.Button.clear_events()

            if button.buggy_button.draw(window):
                fighters.menu_state = 'prefight'
                fighters.opponent_state = 'Buggy'
                button.Button.clear_events()

            if button.smoker_button.draw(window):
                fighters.opponent_state = 'Smoker'
                fighters.menu_state = 'prefight'
                button.Button.clear_events()

            if button.arlong_button.draw(window):
                fighters.opponent_state = 'Arlong'
                fighters.menu_state = 'prefight'
                button.Button.clear_events()


            battle.reset_fighters()
            characters = [luffy, buggy, smoker, arlong]

            for i in characters:
                if i.name == fighters.opponent_state:
                    fighters.p2 = i

        if fighters.menu_state == 'squadset':
            fighters.p1 = fighters.crew[0]
            if fighters.boss1 == True:
                fighters.p2 = fighters.boss_crew[0]
            else:
                fighters.p2 = fighters.rival_crew[0]
            fighters.p1.name = fighters.captain_state
            fighters.p2.name = fighters.rival_state
            fighters.menu_state = 'prefight'
            button.Button.clear_events()

        if fighters.menu_state == 'prefight':
            button.Button.clear_events()
            if fighters.boss1 == True:
                window.blit(pics.background_boss, (0, 0))
                moves.display_message('Boss Kaido has appeared!')
                time.sleep(1)
                moves.display_message('Your crew is buzzing for a battle to the death!')
                time.sleep(1)
                button.Button.clear_events()
            else:
                window.blit(pics.background_battle, (0, 0))
                button.Button.clear_events()
            fighters.p1.draw_hp()
            fighters.p2.draw_hp()
            fighters.p1.set_sprite()
            fighters.p2.set_sprite()
            moves.display_message(f'Let the Showdown begin!')
            time.sleep(1.5)

            fighters.menu_state = 'fight'

        if fighters.menu_state == 'fight':
            button.Button.clear_events()
            if fighters.boss1 == True:
                window.blit(pics.background_boss, (0, 0))
            else:
                window.blit(pics.background_battle, (0, 0))
            fighters.p1.draw_hp()
            fighters.p2.draw_hp()
            fighters.p1.set_sprite()
            fighters.p2.set_sprite()

            battle.battle(fighters.p1, fighters.p2)

        if fighters.menu_state == 'switch':
            button.Button.clear_events()
            window.blit(pics.background_switch, (0, 0))
            battle.switch(fighters.crew)

        if fighters.menu_state == 'postfight':
            window.blit(pics.background_end, (0, 0))
            if button.yes_button.draw(window):
                fighters.menu_state = 'mode'
                fighters.fighter_state = ''
                fighters.opponent_state = ''
                fighters.p1.current_hp = fighters.p1.max_hp
                fighters.p2.current_hp = fighters.p2.max_hp

            if button.no_button.draw(window):
                running = False

    pygame.display.update()

pygame.quit()
