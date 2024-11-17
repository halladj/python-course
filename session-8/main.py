from flask import Flask



app = Flask(__name__)
@app.route("/")
def home():
    return "bonjour, le monde"

@app.route("/user/<name>")
def user(name):
    return f"{name} page"

@app.route("/aboutme")
def aboutme():


    return {
        "name" : "abdou",
        "age" : 22
        }


@app.route("/animal/<type>")
def animaltype(type):
    if type == "cow":
        return{
            "name": "cow",
            "sound": "muu",
            "env": "farm"
        }
    elif type == "cat":
        return{
            "name": "cat",
            "sound": "meaw",
            "env": "house"

        }
    else:
        return{
            "error":"dont know this animal"
        }

    

if __name__=="__main__":
    app.run(debug=True)