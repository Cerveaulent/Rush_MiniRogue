import sys
import curses
from room import Room as Room
from room import Treasure as Treasure
from room import Arrivee as Arrivee
from monster import MonsterTypeA as MonsterA
from player import Player as Player
from random import randint

def display_chr(win, h, w, i, j, c, color):
    win.addstr(int(height // 2 + i - h // 2), int(width // 2 + j - w // 2), c, curses.color_pair(color))

def monster(pos, x, y, player, pos_ac):
    if pos == pos_ac and x == player.x and y == player.y :
        return True
    for m in range(len(monsters)):
        if monsters[m] and pos == monsters[m].room and x == monsters[m].pos_x and y == monsters[m].pos_y :
            return True
    return False

def treasure(pos, x, y):
    for t in range(len(treasures)):
        if treasures[t] and pos == treasures[t].room and x == treasures[t].pos_x and y == treasures[t].pos_y :
            return True
    return False

def end(pos, player):
    if finish[0].pos_x and pos == finish[0].room and player.x == finish[0].pos_x and player.y == finish[0].pos_y and escape :
        return True
    return False

def affiche_salle(win, player):
    horiz  = chr(int('2550',16))
    verti  = chr(int('2551',16))
    coinHG = chr(int('2554',16))
    coinHD = chr(int('2557',16))
    coinBG = chr(int('255A',16))
    coinBD = chr(int('255D',16))
    coinX  = chr(int('256C',16))
    heros  = chr(int('263B',16))
    coeur = chr(int('2665',16))
    coeurb = chr(int('2661', 16))
    cle = chr(int('2A22',16))
    end = chr(int('2A53', 16))
    mons = chr(int('F12', 16))
    floor = chr(int('22C6', 16))
    h = salle[pos]['size'].height
    w = salle[pos]['size'].width
    for m in range(len(monsters)):
        if monsters[m] and pos == monsters[m].room and not monsters[m].pos_x :
            a = randint(1, w - 2)
            b = randint(1, h - 2)
            while monster(pos, a, b, player, pos) or treasure(pos, a, b) :
                a = randint(1, w - 2)
                b = randint(1, h - 2)
            monsters[m] = MonsterA(a, b, pos)
    for t in range(len(treasures)):
        if treasures[t] and pos == treasures[t].room and not treasures[t].pos_x :
            a = randint(1, w - 2)
            b = randint(1, h - 2)
            while monster(pos, a, b, player, pos) or treasure(pos, a, b) :
                a = randint(1, w - 2)
                b = randint(1, h - 2)
            treasures[t] = Treasure(a, b, pos, treasures[t].symbol)
    if pos == finish[0].room and not finish[0].pos_x :
        a = randint(1, w - 2)
        b = randint(1, h - 2)
        while monster(pos, a, b, player, pos) or treasure(pos, a, b) :
            a = randint(1, w - 2)
            b = randint(1, h - 2)
        finish[0] = Arrivee(pos, a, b)
    i = 0
    while i < h :
        j = 0
        while j < w :
            if not i :
                if j == salle[pos]['place']['n'] :
                    display_chr(win,  h, w, i, j, coinX, 1)
                elif not j :
                    display_chr(win,  h, w, i, j, coinHG, 1)
                elif j + 1 == w :
                    display_chr(win,  h, w, i, j, coinHD, 1)
                else :
                    display_chr(win,  h, w, i, j, horiz, 1)
            elif i + 1 == h :
                if j == salle[pos]['place']['s'] :
                    display_chr(win,  h, w, i, j, coinX, 1)
                elif not j :
                    display_chr(win,  h, w, i, j, coinBG, 1)
                elif j + 1 == w :
                    display_chr(win,  h, w, i, j, coinBD, 1)
                else :
                    display_chr(win,  h, w, i, j, horiz, 1)
            elif not j or j + 1 == w :
                if (not j and i == salle[pos]['place']['w']) or (j + 1 == w and i == salle[pos]['place']['e']) :
                    display_chr(win,  h, w, i, j, coinX, 1)
                else :
                    display_chr(win,  h, w, i, j, verti, 1)
            else :
                display_chr(win,  h, w, i, j, floor, 2)
            for m in range(len(monsters)):
                if monsters[m] and pos == monsters[m].room and j == monsters[m].pos_x and i == monsters[m].pos_y :
                    display_chr(win, h, w, i, j, mons, 4)
            for t in range(len(treasures)):
                if treasures[t] and pos == treasures[t].room and j == treasures[t].pos_x and i == treasures[t].pos_y :
                    if not treasures[t].symbol :
                        display_chr(win, h, w, i, j, coeur, 3)
                    elif treasures[t].symbol == 1 :
                        display_chr(win, h, w, i, j, coeurb, 3)
                    else :
                        display_chr(win, h, w, i, j, cle, 7)
            if pos == finish[0].room and j == finish[0].pos_x and i == finish[0].pos_y :
                display_chr(win, h, w, i, j, end, 6)
            if player.x == j and player.y == i :
                display_chr(win, h, w, i, j, heros, 5)
            j += 1
        win.addstr(int(height // 2 + i - h // 2), int(width // 2 + j - w // 2), '\n')
        i += 1
    win.addstr(height - 1, width - 1, '')

def door(win, player):
    if (player.x == 0 and player.y == salle[pos]['place']['w']) or (player.x == salle[pos]['place']['s'] and player.y == salle[pos]['size'].height - 1) or (player.x == salle[pos]['place']['n'] and player.y == 0)    \
        or (player.x == salle[pos]['size'].width - 1 and player.y == salle[pos]['place']['e']) :
        return True
    return False

def fight(player, pos, m):
    if monsters[m] :
        dx = player.x - monsters[m].pos_x
        dy = player.y - monsters[m].pos_y
        if pos == monsters[m].room and -1 <= dx <= 1 and -1 <= dy <= 1 :
            return True
    return False

def main(win):
    global salle, height, width, pos, monsters, treasures, finish, escape

    win.nodelay(True)
    while True :
        height, width = win.getmaxyx()
        finish = ['']
        finish[0] = Arrivee(randint(0, 4), 0, 0)
        treasures = [''] * 9
        treasures[0] = Treasure(0, 0, randint(0, 4), 0)
        treasures[1] = Treasure(0, 0, randint(0, 4), 0)
        treasures[2] = Treasure(0, 0, randint(0, 4), 0)
        treasures[3] = Treasure(0, 0, randint(0, 4), 0)
        treasures[4] = Treasure(0, 0, randint(0, 4), 0)
        treasures[5] = Treasure(0, 0, randint(0, 4), 0)
        treasures[6] = Treasure(0, 0, randint(0, 4), 0)
        treasures[7] = Treasure(0, 0, randint(0, 4), 2)
        treasures[8] = Treasure(0, 0, randint(0, 4), 1)
        monsters = [''] * 13
        monsters[0] = MonsterA(0, 0, randint(0, 4))
        monsters[1] = MonsterA(0, 0, randint(0, 4))
        monsters[2] = MonsterA(0, 0, randint(0, 4))
        monsters[3] = MonsterA(0, 0, randint(0, 4))
        monsters[4] = MonsterA(0, 0, randint(0, 4))
        monsters[5] = MonsterA(0, 0, randint(0, 4))
        monsters[6] = MonsterA(0, 0, randint(0, 4))
        monsters[7] = MonsterA(0, 0, randint(0, 4))
        monsters[8] = MonsterA(0, 0, randint(0, 4))
        monsters[9] = MonsterA(0, 0, randint(0, 4))
        monsters[10] = MonsterA(0, 0, randint(0, 4))
        monsters[11] = MonsterA(0, 0, randint(0, 4))
        monsters[12] = MonsterA(0, 0, randint(0, 4))
        salle = [''] * 5
        h = randint(7, 15)
        w = randint(7, 15)
        salle[0] = {'size' : Room(h, w), 'card' : {'s' : 3, 'n' : -1, 'w' : 2, 'e' : 1}, 'place' : {'s' : randint(1, w - 2), 'n' : -1, 'w' : randint(1, h - 2), 'e' : randint(1, h - 2)}}
        h = randint(7, 15)
        w = randint(7, 15)
        salle[1] = {'size' : Room(h, w), 'card' : {'s' : 4, 'n' : -1, 'w' : 0, 'e' : -1}, 'place' : {'s' : randint(1, w - 2), 'n' : -1, 'w' : randint(1, h - 2), 'e' : -1}}
        h = randint(7, 15)
        w = randint(7, 15)
        salle[2] = {'size' : Room(h, w), 'card' : {'s' : -1, 'n' : -1, 'w' : -1, 'e' : 0}, 'place' : {'s' : -1, 'n' : -1, 'w' : -1, 'e' : randint(1, h - 2)}}
        h = randint(7, 15)
        w = randint(7, 15)
        salle[3] = {'size' : Room(h, w), 'card' : {'s' : -1, 'n' : 0, 'w' : -1, 'e' : 4}, 'place' : {'s' : -1, 'n' : randint(1, w - 2), 'w' : -1, 'e' : randint(1, h - 2)}}
        h = randint(7, 15)
        w = randint(7, 15)
        salle[4] = {'size' : Room(h, w), 'card' : {'s' : -1, 'n' : 1, 'w' : 3, 'e' : -1}, 'place' : {'s' : -1, 'n' : randint(1, w - 2), 'w' : randint(1, h - 2), 'e' : -1}}
        player = Player()
        pos = 0
        time = 0
        fin = False
        fin2 = False
        level = 1
        stop = False
        game_over = False
        game_over_end = False
        game_over_end2 = False
        escape = False
        curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
        curses.init_pair(2, curses.COLOR_BLUE, curses.COLOR_BLACK)
        curses.init_pair(3, curses.COLOR_MAGENTA, curses.COLOR_BLACK)
        curses.init_pair(4, curses.COLOR_WHITE, curses.COLOR_BLACK)
        curses.init_pair(5, curses.COLOR_YELLOW, curses.COLOR_BLACK)
        curses.init_pair(6, curses.COLOR_BLACK, curses.COLOR_WHITE)
        curses.init_pair(7, curses.COLOR_CYAN, curses.COLOR_BLACK)
        win.addstr("Time : {}".format(time))
        win.addstr(0, width - 9, "Level : {}".format(level))
        win.addstr(0, width // 2 - 5, "Lives : {}".format(player.health))
        win.addstr(2, width - 18, "Monsters left : 13")
        nb = 13
        affiche_salle(win, player)
        while not game_over_end2 :
            try :
                key = win.getkey()
                win.clear()
                win.addstr(0, 0, "Time : {}".format(time))
                time += 1
                win.addstr(0, width - 9, "Level : {}".format(level))
                if escape :
                    win.addstr(2, 0, "Cle trouvee")
                win.addstr(2, width - 18, "Monsters left : {}".format(nb))
                height, width = win.getmaxyx()
                if key == 'KEY_LEFT' and (player.x > 1 or player.y == salle[pos]['place']['w']) and not monster(pos, player.x - 1, player.y, player, pos) :
                    player.x -= 1
                elif key == 'KEY_DOWN' and (player.y < salle[pos]['size'].height - 2 or player.x == salle[pos]['place']['s']) and not monster(pos, player.x, player.y + 1, player, pos) :
                    player.y += 1
                elif key == 'KEY_UP' and (player.y > 1 or player.x == salle[pos]['place']['n']) and not monster(pos, player.x, player.y - 1, player, pos) :
                    player.y -= 1
                elif key == 'KEY_RIGHT' and (player.x < salle[pos]['size'].width - 2 or player.y == salle[pos]['place']['e']) and not monster(pos, player.x + 1, player.y, player, pos) :
                    player.x += 1
                if key == 'q' :
                    win.addstr(height - 1, 0, "You really want to leave the game ? [Y/n]")
                    stop = True
                elif stop and key != 'n' :
                    exit()
                elif stop :
                    stop = False
                if door(win, player) :
                    if key == 'KEY_RIGHT' :
                        if monster(salle[pos]['card']['e'], 1, salle[salle[pos]['card']['e']]['place']['w'], player, pos) :
                            player.x -= 1
                        else :
                            pos = salle[pos]['card']['e']
                            player.x = 1
                            player.y = salle[pos]['place']['w']
                    elif key == 'KEY_LEFT' :
                        if monster(salle[pos]['card']['w'], salle[salle[pos]['card']['w']]['size'].width - 2, salle[salle[pos]['card']['w']]['place']['e'], player, pos) :
                            player.x += 1
                        else :
                            pos = salle[pos]['card']['w']
                            player.x = salle[pos]['size'].width - 2
                            player.y = salle[pos]['place']['e']
                    elif key == 'KEY_UP' :
                        if monster(salle[pos]['card']['n'], salle[salle[pos]['card']['n']]['place']['s'], salle[salle[pos]['card']['n']]['size'].height - 2, player, pos) :
                            player.y += 1
                        else :
                            pos = salle[pos]['card']['n']
                            player.x = salle[pos]['place']['s']
                            player.y = salle[pos]['size'].height - 2
                    elif key == 'KEY_DOWN' :
                        if monster(salle[pos]['card']['s'], salle[salle[pos]['card']['s']]['place']['n'], 1, player, pos) :
                            player.y -= 1
                        else :
                            pos = salle[pos]['card']['s']
                            player.x = salle[pos]['place']['n']
                            player.y = 1
                if treasure(pos, player.x, player.y) :
                    for t in range(len(treasures)):
                        if treasures[t] and pos == treasures[t].room and player.x == treasures[t].pos_x and player.y == treasures[t].pos_y :
                            if not treasures[t].symbol :
                                player.health += 1
                                win.addstr(1, 0, "Tresor recupere : Vie bonus")
                            elif treasures[t].symbol == 1 :
                                player.health += 3
                                win.addstr(1, 0, "Tresor recupere : Super Vie")
                            else :
                                escape = True
                                win.addstr(1, 0, "Tresor recupere : Cle de fin de niveau")
                            treasures[t] = ''
                for m in range(len(monsters)):
                    if fight(player, pos, m) :
                        if key == ' ' :
                            player.attack(monsters[m], win, height, width)
                            if monsters[m].health <= 0 :
                                monsters[m] = ''
                                nb -= 1
                        if monsters[m] :
                            monsters[m].attack(player, win, height, width)
                        if player.health <= 0 :
                            game_over = True
                win.addstr(0, width // 2 - 5, "Lives : {}".format(player.health))
                affiche_salle(win, player)
                if game_over_end and key != 'n' :
                    win.clear()
                    game_over_end2 = True
                elif game_over_end :
                    exit()
                elif game_over :
                    win.clear()
                    win.addstr(height // 2, width // 2 - 5, "GAME OVER !")
                    win.addstr(height // 2 + 1, width // 2 - 7, "Retry ? [Y/n]")
                    game_over_end = True
                elif fin2 and key != 'n' :
                    win.clear()
                    game_over_end2 = True
                elif fin2 :
                    fin = False
                    fin2 = False
                elif not fin and end(pos, player):
                    win.clear()
                    fin = True
                    win.addstr(height // 2, width // 2 - 9, "NIVEAU {} TERMINE !".format(level))
                    win.addstr(height // 2 + 1, width // 2 - 9, "Next level ? [Y/n]")
                elif fin and key != 'n' :
                    exit()
                elif fin :
                    win.clear()
                    win.addstr(height // 2, width // 2 - 7, "Retry ? [Y/n]")
                    fin2 = True
                    fin = False
            except Exception :
                pass

curses.wrapper(main)