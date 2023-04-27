cricket_dict = {}
num_players = int(input("Enter number of players: "))
for i in range(num_players):
    name = input("Enter player name: ")
    score = int(input("Enter player score: "))
    cricket_dict[name] = score
player_name = input("Enter player name to retrieve score: ")
if player_name in cricket_dict:
    print(player_name + "'s score is", cricket_dict[player_name])
else:
    print("Player not found")
