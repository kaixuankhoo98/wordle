from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route("/")
def on_open():
    return redirect("/home/")

@app.route("/home/")
def home():
    return render_template("main_page.html")

@app.route("/game/")
def game(g1="     ",g2="     ",g3="     ",g4="     ",g5="     ",g6="     "):
    g1 = "guess"
    return render_template("game.html",g1=g1,g2=g2,g3=g3,g4=g4,g5=g5,g6=g6)

@app.route("/future_updates/")
def future():
    return render_template("future_updates.html")

@app.route("/about_me/")
def about():
    return render_template("about_me.html")

if __name__ == "__main__":
    app.run(debug=True)