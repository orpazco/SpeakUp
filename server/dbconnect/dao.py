from sqlite3 import connect
from dbconnect.dto import User, Company,Issue, Comment

class _Users:
    def __init__(self, connect):
            self._connect = connect

    def insert(self, user):
        self._connect.execute("""
        INSERT INTO users (username, password) VALUES (%s, %s)
        """, [user.username, user.password])

    def delete(self, user):
        self._connect.execute("""
        DELETE FROM users WHERE username=(%s) and password=(%s)
        """, [user.username, user.password])

    def udpate(self, user):
        self._connect.execute("""
        UPDATE users SET password=(%s) WHERE username=(%s)
        """, [user.password, user.username])

    def get(self, user):
        conn = self._connect.cursor()
        conn.execute("""
        SELECT * FROM users WHERE username=(%s)
        """, [user.username])
        return User(*conn.fetchone())


class _Companies:
    def __init__(self, connect):
            self._connect = connect

    def insert(self, company): 
        conn = self._connect.cursor()
        conn.execute("""
        INSERT INTO companies (name, password)
        OUTPUT Inserted.ID
        VALUES (%s, %s)
        """, [company.name, company.password])
        return str(*conn.fetchone())

    def delete(self, company):
        self._connect.execute("""
        DELETE FROM companies WHERE username=(%s) and password=(%s)
        """, [company.username, company.password])

    def get_labels(self, company):
        conn = self._connect.cursor()
        conn.execute("""
        SELECT labels FROM companies WHERE name = (%s)
        """, [company.name])
        return list(*conn.fetchone())

    def add_labels(self, company):
        self._connect.execute("""
        UPDATE companies SET labels || (%s) WHERE name=(%s)
        """, [company.labels, company.name])

    def update_labels_after_remove(self, company):
        self._connect.execute("""
        UPDATE companies SET labels = (%s) WHERE name=(%s)
        """, [company.labes, company.name])
    
    def get_all_by_label(self, company):
        conn = self._connect.cursor()
        conn.execute("""
        SELECT name WHERE (%s) IN labels
        """, company.labels)
        return list(*conn.fetchall())

class _Issues:
    def __init__(self, connect):
        self._connect = connect

    def insert(self, issue):
        conn = self._connect.cursor()
        conn.execute("""
        INSERT INTO issues (date, title, content, labels, is_annonymus, user_id)
        OUTPUT Inserted.ID
        VALUES (?, %s, %s, %s, %s, %d)
        """, [issue.date, issue.title, issue.content, issue.labels, issue.is_annonymus, issue.user_id])
        return str(*conn.fetchone())

    def delete(self, issue):
        self._connect.execute("""
        DELETE FROM issues WHERE id=(%s)
        """, [issue.id])

class _Comments:
    def __init__(self, connect):
        self._connect = connect

    def insert(self, comment):
        self._connect.execute("""
        INSERT INTO comments (issue_id, date, content, poster) VALUES (%d, ?, %s, %s)
        """, [comment.issue_id, comment.date, comment.content, comment.poster])