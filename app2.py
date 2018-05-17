from flask import Flask, request

app2 = Flask(__name__)

import nltk

a=open("all.txt", "rU")
text=a.read()
text_a=text.lower()
text_b=text_a.split()
corpus=nltk.Text(text_b)

@app2.route('/form-sample', methods=['GET', 'POST'])
def form_sample():
	return render_template('index.html')
	
if __name__ == '__main__':
	app2.run(debug=True, port=5000)