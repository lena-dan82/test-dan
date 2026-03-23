from flask import Flask, render_template

app = Flask(__name__)

# Главная страница
@app.route('/')
def index():
    return render_template('index.html')

# Страница блога
@app.route('/blog')
def blog():
    return render_template('blog.html')

# Страница контактов
@app.route('/contacts')
def contacts():
    return render_template('contacts.html')

if __name__ == '__main__':
    app.run()