from webbrowser import open as webbrowser_open
from calendar import month_name as calendar_month_name


class Movie():
    """Class creates a movie object"""
    def __init__(self, movie_title, movie_synopsis, movie_poster, movie_trailer, movie_release_date):
        self.title = movie_title
        self.synopsis = movie_synopsis
        self.poster_image_url = movie_poster
        self.trailer_youtube_url = movie_trailer
        self.release_date = movie_release_date

        release_date_split = movie_release_date.split('-')
        friendly_date_obj = {
            'month': calendar_month_name[int(release_date_split[1])],
            'day': release_date_split[2],
            'year': release_date_split[0]
        }

        self.friendly_release_date = "%(month)s %(day)s, %(year)s" % friendly_date_obj

    def show_trailer(self):
        webbrowser_open(self.trailer)
