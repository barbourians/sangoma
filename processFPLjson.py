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

DOKUHOME="/home/ian/dokuwiki/fantasy/"
JSONFILE = "fpl2019-gw00"


def load_jsonfile():
    filename = "json/"+JSONFILE+".json"
    with open(filename) as json_file:
        data = json.load(json_file)
    return data


def extract_data(dict, element):
    for i in dict[element]:
        print(i)


def extract_players(dict, element='elements'):
    f = open(DOKUHOME+'id2.txt','w')
    for i in dict[element]:
        #print(i)
        id=str(i['id'])
        second_name=i['second_name'].lower().replace(" ","_")
        first_name=i['first_name'].lower().replace(" ","_")
        full_name=second_name+"_"+first_name
        full_name = full_name.replace("'","_")















        full_name = full_name.replace("á","a")
        full_name = full_name.replace("ä","ae")
        full_name = full_name.replace("ã","a")
        full_name = full_name.replace("ç","c")
        full_name = full_name.replace("é","e")
        full_name = full_name.replace("ë","e")
        full_name = full_name.replace("í","i")
        full_name = full_name.replace("ï","i")
        full_name = full_name.replace("ó","o")
        full_name = full_name.replace("ö","oe")
        full_name = full_name.replace("ø","o")
        full_name = full_name.replace("ß","ss")
        full_name = full_name.replace("ú","_")
        full_name = full_name.replace("ü","ue")
        string=id+":"+full_name
        print(string)
        f.write(string+"\n")
    f.close()

    f = open(DOKUHOME+'player.txt','w')
    for i in dict[element]:
        #print(i)
        string=str(i['id'])+":"+i['second_name']+", "+i['first_name']
        #print(string)
        f.write(string+"\n")
    f.close()


def main():
    data = load_jsonfile()
    extract_players(data)

if __name__ == "__main__":
    main()