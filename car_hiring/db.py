import pymysql
from flask import app


class DB():

    def __init__(self, host, user, db, password):
        self.host = host
        self.user = user
        self.db = db
        self.password = password

    def mysqlconnect(self):
        # To connect MySQL database
        conn = pymysql.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            db=self.db,
        )
        return conn