from flask import Flask
from flask import render_template
import json
import codecs

app = Flask(__name__)

def readJson(json_name):
	file_text=''
	json_folder = 'static/json/'
	file = codecs.open(json_folder+json_name+'.json', 'r+','utf-8')
	file_text = file.read()
	file_text = json.loads(file_text)
	return file_text

def readData(text):
	student_json ={}
	for student in json_text:
		if student["student_number"] == student_number:
				return student

@app.route('/')
def homepage():
	json_text = readJson("index")
	return render_template('index.html',data=json_text)

@app.route('/<string:student_number>/details')
def intro(student_number):
	json_text = readJson("index")
	student_json =readData(json_text)
	return render_template("person.html", data=student_json)

@app.route('/<string:student_number>/academy')
def acad(student_number):
	json_text = readJson("index")
	student_json =readData(json_text)
	return render_template("academy.html", data=student_json)

@app.route('/<string:student_number>/life')
def acad(student_number):
	json_text = readJson("index")
	student_json =readData(json_text)
	return render_template("life.html", data=student_json)

@app.route('/<string:student_number>/contact')
def acad(student_number):
	json_text = readJson("index")
	student_json =readData(json_text)
	return render_template("contact.html", data=student_json)


if __name__ == '__main__':
	app.run(debug=True)
	