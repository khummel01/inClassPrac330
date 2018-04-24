from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/processform')
def procform():
	limit = int(request.args.get('numodds'))
	numLst = range(1, limit*2, 2)
	return render_template('oddsoutput.html', outputodds=numLst)

if __name__ == '__main__':
	app.run(debug=True)
