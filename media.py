import webbrowser

class Movie():
    """reperesent a movie inforamtions and operations

        Attributes:
            title.
            story line.
            poster image.
            youtube trailer.


    """
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        """the constructor to intialize all the attributes"""
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        """show the movie trailer"""
        webbrowser.open(self.trailer_youtube_url)
