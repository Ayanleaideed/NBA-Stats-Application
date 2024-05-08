import requests

# Define the API key and the base URL
api_key = 'a16ac370-e80f-4615-a9c6-36346f9cb961'
base_url = 'https://api.balldontlie.io/v1'

# Set up headers with your API key
headers = {
    'Authorization': api_key
}

# Function to search for players by name with multiple attempts
def get_player_by_name_variants(first_name):
    name_variants = [
        f'{first_name}',            # "LeBron"
        f'{first_name.lower()}',
        f'{first_name.upper()}',
        f'{first_name.capitalize()}'

    ]
    for name in name_variants:
        params = {'search': name}
        response = requests.get(f'{base_url}/players', headers=headers, params=params)
        if response.status_code == 200:
            data = response.json()
            if data['data']:
                return data['data']  # Return the first player that matches the name
    return None


import json
from django.shortcuts import render
from nba_api.stats.static import players
from django.http import HttpResponse



file_path = 'stats\data.json'
file_path = 'stats/data.json'

num_sorts_by_position = 2
data = None

def load_data():
    global data
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        print("The file was not found:", file_path)
    except json.JSONDecodeError:
        print("Failed to decode JSON from the file:", file_path)

def get_players_by_position():
    """Retrieve the position of players."""
    global num_sorts_by_position
    sorted_players = []
    if num_sorts_by_position % 3 == 0:
        for value in data['data']:
            if value['player']['position'] == 'C':
                sorted_players.append(value)
    elif num_sorts_by_position % 3 == 1:
        for value in data['data']:
            if value['player']['position'] == 'F':
                sorted_players.append(value)
    else:
        print
        for value in data['data']:
            if value['player']['position'] == 'G':
                sorted_players.append(value)
    num_sorts_by_position += 1
    return sorted_players

def get_players(sort_option):
    """Get active NBA players."""
    player_data = []
    load_data()

    if sort_option == 1:
        player_data = get_players_by_position()
    elif sort_option == 2:
        player_data = sorted(data['data'], key=lambda x: x['pts'], reverse=True)
    elif sort_option == 3:
        player_data = sorted(data['data'], key=lambda x: x['reb'], reverse=True)

    # Eliminate duplicates using a set for unique keys
    seen = set()
    unique_players = []
    for player in player_data:
        # Define a tuple of properties that makes each record unique
        identifier = (player['player']['first_name'] + ' ' + player['player']['last_name'], player['player']['position'])
        if identifier not in seen:
            seen.add(identifier)
            unique_players.append(player)

    # Iterate over each active player
    result_data = []
    for index, player in enumerate(unique_players, start=1):
        player_stats = {
            'full_name': player['player']['first_name'] + ' ' + player['player']['last_name'],
            'position': player['player']['position'],
            'pts': player['pts'],
            'reb': player['reb'],
            'turnover': player['turnover'],
            'rank': index
        }
        result_data.append(player_stats)

    return result_data



import requests
from datetime import datetime, timedelta

def fetch_games_upcoming(days_ahead=7):
    api_key = 'a16ac370-e80f-4615-a9c6-36346f9cb961'
    base_url = 'https://api.balldontlie.io/v1/games'
    headers = {'Authorization': api_key}
    start_date = datetime.now().date()
    end_date = start_date + timedelta(days=days_ahead)

    start_date_str = start_date.strftime('%Y-%m-%d')
    end_date_str = end_date.strftime('%Y-%m-%d')

    params = {
        'start_date': start_date_str,
        'end_date': end_date_str
    }

    try:
        response = requests.get(base_url, headers=headers, params=params)
        response.raise_for_status()  # Raises an exception for HTTP error codes
        games = response.json().get('data', [])

        # Process and structure the game data for easy display
        formatted_games = []
        for game in games:
            game_info = {
                'date': game['date'],
                'home_team': game['home_team']['full_name'],
                'away_team': game['visitor_team']['full_name'],
                'home_score': game.get('home_team_score'),
                'visitor_score': game.get('visitor_team_score'),
                'status': 'Final' if game['status'] == 'Final' else 'Upcoming',
                'series_text': game.get('seriesText', 'Series tied 0-0'),
            }
            formatted_games.append(game_info)

        return formatted_games
    except requests.RequestException as e:
        return {'error': str(e)}

# Usage example:
# api_key = 'your_api_key_here'
# games_info = fetch_games(api_key)
# for game in games_info:
#     print(game)
