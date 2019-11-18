from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Taskes(db.Model):
    __tablename__ = "todo"
    id = db.Column(db.Integer, primary_key=True)
    action = db.Column(db.String, nullable=False)