from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Bonjour, le monde !"

@app.route("/about")
def about():
    return "À propos de nous"


@app.route("/user/<name>")
def user(name):
    return f"Bonjour, {name}!"

if __name__ == "__main__":
    app.run(debug=True)