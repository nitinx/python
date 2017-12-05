# 09 Nov 2017 | OMDb API Integration
'''
http://www.omdbapi.com/
https://github.com/dgilland/omdb.py
'''

import omdb

omdb.set_default('apikey', '6cf170d0')

# must use OMDb API parameters
res = omdb.request(t='True Grit', year=1969, r='json', apikey='6cf170d0')
#res = omdb.request(t='True Grit', year=1969, r='json')

#res = omdb.request(y=2017, r='json', apikey='6cf170d0')
print(res.content)

#src = omdb.search_movie(2017)
src = omdb.search(year=2017)
print(src)
