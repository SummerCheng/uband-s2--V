from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
	print ("h")
	return render_template('index.html')

@app.route('/A10134')
def introl():
	return render_template('html-test.html')

@app.route('/A14075')
def intros():
	return render_template('A14075.html')

@app.route('/B20837')
def introx():
	return render_template('B20837xz.html')

@app.route('/A10509')
def introv():
	return render_template('v.html')


if __name__ == '__main__':
    app.run(debug=True)
