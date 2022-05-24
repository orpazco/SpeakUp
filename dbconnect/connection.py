# The Repository
import atexit
import sqlite3

from dao import _Users, _Companies, _Issues, _Comments


class _Repository:
    def __init__(self):
        self._connect = sqlite3.connect('database.db')
        self.vaccines = _Users(self._connect)
        self.suppliers = _Companies(self._connect)
        self.clinics = _Issues(self._connect)
        self.logistics = _Comments(self._connect)

    def _close(self):
        self._connect.commit()
        self._connect.close()

    def create_tables(self):
        self._connect.executescript("""
        DROP TABLE IF EXISTS users;
        CREATE TABLE users (
            username    TEXT     NOT NULL,
            password    TEXT     NOT NULL          
        );

        DROP TABLE IF EXISTS companies;
        CREATE TABLE companies (
            id              INT     PRIMARY KEY,
            name            TEXT    NOT NULL,
            password        TEXT     NOT NULL,
            subbed_labels   TEXT               
        );
        
        DROP TABLE IF EXISTS issues;
        CREATE TABLE issues (
            id              INT     PRIMARY KEY,
            date            DATE    NOT NULL,
            title           TEXT    NOT NULL,
            content         TEXT    NOT NULL,
            labels          TEXT    ,
            is_annonymus    TEXT    NOT NULL,
            user_id         INT     ,

            KEY(user_id)     REFERENCES users(id)
        );
        
        DROP TABLE IF EXISTS comments;
        CREATE TABLE comments (
            comment_id  INT     PRIMARY KEY,
            issue_id    INT     NOT NULL,
            date        DATE    NOT NULL,
            content     TEXT    NOT NULL,
            poster      TEXT    ,

            Key(issue_id)   REFERENCES issues(id)
        );
""")