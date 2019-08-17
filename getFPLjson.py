"""
Original source:
    Vaastav Anand - vaastav
    https://github.com/vaastav/Fantasy-Premier-League/blob/master/getters.py
"""

import requests
import json
import time

BASE_URL = "https://fantasy.premierleague.com/api"

def get_fpl_api_data(element):
    full_url = BASE_URL+"/"+element+"/"
    print(full_url)
    response = requests.get(full_url)
    if response.status_code != 200:
        raise Exception("Response was code " + str(response.status_code))
    responseStr = response.text
    data = json.loads(responseStr)
    return data


def get_fixture_data():
    """ Retrieve the fpl player data from the hard-coded url
    """
    full_url = BASE_URL+"/fixtures"
    print(full_url)
    response = requests.get(full_url)
    if response.status_code != 200:
        raise Exception("Response was code " + str(response.status_code))
    responseStr = response.text

    data = json.loads(responseStr)
    return data


def get_all_player_data():
    """ Retrieve the fpl player data from the hard-coded url
    """
    full_url = BASE_URL+"/bootstrap-static"
    print(full_url)
    response = requests.get(full_url)
    if response.status_code != 200:
        raise Exception("Response was code " + str(response.status_code))
    responseStr = response.text

    data = json.loads(responseStr)
    return data


def get_individual_player_data(player_id):
    """ Retrieve the player-specific detailed data

    Args:
        player_id (int): ID of the player whose data is to be retrieved
    """
    full_url = BASE_URL+"/element-summary/"+str(player_id)
    print(full_url)
    response = ''
    while response == '':
        try:
            response = requests.get(full_url)
        except:
            time.sleep(5)
    if response.status_code != 200:
        raise Exception("Response was code " + str(response.status_code))
    data = json.loads(response.text)
    return data


def get_team_summary_data(entry_id):
    """ Retrieve the summary data for a specific entry/team

    Args:
        entry_id (int) : ID of the team whose data is to be retrieved
    """
    full_url = BASE_URL+"/entry/"+ str(entry_id)+"/history"
    print(full_url)
    response = ''
    while response == '':
        try:
            response = requests.get(full_url)
        except:
            time.sleep(5)
    if response.status_code != 200:
        raise Exception("Response was code " + str(response.status_code))
    data = json.loads(response.text)
    return data


def get_team_goalweek_data(entry_id):
    """ Retrieve the gw-by-gw data for a specific entry/team

    Args:
        entry_id (int) : ID of the team whose data is to be retrieved
    """
    gw_data = []
    for i in range(1, 39):
        full_url = BASE_URL+"/entry/"+str(entry_id)+"/event/"+str(i)
        print(full_url)
        response = ''
        while response == '':
            try:
                response = requests.get(full_url)
            except:
                time.sleep(5)
        if response.status_code != 200:
            raise Exception("Response was code " + str(response.status_code))
        data = json.loads(response.text)
        gw_data += [data]
    return data


def get_team_transfer_data(entry_id):
    """ Retrieve the transfer data for a specific entry/team

    Args:
        entry_id (int) : ID of the team whose data is to be retrieved
    """
    full_url = BASE_URL+"/entry/"+str(entry_id)+"/transfers"
    print(full_url)
    response = ''
    while response == '':
        try:
            response = requests.get(full_url)
        except:
            time.sleep(5)
    if response.status_code != 200:
        raise Exception("Response was code " + str(response.status_code))
    data = json.loads(response.text)
    return data


def main():
    #data = get_all_player_data()
    #data = get_fixture_data()
    element = "fixtures"
    data = get_fpl_api_data(element)
    if len(data) < 100:
        print(element+": No fpl api data found")
    else:
        with open("json/"+element+".json", 'w') as outf:
            json.dump(data, outf)


if __name__ == '__main__':
    main()
