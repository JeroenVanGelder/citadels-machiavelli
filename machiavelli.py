from state_machines.player_turn_device import PlayerTurnDevice
from player.player import Player
import random

character_cards = ['Assassin', 'Thief', 'Magician', 'King', 'Prediker', 'Koopman', 'Bouwmeester', 'Conditaire']

position = 0

players = list()    

player1 = Player('jeroen', position + 1)
position = position + 1
players.append(player1)

player2 = Player('robin', position + 1)
position = position + 1
players.append(player2)

player3 = Player('sander', position + 1)
position = position + 1
players.append(player3)

player4 = Player('martijn', position + 1)
position = position + 1
players.append(player4)

player5 = Player('casper', position + 1)
position = position + 1
players.append(player5)

for player in players:
    print("turn for",player.name)
    rnd = random.randint(0, len(character_cards)-1)
    player.pick_character_card(character_cards[rnd])
    character_cards.pop(rnd)
    print("plays as",player.character)

i = 0
kingPosition = 0
for player in players:
    if player.character is 'King':
        kingPosition = i
    i = i + 1

print("king", kingPosition)

for player in players[kingPosition:len(players)]:
    print(player.name, ', ', player.character)
    
for player in players[0:kingPosition]:
    print(player.name, ', ', player.character)

try: 
    print("First the assassin:", players[players.index('Assassin')].name)
except:
    print("No Assassing")
try:
    print("Then the thief:", players[players.index('Thief')].name)
except:
    print("No Thief")

try:
    print("Then the Magician:", players[players.index('Magician')].name)
except:
    print("No Magician")

try:
    print("Then the King:", players[players.index('King')].name)
except:
    print("No King")

try:
    print("Then the Prediker", players[players.index('Prediker')].name)
except:
    print("No Prediker")

