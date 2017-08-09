from flask import Flask
from flask import render_template
import json
import codecs

app = Flask(__name__)

def readJson(json_name):
	file_text=''
	json_folder = 'static/json/'
	file = codecs.open(json_folder+json_name+'.json', 'r+','utf-8')
	# file = open(json_folder+student_number+'.json', 'r+',encoding='utf-8')
	file_text = file.read()
	file_text = json.loads(file_text)
	return file_text

@app.route('/')
def homepage():
	json_text = readJson("index")
	return render_template('index.html',data=json_text)

@app.route('/<string:student_number>/details')
def intro(student_number):
	file_text = readJson(student_number)
	return render_template(str(student_number)+".html", data=dict(file_text))

if __name__ == '__main__':
	app.run(debug=True)
