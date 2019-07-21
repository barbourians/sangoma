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

JSONFILE = "fpl2019-gw00"


def load_jsonfile():
    filename = "json/"+JSONFILE+".json"
    with open(filename) as json_file:
        data = json.load(json_file)
    return data


def extract_data(dict, element):
    for i in dict[element]:
        print(i)


def main():
    data = load_jsonfile()
    element = "events"
    #element = "game_settings"
    #element = "phases"
    #element = "teams"
    #element = "total_players"
    #element = "elements"
    #element = "element_stats"
    #element = "element_types"
    extract_data(data,element)

if __name__ == "__main__":
    main()