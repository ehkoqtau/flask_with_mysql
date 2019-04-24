from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost/flask_mysql_test'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(256), nullable=False)
    kelamin = db.Column(db.String(1), nullable=False)
    token = db.Column(db.String(512))
    tgl_buat = db.Column(db.Date(), nullable=False)

    def __init__(self, id, username, email, password, kelamin, token, tgl_buat):
        self.id = id
        self.username = username
        self.email = email
        self.password = password
        self.kelamin = kelamin
        self.token = token
        self.tgl_buat = tgl_buat

    def __repr__(self):
        return '[%s, %s, %s, %s,%s, %s]' % (self.id, self.username, self.email, self.password, self.kelamin, self.token)

db.create_all()

#tambah data
user1 = User('', 'ehkoqtau', 'ehkoqtau@outlook.com', '$2b$12$P7yYNP/8umfG1ATivz77ce4UoWfJhSPHgzHmgryDxyjhAq5sFTzny', '', '', '2019-04-19')
db.session.add(user1)
