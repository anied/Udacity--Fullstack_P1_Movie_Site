from movie_site import fetch_movies, get_movie_trailer
from fresh_tomatoes import make_movies_page, open_movies_page
from media import Movie
from json import dumps as json_dumps
from os import path
from calendar import timegm as calendar_timegm
from time import gmtime as time_gmtime


def make_movie(movie_obj):
    return Movie(movie_title=movie_obj['title'],
                 movie_synopsis=movie_obj['overview'],
                 movie_poster="https://image.tmdb.org/t/p/w370" + movie_obj['poster_path'],
                 movie_trailer=movie_obj['trailer_url'],
                 movie_release_date=movie_obj['release_date']
                 )


now = calendar_timegm(time_gmtime())

movie_load_list = []

# if content_cache.json exists (short-circuit) and it has been modified within the last 24 hours...
if path.exists('content_cache.json') and now - path.getmtime('content_cache.json') < (60*60*60):
    # we can use the cached content
    print "Using cache"
else:
    # fetch fresh data and build it anew
    print "Fetching movie data..."

    movies_array = fetch_movies()

    for movie_obj in movies_array:  # this is a little redundant, but writing it this way prevents us from iterating over the content twice, checking for the presensce of a 'trailer_url' key on each movie object before deciding if we need to fetch it.
        movie_obj['trailer_url'] = get_movie_trailer(movie_obj['id'])
        movie_load_list.append(make_movie(movie_obj))

    with open('content_cache.json', 'w') as cache_file:
        cache_file.write(json_dumps(movies_array))
        make_movies_page(movie_load_list)

open_movies_page()
