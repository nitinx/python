# 05 Oct 2017 | Returns API Key(s)

import json


class NXAuth:

    def key_twitter(self):
        # Open KEY files
        with open('c:\\DEV\\GitHub\\python\\keys\\twitter.key') as key_file:
            key = json.load(key_file)
        return key

    def key_zomato(self):
        # Open KEY files
        with open('c:\\DEV\\GitHub\\python\\keys\\zomato.key') as key_file:
            key = json.load(key_file)
        return key

    def key_instagram(self):
        # Open KEY files
        with open('c:\\DEV\\GitHub\\python\\keys\\instagram.key') as key_file:
            key = json.load(key_file)
        return key

    def key_facebook(self):
        # Open KEY files
        with open('c:\\DEV\\GitHub\\python\\keys\\facebook.key') as key_file:
            key = json.load(key_file)
        return key
