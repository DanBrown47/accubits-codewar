# Accubits code war

import sqlite3
import argparse
import sys
from tabulate import tabulate


# connect to database
conn = sqlite3.connect('movies.db')
# create cursor
cursor = conn.cursor()

def tabulate_data(data:list) -> None:
    print(tabulate(data, headers=['id', 'name', 'year', 'rating', 'link']))

def get_by_year(parser:any) -> None:
    year = parser.parse_args().year
    cursor.execute('SELECT * FROM movies WHERE year = ?', (year,))
    tabulate_data(cursor.fetchall())

def get_by_rating(parser:any) -> None:
    rating = parser.parse_args().rating
    cursor.execute('SELECT * FROM movies WHERE rating = ?', (rating,))
    print(cursor.fetchall())

def get_by_name(parser:any) -> None:
    name = parser.parse_args().name
    cursor.execute('SELECT * FROM movies WHERE name = ?', (name,))
    print(cursor.fetchall())

def get_by_genere() -> None:
    pass

def get_all() -> None:
    cursor.execute('SELECT * FROM movies')
    print(cursor.fetchall())

def check_args() -> None:
    parser = argparse.ArgumentParser(description='Movie Database Sorting Script')
    parser.add_argument('-y', '--year', help='Add this tag to query for the best movie in the year', required=False)
    parser.add_argument('-g', '--genre', help='Add this tag to query for the best movie in the genre', required=False)
    parser.add_argument('-a', '--all', help='Get all the movies in the Database')

    if not len(sys.argv) > 1:
        parser.print_help()
    
    if parser.parse_args().year:
        get_by_year(parser)
    elif parser.parse_args().genre:
        get_by_genere()
    elif parser.parse_args().all:
        get_all()
    else:
        parser.print_help()
        
if __name__=="__main__":
    check_args()