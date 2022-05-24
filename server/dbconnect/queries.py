import string
from dto import User, Comment, Issue, Comment
from connection import _Connection


def register_user(conn, username, password):
    conn.users.insert(User(username, password))

def unregister_user(conn, username, password):
    conn.users.delete(User(username, password))

def update_password(conn, username, password):
    conn.users.update(User(username, password))

def user_exists(conn, username):
    if conn.users.get(User(username, "")) == None:
        return False
    else:
        return True

def register_company(conn, name, password):
    conn.companies.insert

def unregister_company(name, password): pass

def sub_to_labels(copany_name: string, labels: list): pass

def unsub_from_labels(company_name: string, labels: list): pass

def get_subbed_companies(labels: list): pass

def submit_annonymus_issue(title, content, labels): pass #return issue_id

def submit_registered_issue(title, content, labels, username): pass #return issue_id

def delete_issue(issue_id): pass

def is_signin_valid(username, password): pass

def add_comment(issue_id, content, poster): pass #return comment_id