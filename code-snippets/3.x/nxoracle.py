# 05 Oct 2017 | Oracle Functions

import cx_Oracle
import json


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
