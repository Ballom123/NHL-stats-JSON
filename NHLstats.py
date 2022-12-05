import json

class Statsmachine:
    
    def __init__(self):

        self.active = True
        self.read_file()
        self.teams = self.teams_list_startup()
        self.countries = self.nats_list_startup()
        self.mainloop()

    #Asks for filename + loads json.
    def read_file(self):
        #"sample.json" for a sample file of 14 players, "NHL all stats.json" for actual data
        print(f"Open 'sample.json' or 'NHL all stats.json'")
        stats_file = input("tiedosto: ")
        with open(stats_file) as fh:
            data = fh.read()
        self.players = json.loads(data)
        print(f"{len(self.players)} player's stats found.")
    
    #Actual mainloop, asks commands, executes methods accordingly.
    def mainloop(self):
        self.print_commands()
        while self.active:
            command = int(input("Command: "))

            if command == 0:
                self.quit_program()
            if command == 1:
                self.search_player()
            if command == 2:
                self.all_teams()
            if command == 3:
                self.all_nationalities()
            if command == 4:
                self.teams_players()
            if command == 5:
                self.countrys_players()
            if command == 6:
                self.most_points()
            if command == 7:
                self.most_goals()
            if 0>command or command>7:
                print("Error: expected values of 0-7. Enter 0 for help.") 


    #Prints available commands for dataset.
    def print_commands(self):
        
        print("Commands:")
        print("0 Quit")
        print("1 Search for player")
        print("2 List teams")
        print("3 List nationalities")
        print("4 Players from a team")
        print("5 Players from a country")
        print("6 Player w/ most points")
        print("7 Player with most goals")

    #Stops mainloop.
    def quit_program(self):
        
        self.active = False

    #Search for a player by name, print out statline.
    def search_player(self):
        
        player_name = input("Name: ")
        player_name = player_name.title()
        player_profile = next((player for player in self.players if player['name'] == player_name), None)
        print(f"{player_profile['name']}, Team: {player_profile['team']}, G/A = {player_profile['goals']} / {player_profile['assists']}")

    #Finds all teams and list alphabetically on startup.
    def teams_list_startup(self):
        
        return sorted({player['team'] for player in self.players})
    
    #Returns list on call.
    def all_teams(self):
        
        print(self.teams)

    #Same as above but for countries.
    def nats_list_startup(self):
        
        return sorted({player['nationality'] for player in self.players})
    
    #Returns list on call.
    def all_nationalities(self):
        
        print(self.countries)

    #Asks for team and then comprehension for all players in said team, NAMES ONLY.
    def teams_players(self):
        
        team_name = input("Team: ")
        team_players = [player['name'] for player 
                        in self.players 
                        if player['team'] == team_name.upper()]
        for player in team_players:
            print(player)

    def countrys_players(self):
        
        country_name = input("Country: ")
        country_players = [player['name'] for player 
                           in self.players 
                           if player['nationality'] == country_name.upper()]
        for player in country_players:
            print(player)
    
    #Player with most points: sum of goals + assists.
    def most_points(self):
        
        most_points = max(self.players, key=most_points_key)
        print(f"Most points: {most_points['goals']+most_points['assists']} by {most_points['name']}")
    
    #Player with most goals.
    def most_goals(self):
        most_goals = max(self.players, key=most_goals_key)
        print(f"Most goals: {most_goals['goals']} by {most_goals['name']}")

        
def most_points_key(player: dict):
    
    return player['goals']+player['assists']


def most_goals_key(player: dict):
    
    return player['goals']

if __name__ == "__main__":
    Statsmachine()
