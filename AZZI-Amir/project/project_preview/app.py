from flask import Flask, render_template, request, redirect, url_for
import time
app = Flask(__name__)

# In-memory storage for name-age pairs
name_age_pairs = []
email_phone = []
uni_level = []
# Routes
@app.route('/')
def index():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form.get('name')
    age = request.form.get('age')
    email = request.form.get('email')
    phone = request.form.get('phone')

    # Check if name and age inputs are valid
    if name and age and email and phone.isdigit():
        # Append the name and age as a dictionary to name_age_pairs
        name_age_pairs.append({'name': name, 'age': int(age)})
        email_phone.append({'email': email, 'phone': phone})
    else:
        print("Invalid data submitted")  # Debugging message

    # Redirect to the display page to show updated list
    return redirect(url_for('display'))

@app.route('/display')
def display():
    # Debugging: Print out current state of name_age_pairs
    print("Current :", name_age_pairs, email_phone)
    return render_template('display.html', name_age_pairs=name_age_pairs, email_phone=email_phone)

@app.route('/form')
def form():
    return render_template('form2.html')

@app.route('/form2', methods=['POST'])
def form2():
    university = request.form.get('university')
    level = request.form.get('level')
    if university and level.isdigit():
       
        uni_level.append({'university': university, 'level': level})
    else:
        print("Invalid data submitted")  # Debugging message

    return redirect(url_for('display2'))
@app.route('/display2')
def display2():
    return render_template('display2.html', uni_level=uni_level)
    
    
    
   

@app.route('/delete', methods=['POST'])
def delete():
   # name = request.form.get('name')
    #age = request.form.get('age')
    #email = request.form.get('email')
    #phone = request.form.get('phone')
    #if name and age and email and phone
    pass
@app.route('/sleep')
def sleep():
    pass 

    

if __name__ == '__main__':
    app.run(debug=True)
