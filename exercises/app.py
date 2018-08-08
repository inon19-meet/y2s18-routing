from databases import *
from flask import Flask, render_template, url_for
app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/student/<int:student_id>')
def students(student_id):
	return render_template('student.html', id = student_id)

app.run(debug=True)
