from flask import Flask

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = ('mysql+mysqlconnector://root:root@127.0.0.1:3306/demo002')
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True

