from data import db_session
from flask import Flask, render_template

from data.users import User
from data.jobs import Jobs

app = Flask(__name__)
app.config['SECRET_KEY'] = 'you_will_never_pass_my_password'


@app.route('/')
@app.route('/index')
def main():
    db_session.global_init("db/mars_explorer.db")
    session = db_session.create_session()
    sp = session.query(Jobs).all()
    action_list = []
    for elem in sp:
        leader = session.query(User).filter(User.id == elem.team_leader).first()
        action_list.append([elem.id, elem.job, leader.surname + ' ' + leader.name, elem.work_size,
                            elem.collaborators, elem.is_finished])
    return render_template('index.html', actions=action_list)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
