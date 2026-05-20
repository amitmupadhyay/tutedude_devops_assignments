from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient

app = Flask(__name__)

# MongoDB Atlas Connection
client = MongoClient("MONGODB_CONNECTION_STRING_GOES _HERE")

db = client["DB-TuteDude"]
collection = db["Coll-Flask"]

# Home Page with Form
@app.route('/')
def home():
    return render_template('form.html')

# Form Submit
@app.route('/submit', methods=['POST'])
def submit():

    try:
        name = request.form['name']
        email = request.form['email']

        # Insert into MongoDB
        collection.insert_one({
            "name": name,
            "email": email
        })

        # Redirect on success
        return redirect(url_for('success'))

    except Exception as e:
        # Show error on same page
        return render_template('form.html', error=str(e))

# Success Page
@app.route('/success')
def success():
    return render_template('success.html')

if __name__ == '__main__':
    app.run(debug=True)