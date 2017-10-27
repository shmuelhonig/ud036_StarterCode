import webbrowser


class Movie():
    """Creates a class to allow for storage of data pertaining to any number of
    movies
    Attributes:
        Film title, film genre, film release year, poster image, trailer video
    """
    def __init__(self, movie_title, movie_genre, movie_year, poster_image,
                 trailer_youtube):
        """Initializes instances of the class with the attributes described
        above and listed below
        """
        self.title = movie_title
        self.genre = movie_genre
        self.release_year = movie_year
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
