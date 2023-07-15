class Player:
    def __init__(self, name, age, position, team):
        self.name = name
        self.age = age
        self.position = position
        self.team = team

    @classmethod
    def get_team(cls, team_list):
        players = []
        for player_dict in team_list:
            player = cls(**player_dict)
            players.append(player)
        return players


players = [
    {
        "name": "Kevin Durant",
        "age": 34,
        "position": "small forward",
        "team": "Brooklyn Nets",
    },
    {
        "name": "Jason Tatum",
        "age": 24,
        "position": "small forward",
        "team": "Boston Celtics",
    },
    {
        "name": "Kyrie Irving",
        "age": 32,
        "position": "Point Guard",
        "team": "Brooklyn Nets",
    },
    {
        "name": "Damian Lillard",
        "age": 33,
        "position": "Point Guard",
        "team": "Portland Trailblazers",
    },
    {
        "name": "Joel Embiid",
        "age": 32,
        "position": "Power Forward",
        "team": "Philadelphia 76ers",
    },
    {
        "name": "DeMar DeRozan",
        "age": 32,
        "position": "Shooting Guard",
        "team": "Chicago Bulls",
    },
]

# Challenge 1: Create Player instances using dictionaries
player1 = Player(**players[0])
player2 = Player(**players[1])
player3 = Player(**players[2])

# Challenge 2: Create Player instances from the list of dictionaries
player_list = []
for player_dict in players:
    player = Player(**player_dict)
    player_list.append(player)

# Challenge 3: Use the @classmethod to create Player instances from the list of dictionaries
player_list = Player.get_team(players)

# Ninja Bonus: Use the @classmethod to create Player instances from the list of dictionaries
player_list = Player.get_team(players)

# Print the player names
for player in player_list:
    print(player.name)
