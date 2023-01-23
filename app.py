from flask import Flask
from utils import *

app = Flask(__name__)


@app.route('/movie/<title>')
def movie_page(title):
    data = search_by_title(title)
    return jsonify(data)


@app.route('/movie/<year_1>/to/<year_2>')
def search_by_year_page(year_1, year_2):
    data = search_by_year(year_1, year_2)
    return jsonify(data)


@app.route('/rating/<group>')
def search_by_group_page(group):
    rating = get_rating(group)
    data = search_by_rating_query(rating)
    return jsonify(data)


@app.route('/genre/<genre>')
def search_by_genre_page(genre):
    data = search_by_genre(genre)
    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True)
