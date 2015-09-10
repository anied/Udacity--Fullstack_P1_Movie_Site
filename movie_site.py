from urllib import urlopen
from json import loads


def fetch_movies():
    """Fetches JSON object of current popular movies from "TheMovieDB" API"""
    discover_api_base_url = "http://api.themoviedb.org/3/discover/movie"
    sorting_parameter = "sort_by=popularity.desc"
    page_limit = "page=1"
    api_key = "api_key=<YOUR_API_KEY_HERE>"

    fetch_url = discover_api_base_url + '?' + sorting_parameter + '&' + page_limit + '&' + api_key

    api_fetch = urlopen(fetch_url)

    api_response = loads(api_fetch.read())['results']

    return api_response


def get_movie_trailer(movie_id):
    """Uses "TheMovieDB" API to fetch and return movie trailer by movie_id"""

    api_key_parameter = "api_key=<YOUR_API_KEY_HERE>"

    fetch_url = "http://api.themoviedb.org/3/movie/%(id)s/videos?%(api_key)s" % {'id': movie_id, 'api_key': api_key_parameter}

    trailer_fetch = urlopen(fetch_url)

    trailer_info = loads(trailer_fetch.read())['results']

    for trailer in trailer_info:
        if trailer['site'] == "YouTube" and trailer['type'] == "Trailer":
            trailer_url = "https://www.youtube.com/watch?v=" + trailer['key']
            return trailer_url

    return trailer_info  # returns the whole shebang if no video meets the condition-- it would break the page, but give us something in the cache to determine what is happening-- as of now, we've only seen responses that have something that matches, so we can't really plan for alternatives very effectively
