import string


def register_user(username, password): pass

def unregister(username, password): pass

def udpate_password(username, password):pass

def user_exists(username): pass

def register_company(name, password): pass #return company id

def unregister_company(name, password): pass

def sub_to_labels(copany_name: string, labels: list): pass

def unsub_from_labels(company_name: string, labels: list): pass

def get_subbed_companies(labels: list): pass

def submit_annonymus_issue(title, content, labels): pass #return issue_id

def submit_registered_issue(title, content, labels, username): pass #return issue_id

def delet_issue(issue_id): pass

def is_signin_valid(username, password): pass

def add_comment(issue_id, content, poster): pass #return comment_id