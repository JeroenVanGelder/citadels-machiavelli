from cards.character_cards import CharacterCards
import random

class CharacterCardController(object):
    def __init__(self):
        self.characterCards = list()
        moordenaar = CharacterCards('moordenaar',1,'kill a guy')
        dief = CharacterCards('dief',2,'Steal stuff')
        magier = CharacterCards('magier',3,'Swap hands')
        koning = CharacterCards('koning',4,'Select First Card')
        prediker = CharacterCards('prediker',5,'Imune to condottiere')
        koopman = CharacterCards('koopman',6,'extra doekoe')
        bouwmeester = CharacterCards('bouwmeester',7,'twee kaarten en drie bouwen')
        condottiere = CharacterCards('condottiere',8,'mol n gebouw')

        self.characterCards.extend([moordenaar, dief, magier, koning, prediker, koopman, bouwmeester, condottiere])

    def getCharacterCard(self, characterCard):
        cardFound = None
        for card in self.characterCards:
            if card.name is characterCard:
                cardFound = card
        return cardFound

    def getAllCharacterCards(self):
        return self.characterCards

    def getAvailableCharacterCards(self):
        availableCards = list()
        for card in self.characterCards:
            if card.available is True:
                availableCards.append(card)
        return availableCards

    def resetCharacterCards(self):
        for card in self.characterCards:
            card.reset()

    def getExposedCharacterCards(self):
        exposedCards = list()
        for characterCard in self.characterCards:
            if characterCard.open is True:
                exposedCards.append(characterCard)
        return exposedCards

    def exposeCharacterCards(self, amountOfPlayers):
        if amountOfPlayers is 4:
            openAmount = 2
        elif amountOfPlayers is 5:
            openAmount = 1
        else:
            openAmount = 0

        for x in range(0,openAmount):
            cardIsOpenable = True
            while cardIsOpenable:
                rnd = random.randint(0, len(self.characterCards)-1)
                if self.characterCards[rnd].name is not "koning":
                    if not self.characterCards[rnd].open:
                        cardIsOpenable = False
            self.characterCards[rnd].openCard()