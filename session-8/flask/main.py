from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Bonjour, le monde !"


@app.route("/user/<name>")
def user(name):
    return f"{name}'s Page"

@app.route("/aboutme")
def aboutme():
    
    return {
        "name": "hamza",
        "age" : 199
        } 


####
## create an route "/animal", add a param as the animal type,
## return to the client, the animals info as json.
####

@app.route("/animal/<type>")
def animaltype(type):
    if type == "cow":
        return {
            "name" : "cow",
            "sound": "Muu!",
            "env"  : "wild, farm"
        }
    elif type == "cat":
        return {
            "name" : "cat",
            "sound": "Meow!",
            "env"  : "house"
        }
    else:
        return {
            "error": "dont know this animal"
        }

if __name__ == "__main__":
    app.run(debug=True)






