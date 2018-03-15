from flask import Flask, request, jsonify, Response

app = Flask(__name__)

@app.route('/adder') 
def addNums(): 
	num1 = int(request.args['num1'])
	num2 = int(request.args['num2'])
	
	# res = Response(json.dumps(num1+num2))
	# res.headers = {'Content-Type': 'application/json'}
	# return res
	
	return jsonify(num1+num2)

app.run(debug=True, port=5001)
# to run: in terminal write python3 adder.py
