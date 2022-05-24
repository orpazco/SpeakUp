from flask import Flask, request
from server.dbconnect import queries as q

app = Flask(__name__)


@app.route('/register_user', methods=['POST'])
def register_user():
    data = request.json
    username = data.username
    password = data.password
    # check if username exists
    if not q.user_exists(username):
        id = q.register_user(username, password)
        return id
    else:
        return -1


@app.route('/unregister_user', methods=['POST'])
def unregister_user():
    data = request.json
    username = data.username
    password = data.password
    return q.unregister(username, password)


@app.route('/update_password', methods=['POST'])
def update_password():
    data = request.json
    username = data.username
    password = data.password
    if q.user_exists(username):
        update_password(username, password)


@app.route('/register_company', methods=['POST'])
def register_company():
    data = request.json
    company_name = data.username
    password = data.password
    q.register_company(company_name, password)


@app.route('/unregister_company', methods=['POST'])
def unregister_company():
    data = request.json
    company_name = data.username
    password = data.password
    q.unregister_company(company_name, password)


@app.route('/subscribe_labels', methods=['POST'])
def sub_to_labels():
    data = request.json
    name = data.company
    labels = data.labels
    q.sub_to_labels(name, labels)


@app.route('/unsubscribe_labels', methods=['POST'])
def unsub_from_labels():
    data = request.json
    name = data.company
    labels = data.labels
    q.unsub_from_labels(name, labels)


@app.route('/get_subbed_companies', methods=['GET'])
def get_subbed_companies():
    labels = request.args.get("labels")
    return q.get_subbed_companies(labels)


@app.route('/submit_issue_anonymous', methods=['POST'])
def submit_issue_ann():
    data = request.json
    message = data.content
    title = data.title
    labels = data.labels
    q.submit_annonymus_issue(title, message, labels)


@app.route('/submit_issue_registered', methods=['POST'])
def submit_issue_reg():
    data = request.json
    message = data.content
    title = data.title
    labels = data.labels
    user = data.username
    q.submit_registered_issue(title, message, labels, user)


@app.route('/delete_issue', methods=['GET'])
def delete_issue():
    issue_id = request.args.get("issue_id")
    q.delet_issue(issue_id)


@app.route('/add_comment', methods=['POST'])
def comment():
    data = request.json
    issue_id = data.issue_id
    content = data.comment
    poster = data.poster
    q.add_comment(issue_id, content, poster)
