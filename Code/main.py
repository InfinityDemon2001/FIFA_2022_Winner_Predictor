from bs4 import BeautifulSoup
import requests
import pandas as pd

years = [1930, 1934, 1938, 1950, 1954, 1958, 1962, 1966, 1970, 1974, 1978, 1982, 1986, 1990, 1994, 1998, 2002, 2006, 2010, 2014, 2018]

# Function to get results of all the previous FIFA matches
def get_matches(year):
    web = f'https://en.wikipedia.org/wiki/{year}_FIFA_World_Cup'
    response = requests.get(web)
    content = response.text
    soup = BeautifulSoup(content, 'lxml')
    
    matches = soup.find_all('div', 'footballbox')
    
    home = []
    score = []
    away = []
    
    for match in matches:
        home.append(match.find('th', 'fhome').get_text())
        score.append(match.find('th', 'fscore').get_text())
        away.append(match.find('th', 'faway').get_text())
    
    dict_football = {'home': home, 'score': score, 'away': away}
    df_football = pd.DataFrame(dict_football)
    df_football['year'] = year
    return df_football

# Function to get fixtures of current FIFA World Cup
def get_fixture():
    web = 'https://web.archive.org/web/20221115040351/https://en.wikipedia.org/wiki/2022_FIFA_World_Cup'
    response = requests.get(web)
    content = response.text
    soup = BeautifulSoup(content, 'lxml')
    
    matches = soup.find_all('div', 'footballbox')
    
    home = []
    score = []
    away = []
    
    for match in matches:
        home.append(match.find('th', 'fhome').get_text())
        score.append(match.find('th', 'fscore').get_text())
        away.append(match.find('th', 'faway').get_text())
    
    dict_football = {'home': home, 'score': score, 'away': away}
    df_football = pd.DataFrame(dict_football)
    df_football['year'] = '2022'
    return df_football

# Historical Data
fifa = [get_matches(year) for year in years]
df_fifa = pd.concat(fifa, ignore_index = True)
df_fifa.to_csv('fifa_worldcup_matches.csv', index = False)

# Fixture
df_fixture = get_fixture()
df_fixture.to_csv('fifa_worldcup_fixture.csv', index = False)