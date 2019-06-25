# Player object definition

class Player:
    def __int__(self, name, level, power, special, life):
        self.name = name
        self.life = life
        self.level = level
        self.power = power
        self.special




def set_player (level):

    # Defining the player name
    player = Player()
    print ("Please enter your name :")

    name = raw_input()
    player.name = name

    # Defining the player level
    player.level = level

    # Defining the player power level
    player.power = level

    # defining any player special
    player.special = []


    # Display the player info
    print player.name
    print player.level
    print player.power
    print len(player.special)
