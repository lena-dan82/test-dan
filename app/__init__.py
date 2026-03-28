from flask import Flask

#создаёт экземпляр класса Flask (переменную app)
app = Flask(__name__)

app.config['SECRET_KEY'] = 'my_secret_key'

from app import routes