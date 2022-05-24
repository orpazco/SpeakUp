# Data Transfer Objects:

class User:
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password


class Company:
    def __init__(self, id, name, password, subbed_labels):
        self.id = id
        self.name = name
        self.password = password
        self.subbed_labels = subbed_labels


class Issue:
    def __init__(self, id, date, title, content, labels, is_annonymus, user_id):
        self.id = id
        self.date = date
        self.title = title
        self.content = content
        self.labels = labels
        self.is_annonymus = is_annonymus
        self.user_id = user_id


class Comment:
    def __init__(self, comment_id, issue_id, date, content, poster):
        self.comment_id = comment_id
        self.issue_id = issue_id
        self.date = date
        self.content = content
        self.poster = poster
