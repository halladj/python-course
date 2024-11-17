from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory storage for name-age pairs
name_age_pairs = []

# Routes
@app.route('/')
def index():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form.get('name')
    age = request.form.get('age')

    # Check if name and age inputs are valid
    if name and age.isdigit():
        # Append the name and age as a dictionary to name_age_pairs
        name_age_pairs.append({'name': name, 'age': int(age)})
    else:
        print("Invalid data submitted")  # Debugging message

    # Redirect to the display page to show updated list
    return redirect(url_for('display'))

@app.route('/display')
def display():
    # Debugging: Print out current state of name_age_pairs
    print("Current name_age_pairs:", name_age_pairs)
    return render_template('display.html', name_age_pairs=name_age_pairs)

if __name__ == '__main__':
    app.run(debug=True)
