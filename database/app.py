from flask import Flask, request, render_template
import psycopg2

app = Flask(__name__)

@app.route("/")
def index():
	return render_template('index.html')

@app.route('/processform')
def createTable():
	conn = psycopg2.connect(user="hummka01", host="knuth.luther.edu", port=2345, dbname="world")
	curs = conn.cursor()
	cur.execute(""""select * from country limit 10""")
	res = cur.fetchall()
	return render_template("/worldTable", data=res)