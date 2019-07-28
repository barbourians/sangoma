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


def extract_players(dict, element='elements'):
    f = open(DOKUHOME+'id2.txt','w')
    for i in dict[element]:
        id=str(i['id'])
        first_name=i['first_name'].lower()
        second_name=i['second_name'].lower()
        # Replace non-ascii characters
        full_name = remove_nonascii(second_name+"_"+first_name)
        string=id+":"+full_name
        print(string)
        f.write(string+"\n")
    f.close()

    # Create player txt files
    f = open(DOKUHOME+'player.txt','w')
    for i in dict[element]:
        string=str(i['id'])+":"+i['second_name']+", "+i['first_name']
        f.write(string+"\n")
    f.close()


def main():
    data = load_jsonfile()
    extract_players(data)

if __name__ == "__main__":
    main()
