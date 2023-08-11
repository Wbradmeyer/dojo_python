# Challenge 1
class Player:
    def __init__(self, bio):
        self.name = bio['name']
        self.age = bio['age']
        self.position = bio['position']
        self.team = bio['team']

# Bonus Challenge
    @classmethod
    def get_team(cls, team_list):
        another_team = []
        for player in team_list:
            another_team.append(cls(player))
        return another_team


kevin = {
    "name": "Kevin Durant", 
    "age":34, 
	"position": "small forward", 
	"team": "Brooklyn Nets"
}
jason = {
    "name": "Jason Tatum", 
    "age":24, 
    "position": "small forward", 
    "team": "Boston Celtics"
}
kyrie = {
    "name": "Kyrie Irving", 
    "age":32, "position": "Point Guard", 
    "team": "Brooklyn Nets"
}
    
# Challenge 2
# Create your Player instances here!
player_kevin = Player(kevin)
player_jason = Player(jason)
player_kyrie = Player(kyrie)

# Challenge 3
players = [
    {
    "name": "Kevin Durant", 
	"age":34, 
	"position": "small forward", 
	"team": "Brooklyn Nets"
    },
    {
    "name": "Jason Tatum", 
	"age":24, 
	"position": "small forward", 
	"team": "Boston Celtics"
    },
    {
    "name": "Kyrie Irving", 
	"age":32, "position": "Point Guard", 
	"team": "Brooklyn Nets"
    },
    {
	"name": "Damian Lillard", 
	"age":33, "position": "Point Guard", 
	"team": "Portland Trailblazers"
    },
    {
    "name": "Joel Embiid", 
    "age":32, "position": "Power Foward", 
    "team": "Philidelphia 76ers"
    },
    {
    "name": "", 
    "age":16, 
    "position": "P", 
    "team": "en"
    }
]

new_team = []
for player in players:
    new_team.append(Player(player))

print(new_team)
print(new_team[1].name)
print(new_team[2].age)
print(new_team[0].position)
print(new_team[3].team)

# Bonus call
my_team = Player.get_team(players)
print(my_team[0].name)
