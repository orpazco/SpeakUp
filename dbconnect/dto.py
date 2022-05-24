# Data Transfer Objects:

class Issue:
    def __init__(self, id, date, title, content, labels, is_annonymus):
        self.id = id
        self.date = date
        self.title = title
        self.content = content
        self.labels = labels
        self.is_annonymus = is_annonymus


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password


class Company:
    def __init__(self, id, name, password, subbed_labels):
        self.id = id
        self.name = name
        self.password = password
        self.subbed_labels = subbed_labels


class Comment:
    def __init__(self, comment_id, issue_id, date, content, poster):
        self.comment_id = comment_id
        self.issue_id = issue_id
        self.date = date
        self.content = content
        self.poster = poster
