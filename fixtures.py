"""
Extract current PL fixtures
"""

import json

GW = 2

TEAM = {1:["Arsenal", "ARS"],
        2:["Aston Villa", "AVL"],
        3:["Bournemouth", "BOU"],
        4:["Brighton", "BHA"],
        5:["Burnley", "BUR"],
        6:["Chelsea", "CHE"],
        7:["Crystal Palace", "CRY"],
        8:["Everton", "EVE"],
        9:["Leicester", "LEI"],
        10:["Liverpool", "LIV"],
        11:["Man City", "MCI"],
        12:["Man Utd", "MUN"],
        13:["Newcastle", "NEW"],
        14:["Norwich", "NOR"],
        15:["Sheffield Utd", "SHU"],
        16:["Southampton", "SOU"],
        17:["Spurs", "TOT"],
        18:["Watford", "WAT"],
        19:["West Ham", "WHU"],
        20:["Wolves", "WOL"]}


def load_jsonfile():
    filename = "json/fixtures.json"
    with open(filename) as json_file:
        data = json.load(json_file)
    return data


def process_fixtures(data):
    print("game_week", end=",")
    print("kickoff_date", end=",")
    print("kickoff_time", end=",")
    print("team_h", end=",")
    print("team_a", end=",")
    #print("team_h_difficulty", end=",")
    #print("team_a_difficulty", end=",")
    print()
    for event in data:
        game_week = event['event']
        if game_week != GW:
            continue
        kickoff_date = event['kickoff_time'][0:10]
        kickoff_time = str(int(event['kickoff_time'][11:13])+1)+event['kickoff_time'][13:16]
        team_h = TEAM[event['team_h']][1]
        team_a = TEAM[event['team_a']][1]
        team_h_difficulty = event['team_h_difficulty']
        team_a_difficulty = event['team_a_difficulty']

        # Display to the screen
        print(game_week, end=",")
        print(kickoff_date, end=",")
        print(kickoff_time, end=",")
        print(team_h, end=",")
        print(team_a, end=",")
        #print(team_h_difficulty, end=",")
        #print(team_a_difficulty, end=",")
        print()


def main():
    data = load_jsonfile()
    process_fixtures(data)


if __name__ == "__main__":
    main()
