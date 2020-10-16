from __init__ import db


class Task(db.Model):
    id = db.Column(db.INTEGER, primary_key=True)
    title = db.Column(db.String(20), unique=True)
    description = db.Column(db.String(222))

    def __init__(self, title, description):
        self.title = title
        self.description = description


db.create_all()
