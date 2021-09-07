from flask import Flask, jsonify, render_template, request
from gevent.pywsgi import  WSGIServer
import requests

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])

def raiz():
	
	return render_template('/email.html', email='email')
	
@app.route('/dados', methods=['GET', 'POST'])

def dados():
	
	email = request.form['email']
	with open ('dados.txt', 'a') as arquivo:
		arquivo.write(str(email) + '\n')
	
	return  '<h1> %s <h1>' %(email)
	
	
#app.run()
server = WSGIServer(('localhost', 5000), app)
server.serve_forever()

