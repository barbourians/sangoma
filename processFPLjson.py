"""
The FPL json file has the following dictionaries:
    * events: Game week deadline times
    * game_settings: Game settings - eg squad_team_limit / squad_total_spend etc.
    * phases: Game weeks - overall and month breakdown
    * teams: Team names and codes - with strength values
    * total_players: Number of FPL players so far (not a dictionary)
    * elements: Players
    * element_stats : Column stats - eg 'Minutes played':'minutes'
    * element_types : Player positions ~ GKP / DEF / MID / FWD
"""

import json

DOKUHOME="/home/ian/dokuwiki/fpl/"
JSONFILE = "fpl2019-gw00"

MYTEAM = [44,47,68,141,144,151,171,182,183,191,203,212,265,313,405]

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
    filename = "json/"+JSONFILE+".json"
    with open(filename) as json_file:
        data = json.load(json_file)
    return data


def extract_data(dict, element):
    for i in dict[element]:
        print(i)


def remove_nonascii(text):
    text = text.replace(" ","_")
    text = text.replace("'","_")
    text = text.replace("á","a")
    text = text.replace("ä","ae")
    text = text.replace("ã","a")
    text = text.replace("ç","c")
    text = text.replace("é","e")
    text = text.replace("ë","e")
    text = text.replace("í","i")
    text = text.replace("ï","i")
    text = text.replace("ó","o")
    text = text.replace("ö","oe")
    text = text.replace("ø","o")
    text = text.replace("ß","ss")
    text = text.replace("ú","_")
    text = text.replace("ü","ue")
    return text


def get_position(id):
    if id == 1:
        singular_name = "Goalkeeper"
    elif id == 2:
        singular_name = "Defender"
    elif id == 3:
        singular_name = "Midfielder"
    elif id == 4:
        singular_name = "Forward"
    else:
        singular_name = "Unknown"

    return singular_name


def extract_players(dict, element='elements'):
    f = open(DOKUHOME+'id.txt','w')
    for i in dict[element]:
        id=str(i['id'])
        first_name = i['first_name'].lower()
        second_name = i['second_name'].lower()
        # Replace non-ascii characters
        full_name = remove_nonascii(second_name+"_"+first_name)
        string = id+":"+full_name
        # Add element type
        position = get_position(i['element_type'])
        string = string+":"+position
        # Add current cost
        #now_cost = i['now_cost']/10
        #string = string+":"+str(now_cost)
        # Add current team
        team = TEAM[i['team']][1]
        string = string+":"+team
        # Display to screen
        print(string)
        f.write(string+"\n")
    f.close()

    # Create player txt file
    f = open(DOKUHOME+'player.txt','w')
    for i in dict[element]:
        string = str(i['id'])+":"+i['second_name']+", "+i['first_name']
        f.write(string+"\n")
    f.close()


def main():
    data = load_jsonfile()
    extract_players(data)

if __name__ == "__main__":
    main()
