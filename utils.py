import sqlite3

from flask import jsonify


def search_by_title(movie_title):
    con = sqlite3.connect("netflix.db")
    cur = con.cursor()
    query = f"""
                SELECT title, country, release_year, listed_in, description 
                FROM netflix 
                WHERE lower(title) LIKE '%{movie_title}%' 
                ORDER BY release_year desc 
    """
    cur.execute(query)
    data = cur.fetchone()
    con.close()
    new_data = []
    for i in data:
        movie_data = {
            "title": i[0],
            "country": i[1],
            "release_year": i[2],
            "genre": i[3],
            "description": i[4]
        }
        new_data.append(movie_data)
    return new_data


def search_by_year(year_1, year_2):
    con = sqlite3.connect("netflix.db")
    cur = con.cursor()
    query = f"""
                SELECT title, release_year FROM netflix
                WHERE release_year BETWEEN '{year_1}' AND '{year_2}'
                LIMIT 100
                
    """
    cur.execute(query)
    data = cur.fetchall()
    con.close()
    new_data = []
    for i in data:
        movie_data = {
            "title": i[0],
            "release_year": i[1]
        }
        new_data.append(movie_data)
    return new_data


def get_rating(group):
    if group.lower() == 'children':
        return 'G'
    elif group.lower() == 'family':
        return 'G', 'PG', 'PG-13'
    elif group.lower() == 'adult':
        return 'R', 'NC-17'
    else:
        return 'There is no such group'


def search_by_rating_query(rating):
    con = sqlite3.connect("netflix.db")
    cur = con.cursor()
    query = f"""
                    SELECT title, rating, description FROM netflix
                    WHERE rating = '{rating}' AND type='Movie'
                    LIMIT 1000

        """
    cur.execute(query)
    data = cur.fetchall()
    con.close()

    group = []
    for i in data:
        movie_info = {
            "title": i[0],
            "rating": i[1],
            "description": i[2]
        }
        group.append(movie_info)
    return group


def search_by_genre(genre):
    con = sqlite3.connect("netflix.db")
    cur = con.cursor()
    query = f"""
                       SELECT title, description FROM netflix
                       WHERE listed_in LIKE '%{genre.lower()}%' AND type='Movie'
                       ORDER BY release_year 
                       LIMIT 10

           """
    cur.execute(query)
    data = cur.fetchall()
    con.close()

    new_data = []
    for i in data:
        movie_info = {
            "title": i[0],
            "description": i[1]
        }
        new_data.append(movie_info)
    return new_data


def type_of_picture(picture_type, release_year, listed_in):
    con = sqlite3.connect("netflix.db")
    cur = con.cursor()
    query = f"""
                           SELECT title, description FROM netflix
                           WHERE listed_in LIKE '%{listed_in}%' AND type='{picture_type}' AND release_year='{release_year}' 

               """
    cur.execute(query)
    data = cur.fetchall()
    con.close()
    return jsonify(data)
