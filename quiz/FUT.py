PLAYERS = {
    'Karim Benzema': 93,  # player's name: his rating
    'Robert Lewandowski': 94,
    'Kylian Mbappe': 97,
    'Luka Modric': 90,
    'Pedri': 93,
    'Frenkie de Jong': 88,
}

LEGENDARIES = {
    'Lionel Messi': (
        98,
        1.05,
    ),  # legendary player's name: (his rating, his chemistry booster value)
    'Cristiano Ronaldo': (97, 0.98),
}


class Team:
    """FIFA Ultimate Team"""

    def __init__(self, name, initial_players=None):
        """Initialize team and update squad and information if initial_players is provided

        name: string
        initial_players: a list of strings representing initial players in this team.

        """
        self.name = name
        if initial_players == None:
            self.squad = []
        else:
            self.squad = initial_players
        self.rating = 0
        

    def __str__(self):
        """Return a string representation of this team, including team name and squad."""
        return self.name + ' has ' + str(self.squad)
    
    def draft(self, player):
        """choose one player from PLAYERS and update team's rating which is the average rating of entire current squad.

        player: string
        """
        self.squad.append(player)
        sum = 0.0
        for x in self.squad:
            sum = sum + PLAYERS[x]
        self.rating = sum / len(self.squad)
        return self.__str__()

    def draft_legendary(self, player):
        """choose one player from LEGENDARIES and update team's rating which is the average rating of entire current squad multiplied by legendary's booster value.

        player: string
        """
        sum = 0.0
        for x in self.squad:
            sum = sum + LEGENDARIES[x]
        self.squad.append(player)
        sum = sum + LEGENDARIES[player][1]
        self.rating = sum / len(self.squad) * LEGENDARIES[player][2]
        return self.__str__()
    
    def matchs(self,other):
        return self.rating

#############################################
# Please DO NOT change code in main function!
#############################################
def main():
    real_madrid = Team('Real Madrid', initial_players=['Karim Benzema'])
    barcelona = Team('Barcelona')
    print('Before drafting squad:')
    print(real_madrid)
    print(barcelona)
    print()
    print('After drafting squad:')
    barcelona.draft('Robert Lewandowski')
    real_madrid.draft('Kylian Mbappe')
    barcelona.draft('Pedri')
    real_madrid.draft('Luka Modric')
    barcelona.draft('Frenkie de Jong')
    print(real_madrid)
    print(barcelona)
    print()
    print('Will Real Madrid win against Barcelona?')
    print(real_madrid > barcelona)
    print()
    print('After drafting legendary:')
    real_madrid.draft_legendary('Cristiano Ronaldo')
    barcelona.draft_legendary('Lionel Messi')
    print(real_madrid)
    print(barcelona)
    print()
    print('Will Real Madrid win against Barcelona?')
    print(real_madrid > barcelona)


if __name__ == '__main__':
    main()