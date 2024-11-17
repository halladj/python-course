from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory storage for name-age pairs
email_name_age_grade_pairs = []

# Routes
@app.route('/')
def index():
    return render_template("form.html")


@app.route('/submit', methods=['POST'])
def submit():
    email = request.form.get('email')
    name = request.form.get('name')
    age = request.form.get('age')
    grade = request.form.get('grade')
    
    if email and name and age.isdigit():
        # Append the name and age as a dictionary to name_age_pairs
        email_name_age_grade_pairs.append({
            'email': email, 
            'name': name, 
            'age': int(age), 
            'grade': grade
        })
    else:
        print("Invalid data submitted")  # Debugging message

    # Redirect to the display page to show updated list
    return redirect(url_for('display'))

@app.route('/display')
def display():
    # Debugging: Print out current state of name_age_pairs
    print("Current email_name_age_grade_pairs:", email_name_age_grade_pairs)
    return render_template('display.html', email_name_age_grade_pairs=email_name_age_grade_pairs)

if __name__ == '__main__':
    app.run(debug=True)
