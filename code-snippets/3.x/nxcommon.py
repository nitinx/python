# 05 Oct 2017 | Common Functionality
# -| Returns API Key(s)
# -| Oracle Functions

import json
import cx_Oracle


class NXKey:

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


class NXOracle:

    def db_start(self):
        print("Oracle DB: Starting up...")
        print("Oracle DB: Started.")

    def db_stop(self):
        print("Oracle DB: Stopping...")
        print("Oracle DB: Stopped")

    def db_login(self):
        print("Oracle DB: Logging in...")

        with open('c:\\DEV\\GitHub\\python\\keys\\oracle.key') as key_file_oracle:
            key_oracle = json.load(key_file_oracle)

        connection = cx_Oracle.connect(key_oracle[0]['USER'],
                                       key_oracle[0]['PASSWORD'],
                                       key_oracle[0]['CONNECT_STRING'])

        print("Oracle DB: Logged in")
        return connection
