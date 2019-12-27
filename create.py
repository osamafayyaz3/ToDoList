from flask import Flask, render_template, request
from model import *

app = Flask(__name__)


app.config["SQLALCHEMY_DATABASE_URI"] = 'postgres://bsrlhmynyfunyf:9e48e516537a7940762dadb66d6d15b17f2ac0b972d3468724dab1432d4a4e8f@ec2-107-21-214-222.compute-1.amazonaws.com:5432/du7dthddv5mf7'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)


def main():
    db.create_all()



if __name__ == "__main__":
    with app.app_context():
        main()