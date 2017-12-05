# 27 Nov 2017 | TMDb API

import tmdbsimple as tmdb
tmdb.API_KEY = '8bb773d788328379a26c865c78d3c855'

#Method: Search
search = tmdb.Search()
response = search.movie(query='2017', year=2017)
c = 1
for s in search.results:
    print(c, s['id'], s['release_date'], s['popularity'], s['title'])
    c = c + 1

#Method: Search
search = tmdb.Discover()
response = search.movie(primary_release_year=2017)
c = 1
for s in search.results:
    print(c, s['id'], s['release_date'], s['vote_average'], s['popularity'], s['title'])
    c = c + 1

#Method: Movies
#movie = tmdb.Movies(366003)
#response = movie.info()
#print(movie.title)
