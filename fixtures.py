"""
Extract current PL fixtures
"""
import json
import calendar

from datetime import date
from datetime import datetime


GW = "03"

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


def read_game_week_file():
    team = {}
    with open("/home/ian/dokuwiki/fpl/FILES/my-team/gw"+GW+".txt",'r') as fp:
        for line in fp:
            num = line[0:3].strip()
            player = line.strip().split(" ~ ")
            player.append("")  # Make sure each player list has at least 3 items
            team[num] = player

    return team


def process_fixtures(data, team):
    #print("~~NOTOC~~")
    print("======","FPL Game Week",GW,"======")
    header_date = ""

    for event in data:
        game_week = event['event']
        if game_week != int(GW):
            continue
        kickoff_date = event['kickoff_time'][0:10]
        kickoff_time = str(int(event['kickoff_time'][11:13])+1)+event['kickoff_time'][13:16]
        team_h = TEAM[event['team_h']][0]
        team_a = TEAM[event['team_a']][0]
        team_h_difficulty = event['team_h_difficulty']
        team_a_difficulty = event['team_a_difficulty']

        # Date heading
        if header_date != kickoff_date:
            gw_date = datetime.strptime(kickoff_date, '%Y-%m-%d')
            dow = calendar.day_name[gw_date.weekday()]
            month = calendar.month_name[gw_date.month]
            print("=====",dow,gw_date.day,month,gw_date.year,"=====")
            header_date = kickoff_date
        # Display data
        print("===",team_h,"vs",team_a,"@",kickoff_time,"===")

        # See if I have these teams
        home = "[[team:"+TEAM[event['team_h']][1]+"]]"
        for key,value in team.items():
            if home in value:
                print("  *",value[1],"~",value[2], value[3])
        away = "[[team:"+TEAM[event['team_a']][1]+"]]"
        for key,value in team.items():
            if away in value:
                print("  *",value[1],"~",value[2], value[3])


def main():
    team = read_game_week_file()
    data = load_jsonfile()
    process_fixtures(data, team)


if __name__ == "__main__":
    main()
