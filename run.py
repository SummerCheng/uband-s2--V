from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def homepage():
	return render_template('index.html')

@app.route('/<string:student_number>/details')
def intro(student_number):
	return render_template(str(student_number)+".html")

# @app.route('/A10134')
# def introl():
# 	return render_template('html-test.html')

# @app.route('/A10509')
# def introv():
# 	return render_template('v.html')

if __name__ == '__main__':
    app.run(debug=True)
