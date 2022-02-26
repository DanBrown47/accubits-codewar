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
    cursor.execute('SELECT * FROM movies WHERE rating = ? ORDER BY RATING DESC', (rating,))
    tabulate_data(cursor.fetchall())

def get_by_name(parser:any) -> None:
    name = parser.parse_args().search
    cursor.execute('SELECT * FROM movies WHERE name = ?', (name,))
    tabulate_data(cursor.fetchall())


def get_all() -> None:
    cursor.execute('SELECT * FROM movies')
    print(cursor.fetchall())

def check_args() -> None:
    parser = argparse.ArgumentParser(description='Movie Database Sorting Script')
    parser.add_argument('-y', '--year', help='Add this tag to query for the best movie in the year', required=False)
    parser.add_argument('-r', '--rating', help='Add this tag to query for the best movie in the rating', required=False)
    parser.add_argument('-s', '--search', help='search for a movie in database', required=False)
    parser.add_argument('-a', '--all', help='Get all the movies in the Database', required=False)

    if not len(sys.argv) > 1:
        parser.print_help()
    
    if parser.parse_args().year:
        get_by_year(parser)
    elif parser.parse_args().rating:
        get_by_rating(parser)
    elif parser.parse_args().search:
        get_by_name(parser)
    elif parser.parse_args().all:
        get_all()
    elif parser.parse_args().all:
        get_all()
    else:
        parser.print_help()
        
if __name__=="__main__":
    check_args()