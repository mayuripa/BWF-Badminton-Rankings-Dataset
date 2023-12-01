import csv
from bs4 import BeautifulSoup

# Sample HTML content, replace this with your actual HTML content
content = """
 
"""

soup = BeautifulSoup(content, 'html.parser')

def get_full_name(span_container):
    first_name = span_container.find('span', class_='name-1').get_text(strip=True)
    last_name = span_container.find('span', class_='name-2').get_text(strip=True)
    return f"{first_name} {last_name}"

# Extract data from table rows
players_data = []

for tr in soup.find_all('tr'):
    rank = tr.find('span', class_='rank-value').get_text(strip=True)
    
    player_div = tr.find('div', class_='player')
    spans = player_div.find_all('span', recursive=False)  # direct children spans only
    
    player1_name = get_full_name(spans[0])
    
    # Check if there's a second player, if so, extract their name
    player2_name = get_full_name(spans[1]) if len(spans) > 1 else None
    
    # Extracting other data can remain the same
    country_img = tr.find('td', {'class': 'col-country'}).find('img')
    country = country_img['title'] if country_img else None
    tournaments = tr.find('td', class_='col-tmt').get_text(strip=True)
    points = tr.find('td', class_='col-points').get_text(strip=True)
    
    player_data = {
        'ranking': rank,
        'player1_name': player1_name,
        'player2_name': player2_name,
        'country': country,
        'tournaments': tournaments,
        'points': points
    }
    
    players_data.append(player_data)

# Save to CSV file
with open('fifteen_mixD.csv', 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['ranking', 'player1_name', 'player2_name', 'country', 'tournaments', 'points']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for player in players_data:
        writer.writerow(player)


