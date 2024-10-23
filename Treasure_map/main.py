"""This is a game of a treasure hunt."""

# pylint: disable=anomalous-backslash-in-string
print('''
 ____________________________________________________________________
 / \-----     ---------  -----------     -------------- ------    ----/
 \_/__________________________________________________________________/
 |~ ~~ ~~~ ~ ~ ~~~ ~ _____.----------._ ~~~  ~~~~ ~~   ~~  ~~~~~ ~~~~|
 |  _   ~~ ~~ __,---'_       "         `. ~~~ _,--.  ~~~~ __,---.  ~~|
 | | \___ ~~ /      ( )   "          "   `-.,' (') \~~ ~ (  / _\ \~~ |
 |  \    \__/_   __(( _)_      (    "   "     (_\_) \___~ `-.___,'  ~|
 |~~ \     (  )_(__)_|( ))  "   ))          "   |    "  \ ~~ ~~~ _ ~~|
 |  ~ \__ (( _( (  ))  ) _)    ((     \\//    " |   "    \_____,' | ~|
 |~~ ~   \  ( ))(_)(_)_)|  "    ))    //\\ " __,---._  "  "   "  /~~~|
 |    ~~~ |(_ _)| | |   |   "  (   "      ,-'~~~ ~~~ `-.   ___  /~ ~ |
 | ~~     |  |  |   |   _,--- ,--. _  "  (~~  ~~~~  ~~~ ) /___\ \~~ ~|
 |  ~ ~~ /   |      _,----._,'`--'\.`-._  `._~~_~__~_,-'  |H__|  \ ~~|
 |~~    / "     _,-' / `\ ,' / _'  \`.---.._          __        " \~ |
 | ~~~ / /   .-' , / ' _,'_  -  _ '- _`._ `.`-._    _/- `--.   " " \~|
 |  ~ / / _-- `---,~.-' __   --  _,---.  `-._   _,-'- / ` \ \_   " |~|
 | ~ | | -- _    /~/  `-_- _  _,' '  \ \_`-._,-'  / --   \  - \_   / |
 |~~ | \ -      /~~| "     ,-'_ /-  `_ ._`._`-...._____...._,--'  /~~|
 | ~~\  \_ /   /~~/    ___  `---  ---  - - ' ,--.     ___        |~ ~|
 |~   \      ,'~~|  " (o o)   "         " " |~~~ \_,-' ~ `.     ,'~~ |
 | ~~ ~|__,-'~~~~~\    \"/      "  "   "    /~ ~~   O ~ ~~`-.__/~ ~~~|
 |~~~ ~~~  ~~~~~~~~`.______________________/ ~~~    |   ~~~ ~~ ~ ~~~~|
 |____~jrei~__~_______~~_~____~~_____~~___~_~~___~\_|_/ ~_____~___~__|
 / \----- ----- ------------  ------- ----- -------  --------  -------/
 \_/__________________________________________________________________/
''')

print("Welcome to the Treasure Island.\nYour mission is to find the treasure.")

while True:
    try:
        DIRECTION = str(input("Left or right? "))
        # pylint: disable=no-else-break
        if DIRECTION in ("LEFT", "left", "Left"): 
            break
        else:
            print("Fall into a hole.\nGame Over.")
    except ValueError:
        print("Please enter an appropriate value: ")

while True:
    try:
        SWIM_OR_WAIT = str(input("Swim or wait? "))
        # pylint: disable=no-else-break
        if SWIM_OR_WAIT in ("WAIT", "wait", "Wait"):
            break
        else:
            print("Attacked by trout.\nGame Over.")
    except ValueError:
        print("Please specify 'swim' or 'wait': ")

while True:
    try:
        WHICH_DOOR = str(input("Which door? "))
        if WHICH_DOOR == "Yellow":
            print("You Win!")
            break
        if WHICH_DOOR == "Red":
            print("Burned by fire.\nGame Over.")
            break
        if WHICH_DOOR == "Blue":
            print("Eaten by beasts.\nGame Over.")
            break
        if WHICH_DOOR not in ("Yellow", "Red", "Blue"):
            print("Game Over.")
            break
    except ValueError:
        print("Please specify the door you want to open: ")
