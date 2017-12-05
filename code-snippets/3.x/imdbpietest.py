# 12 Nov 2017 | Checking out imdbpie

from imdbpie import Imdb

imdb = Imdb()
lst = imdb.search_for_title("The Dark Knight")
print(lst)
