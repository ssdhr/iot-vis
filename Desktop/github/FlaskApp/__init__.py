from flask import Flask, render_template, jsonify, request
import rand_num as rn
from pylab import *
app = Flask(__name__)


@app.route('/_add_numbers')
def add_numbers():
	"""Add two numbers server side, ridiculous but well..."""
#	a = request.args.get('a', 0, type=int)
#	b = request.args.get('b', 0, type=int)
	c = float(rn.randm())
	return jsonify(result = c)

@app.route("/")
def hello():
	return render_template('main.html')

if __name__ == "__main__":
    app.run(debug=True)





