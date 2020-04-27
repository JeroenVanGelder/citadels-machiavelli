from game import MachiavelliGame
from player.playerDescriptions import PlayerDescription

newGame = MachiavelliGame()

players = list()    

player1 = PlayerDescription('jeroen')
player2 = PlayerDescription('robin')
player3 = PlayerDescription('sander')
player4 = PlayerDescription('martijn')
player5 = PlayerDescription('casper')


newGame.registerPlayers(player1,player2,player3,player4,player5)
newGame.startGame()