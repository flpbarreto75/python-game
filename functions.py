# This is the main functions file
# It will hold the common functions for the game

# Importing the player classes set on the Player.py
from Player import *
from Enemy import *

player = Player()
enemy = Enemy()
# Defining the player name

def player_name(name):
    #print ("Please enter your name :")
    #name = raw_input()
    #print name
    player.name = name


def set_player():

    player.life = 10
    player.special = []
    player.power = 1
    player.level = 1




def set_enemy(name, life, specials, power, level):
    # Defining the player name
    #print ("Please enter your name :")

    #name = input()

    enemy.name = name
    enemy.life = life
    enemy.special = specials
    enemy.power = power
    enemy.level = level




def damage(who, life, damage):

    who.life = life-damage

    print (who.name, " took ", damage, "damage : ", who.life, "remained")
    if who.life == 0:
        print (who.name, "dies")


def life_increase(who, amount):
    who.life = who.life + amount
    print (who.name, "got", amount, "added to life points")
    print ("Life :", who.life)

def special_add(who, special):

    who.special.append(special)

# # Functions calls
# print "######################## "
# print "Player info"
# player_name()
# set_player()
# print "########################"
# print "########################"
# print "Enemy info"
# set_enemy("enem", 10, "none", 3, 1)
# print "########################"
#
# life_increase(player, 6)
#
# damage(player, player.life, enemy.power)
#
# special_add(player, "life")