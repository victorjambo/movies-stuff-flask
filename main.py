"""Flask test tutorial by thenewboston
"""

from flask import Flask, render_template
from data import Movies, Shows, ItunesMovies
app = Flask(__name__)

Movies = Movies()
Shows = Shows()
ItunesMovies = ItunesMovies()
ItunesMovies = ItunesMovies["feed"]["entry"]
notFound = "Not Found"


@app.route('/')
def index():
    """Main/home page"""
    return render_template('index.html', movies=Movies, shows=Shows)


@app.route('/celebs')
def celebs():
    """celebs and photos page"""
    return 'ItunesMovies'


@app.route('/movies')
def movies():
    """celebs and photos page"""
    return render_template('movies.html', external=ItunesMovies)


@app.route('/profile/<int:id>')
def profile(id):
    """Shows a single video"""
    Movie = {}
    for item in Movies + Shows:
        if item['id'] == id:
            Movie = item
            break
    if Movie:
        return render_template('profile.html', movie=Movie)
    else:
        return render_template('404.html'), 404


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


if __name__ == "__main__":
    app.run(debug=True)
