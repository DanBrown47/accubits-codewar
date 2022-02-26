# Accubits Code wars

# Import message
from bs4 import BeautifulSoup
import requests
import sqlite3
from sqlite3 import Error
from urllib.parse import urljoin


# GLOBAL VARIABLES

# No user input is taken
SCRAP_URL = 'https://www.imdb.com/chart/top/?ref_=nv_mv_250'
USER_AGENT  = "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36"

def write_db(list_movies:list) -> None:
    conn = sqlite3.connect('movies.db')
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS movies (id INTEGER PRIMARY KEY, name TEXT, year TEXT, rating TEXT, link TEXT)')
    for movie in list_movies:
        print(str(movie)+'\n')
        cursor.execute('INSERT INTO movies VALUES (?,?,?,?,?)',movie)
    conn.commit()
    conn.close()

def prober(SCRAP_URL:str) -> list:
    list_movies = []
    page = requests.get(SCRAP_URL, headers={'User-Agent': USER_AGENT})
    soup = BeautifulSoup(page.text,'lxml')
    movie = soup.find('tbody',class_='lister-list')
    count = 1
    for tr in movie.find_all('tr'):

        name = tr.find('td',class_='titleColumn').a.text
        link = tr.find('td',class_='titleColumn').a['href']
        year = tr.find('span',class_='secondaryInfo').text
        rating = tr.find('td',class_='ratingColumn imdbRating').text
        mv_link = 'https://imdb.com{0}'.format(link)
        count = count + 1
        list_movies.append((count,name,year,rating,mv_link))
    return list_movies
if __name__ == '__main__':
    movies_list = prober(SCRAP_URL)
    write_db(movies_list)