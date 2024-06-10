"""
this file will have the battle function of the game
"""
import fighters
import moves
import button
import time

temp = ''

def reset():
    fighters.crew = []
    fighters.rival_crew = []
    fighters.squad = False
    fighters.boss1 = False
    fighters.fighter_state = ''
    fighters.opponent_state = ''
    fighters.captain_state = ''
    fighters.crew_state = ''
    fighters.rival_state = ''
    fighters.rcrew_state = ''
    reset_fighters()


def reset_fighters():
    # Reset Luffy
    fighters.luffy1.max_hp = fighters.luffy_reset.max_hp
    fighters.luffy1.current_hp = fighters.luffy_reset.current_hp
    fighters.luffy1.attack = fighters.luffy_reset.attack
    fighters.luffy1.defense = fighters.luffy_reset.defense
    fighters.luffy1.speed = fighters.luffy_reset.speed
    fighters.luffy1.evasive = fighters.luffy_reset.evasive
    fighters.luffy1.hp_x = fighters.luffy_reset.hp_x
    fighters.luffy1.hp_y = fighters.luffy_reset.hp_y

    # Reset Buggy
    fighters.buggy1.max_hp = fighters.buggy_reset.max_hp
    fighters.buggy1.current_hp = fighters.buggy_reset.current_hp
    fighters.buggy1.attack = fighters.buggy_reset.attack
    fighters.buggy1.defense = fighters.buggy_reset.defense
    fighters.buggy1.speed = fighters.buggy_reset.speed
    fighters.buggy1.evasive = fighters.buggy_reset.evasive
    fighters.buggy1.hp_x = fighters.buggy_reset.hp_x
    fighters.buggy1.hp_y = fighters.buggy_reset.hp_y

    # Reset Smoker
    fighters.smoker1.max_hp = fighters.smoker_reset.max_hp
    fighters.smoker1.current_hp = fighters.smoker_reset.current_hp
    fighters.smoker1.attack = fighters.smoker_reset.attack
    fighters.smoker1.defense = fighters.smoker_reset.defense
    fighters.smoker1.speed = fighters.smoker_reset.speed
    fighters.smoker1.evasive = fighters.smoker_reset.evasive
    fighters.smoker1.hp_x = fighters.smoker_reset.hp_x
    fighters.smoker1.hp_y = fighters.smoker_reset.hp_y

    # Reset Arlong
    fighters.arlong1.max_hp = fighters.arlong_reset.max_hp
    fighters.arlong1.current_hp = fighters.arlong_reset.current_hp
    fighters.arlong1.attack = fighters.arlong_reset.attack
    fighters.arlong1.defense = fighters.arlong_reset.defense
    fighters.arlong1.speed = fighters.arlong_reset.speed
    fighters.arlong1.evasive = fighters.arlong_reset.evasive
    fighters.arlong1.hp_x = fighters.arlong_reset.hp_x
    fighters.arlong1.hp_y = fighters.arlong_reset.hp_y

def switch(queue):
    if len(queue) > 1:
        queue[1].switch.rect.topleft = (60, 55)
        if queue[1].switch.draw(fighters.window):

            fighters.temp = queue[0]
            queue[0] = queue[1]
            queue[1] = fighters.temp
            fighters.p1 = queue[0]

            fighters.captain_state = fighters.p1.name
            fighters.menu_state = 'fight'

        if len(queue) > 2:
            queue[2].switch.rect.topleft = (460, 55)
            if queue[2].switch.draw(fighters.window):
                fighters.temp = queue[0]
                queue[0] = queue[2]
                queue[2] = fighters.temp
                fighters.p1 = queue[0]

                fighters.captain_state = fighters.p1.name
                fighters.menu_state = 'fight'

            if len(queue) > 3:
                queue[3].switch.rect.topleft = (60, 224)
                if queue[3].switch.draw(fighters.window):
                    fighters.temp = queue[0]
                    queue[0] = queue[3]
                    queue[3] = fighters.temp
                    fighters.p1 = queue[0]

                    fighters.captain_state = fighters.p1.name
                    fighters.menu_state = 'fight'
    else:
        fighters.menu_state = 'fight'
        moves.display_message(f'{fighters.p1.name} is the last left!')
        time.sleep(.8)


def send_next(queue, p1, p2):
    if len(queue) >= 1:
        fighters.p1 = queue[0]
        fighters.captain_state = fighters.p1.name
        moves.display_message(f'{fighters.p1.name} is out next!')
        time.sleep(1)
    if len(queue) == 0:
        time.sleep(.8)
        moves.display_message(f'{fighters.p2.name} wins!!!')
        fighters.menu_state = 'postfight'
        reset()

def send_next2(queue, p2, p1):
    if len(queue) >= 1:
        fighters.p2 = queue[0]
        fighters.rival_state = fighters.p2.name
        moves.display_message(f'{fighters.p2.name} is out next!')
        time.sleep(1)
    if len(queue) == 0:
        time.sleep(.8)
        moves.display_message(f'{fighters.p1.name} wins!!!')
        fighters.menu_state = 'postfight'
        reset()


def battle(p1, p2):
    button.Button.clear_events()
    if p1.current_hp > 0 and p2.current_hp > 0:
        button.Button.clear_events()
        if fighters.squad == True:
            if button.switch_button.draw(fighters.window):
                fighters.menu_state = 'switch'

        if p1.button1.draw(fighters.window):
            if p1.speed > p2.speed:
                p1.move1.use_move(p1, p2)
                p2.draw_hp()
                if p2.current_hp <= 0:
                    moves.display_message(f'{p2.name} has been defeated!')
                    if fighters.squad and fighters.boss1 == True:
                        fighters.boss_crew.pop(0)
                        send_next2(fighters.boss_crew, p2, p1)
                    elif fighters.squad == True and fighters.boss1 == False:
                        fighters.rival_crew.pop(0)
                        send_next2(fighters.rival_crew, p2, p1)
                    else:
                        time.sleep(.8)
                        moves.display_message(f'{p1.name} wins!!!')
                        fighters.menu_state = 'postfight'
                        reset()
                else:
                    p2.ai(p2, p1)
                    p1.draw_hp()
                    if p1.current_hp <= 0:
                        moves.display_message(f'{p1.name} has been defeated!')
                        if fighters.squad == True:
                            fighters.crew.pop(0)
                            send_next(fighters.crew, p1, p2)
                        else:
                            time.sleep(.8)
                            moves.display_message(f'{p2.name} wins!!!')
                            fighters.menu_state = 'postfight'
                            reset()

            elif p1.speed < p2.speed:
                p2.ai(p2, p1)
                p1.draw_hp()
                if p1.current_hp <= 0:
                    moves.display_message(f'{p1.name} has been defeated!')
                    if fighters.squad == True:
                        fighters.crew.pop(0)
                        send_next(fighters.crew, p1, p2)
                    else:
                        time.sleep(.8)
                        moves.display_message(f'{p2.name} wins!!!')
                        fighters.menu_state = 'postfight'
                        reset()
                else:
                    p1.move1.use_move(p1, p2)
                    p2.draw_hp()
                    if p2.current_hp <= 0:
                        moves.display_message(f'{p2.name} has been defeated!')
                        if fighters.squad and fighters.boss1 == True:
                            fighters.boss_crew.pop(0)
                            send_next2(fighters.boss_crew, p2, p1)
                        elif fighters.squad == True and fighters.boss1 == False:
                            fighters.rival_crew.pop(0)
                            send_next2(fighters.rival_crew, p2, p1)
                        else:
                            time.sleep(.8)
                            moves.display_message(f'{p1.name} wins!!!')
                            fighters.menu_state = 'postfight'
                            reset()

        if p1.button2.draw(fighters.window):
            if p1.speed > p2.speed:
                p1.move2.use_move(p1, p2)
                p2.draw_hp()
                if p2.current_hp <= 0:
                    moves.display_message(f'{p2.name} has been defeated!')
                    if fighters.squad and fighters.boss1 == True:
                        fighters.boss_crew.pop(0)
                        send_next2(fighters.boss_crew, p2, p1)
                    elif fighters.squad == True and fighters.boss1 == False:
                        fighters.rival_crew.pop(0)
                        send_next2(fighters.rival_crew, p2, p1)
                    else:
                        time.sleep(.8)
                        moves.display_message(f'{p1.name} wins!!!')
                        fighters.menu_state = 'postfight'
                        reset()

                else:
                    p2.ai(p2, p1)
                    p1.draw_hp()
                    if p1.current_hp <= 0:
                        moves.display_message(f'{p1.name} has been defeated!')
                        if fighters.squad == True:
                            fighters.crew.pop(0)
                            send_next(fighters.crew, p1, p2)
                        else:
                            time.sleep(.8)
                            moves.display_message(f'{p2.name} wins!!!')
                            fighters.menu_state = 'postfight'
                            reset()

            elif p1.speed < p2.speed:
                p2.ai(p2, p1)
                p1.draw_hp()
                if p1.current_hp <= 0:
                    moves.display_message(f'{p1.name} has been defeated!')
                    if fighters.squad == True:
                        fighters.crew.pop(0)
                        send_next(fighters.crew, p1, p2)
                    else:
                        time.sleep(.8)
                        moves.display_message(f'{p2.name} wins!!!')
                        fighters.menu_state = 'postfight'
                        reset()

                else:
                    p1.move2.use_move(p1, p2)
                    p2.draw_hp()
                    if p2.current_hp <= 0:
                        moves.display_message(f'{p2.name} has been defeated!')
                        if fighters.squad and fighters.boss1 == True:
                            fighters.boss_crew.pop(0)
                            send_next2(fighters.boss_crew, p2, p1)
                        elif fighters.squad == True and fighters.boss1 == False:
                            fighters.rival_crew.pop(0)
                            send_next2(fighters.rival_crew, p2, p1)
                        else:
                            time.sleep(.8)
                            moves.display_message(f'{p1.name} wins!!!')
                            fighters.menu_state = 'postfight'
                            reset()

        if p1.button3.draw(fighters.window):
            if p1.speed > p2.speed:
                p1.move3.use_move(p1, p2)
                p2.draw_hp()
                if p2.current_hp <= 0:
                    moves.display_message(f'{p2.name} has been defeated!')
                    if fighters.squad and fighters.boss1 == True:
                        fighters.boss_crew.pop(0)
                        send_next2(fighters.boss_crew, p2, p1)
                    elif fighters.squad == True and fighters.boss1 == False:
                        fighters.rival_crew.pop(0)
                        send_next2(fighters.rival_crew, p2, p1)
                    else:
                        time.sleep(.8)
                        moves.display_message(f'{p1.name} wins!!!')
                        fighters.menu_state = 'postfight'
                        reset()

                else:
                    p2.ai(p2, p1)
                    p1.draw_hp()
                    if p1.current_hp <= 0:
                        moves.display_message(f'{p1.name} has been defeated!')
                        if fighters.squad == True:
                            fighters.crew.pop(0)
                            send_next(fighters.crew, p1, p2)
                        else:
                            time.sleep(.8)
                            moves.display_message(f'{p2.name} wins!!!')
                            fighters.menu_state = 'postfight'
                            reset()

            elif p1.speed < p2.speed:
                p2.ai(p2, p1)
                p1.draw_hp()
                if p1.current_hp <= 0:
                    moves.display_message(f'{p1.name} has been defeated!')
                    if fighters.squad == True:
                        fighters.crew.pop(0)
                        send_next(fighters.crew, p1, p2)
                    else:
                        time.sleep(.8)
                        moves.display_message(f'{p2.name} wins!!!')
                        fighters.menu_state = 'postfight'
                        reset()

                else:
                    p1.move3.use_move(p1, p2)
                    p2.draw_hp()
                    if p2.current_hp <= 0:
                        moves.display_message(f'{p2.name} has been defeated!')
                        if fighters.squad and fighters.boss1 == True:
                            fighters.boss_crew.pop(0)
                            send_next2(fighters.boss_crew, p2, p1)
                        elif fighters.squad == True and fighters.boss1 == False:
                            fighters.rival_crew.pop(0)
                            send_next2(fighters.rival_crew, p2, p1)
                        else:
                            time.sleep(.8)
                            moves.display_message(f'{p1.name} wins!!!')
                            fighters.menu_state = 'postfight'
                            reset()

        if p1.button4.draw(fighters.window):
            if p1.speed > p2.speed:
                p1.move4.use_move(p1, p2)
                p2.draw_hp()
                if p2.current_hp <= 0:
                    moves.display_message(f'{p2.name} has been defeated!')
                    if fighters.squad and fighters.boss1 == True:
                        fighters.boss_crew.pop(0)
                        send_next2(fighters.boss_crew, p2, p1)
                    elif fighters.squad == True and fighters.boss1 == False:
                        fighters.rival_crew.pop(0)
                        send_next2(fighters.rival_crew, p2, p1)
                    else:
                        time.sleep(.8)
                        moves.display_message(f'{p1.name} wins!!!')
                        fighters.menu_state = 'postfight'
                        reset()

                else:
                    p2.ai(p2, p1)
                    p1.draw_hp()
                    if p1.current_hp <= 0:
                        moves.display_message(f'{p1.name} has been defeated!')
                        if fighters.squad == True:
                            fighters.crew.pop(0)
                            send_next(fighters.crew, p1, p2)
                        else:
                            time.sleep(.8)
                            moves.display_message(f'{p2.name} wins!!!')
                            fighters.menu_state = 'postfight'
                            reset()

            elif p1.speed < p2.speed:
                p2.ai(p2, p1)
                p1.draw_hp()
                if p1.current_hp <= 0:
                    moves.display_message(f'{p1.name} has been defeated!')
                    if fighters.squad == True:
                        fighters.crew.pop(0)
                        send_next(fighters.crew, p1, p2)
                    else:
                        time.sleep(.8)
                        moves.display_message(f'{p2.name} wins!!!')
                        fighters.menu_state = 'postfight'
                        reset()

                else:
                    p1.move4.use_move(p1, p2)
                    p2.draw_hp()
                    if p2.current_hp <= 0:
                        moves.display_message(f'{p2.name} has been defeated!')
                        if fighters.squad and fighters.boss1 == True:
                            fighters.boss_crew.pop(0)
                            send_next2(fighters.boss_crew, p2, p1)
                        elif fighters.squad == True and fighters.boss1 == False:
                            fighters.rival_crew.pop(0)
                            send_next2(fighters.rival_crew, p2, p1)
                        else:
                            time.sleep(.8)
                            moves.display_message(f'{p1.name} wins!!!')
                            fighters.menu_state = 'postfight'
                            reset()

