from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def films():
    context = {
        "link": "Перейти в кинотеатр"
    }
    return render_template("home.html", **context)

@app.route("/blog/")
def person():
    context = {
        "link": "Зайти в кинотеатр"
    }
    return render_template("about.html", **context)

if __name__ == "__main__":
    app.run()