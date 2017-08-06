from flask import Flask
from flask import render_template
import json
import codecs

app = Flask(__name__)

def readJson(student_number):
	file_text=''
	json_folder = 'static/json/'
	try:
		file = codecs.open(json_folder+student_number+'.json', 'r+','utf-8')
		# file = open(json_folder+student_number+'.json', 'r+',encoding='utf-8')
	except:
		print ("!!!cannot open!!!")
	try:		
		file_text = file.read()
		file_text = dict(json.loads(file_text))
	except:
		print ("!!!cannot read!!!")
		print (file_text)
	return file_text

@app.route('/')
def homepage():
	return render_template('index.html')

@app.route('/<string:student_number>')
def intro(student_number):
	file_text = readJson(student_number)
	return render_template(str(student_number)+".html", data=file_text)

if __name__ == '__main__':
	app.run(debug=True)
