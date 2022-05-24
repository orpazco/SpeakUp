import string
from datetime import datetime
from dto import User, Comment, Issue, Comment
from connection import _Connection
from server.dbconnect.dto import Company


def register_user(conn, username, password):
    conn.users.insert(User(username, password))

def unregister_user(conn, username, password):
    conn.users.delete(User(username, password))

def update_password(conn, username, password):
    conn.users.update(User(username, password))

def user_exists(conn, username):
    if conn.users.get(username) == None:
        return False
    else:
        return True

def register_company(conn, name, password):
    conn.companies.insert(Company(name, password, subbed_labels=""))

def unregister_company(conn, name):
    conn.companies.delete(name)

def sub_to_labels(conn, company_name, labels):
    conn.companies.add_labels(company_name, labels)

def unsub_from_labels(conn, company_name, labels):
    curr_labels = conn.companies.get_labels(company_name)
    for label in labels:
        curr_labels.remove(label)
    conn.companies.update_labels_after_remove(company_name)

def get_subbed_companies(conn, labels):
    companies = []
    for label in labels:
        companies.append(conn.companies.get_all_by_label(label))
    return companies

def submit_annonymus_issue(conn, title, content, labels):
    date = date.today().strftime("%d-%m-%Y")
    issue_id = conn.issues.insert(Issue(date, title, content, labels, True, ""))
    return issue_id

def submit_registered_issue(conn, title, content, labels, username):
    date = date.today().strftime("%d-%m-%Y")
    conn.issues.insert(Issue(date, title, content, labels, False, username))

def delete_issue(conn, issue_id):
    conn.issues.delete(issue_id)

def is_signin_valid(conn, username, password): 
    if conn.users.authenticate(User(username,password)) == None:
        return False
    else:
        return True

def add_comment(issue_id, content, poster): pass #return comment_id