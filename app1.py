from flask import Flask, request
from concord_result import concordance
from nltk.text import ConcordanceIndex

import nltk

app1 = Flask(__name__)

a=open("corpus.txt", "rU")
text=a.read()
text_a=text.lower()
text_b=text_a.split()
corpus=nltk.Text(text_b)

@app1.route('/form-example', methods=['GET', 'POST'])
def form_example():
	if request.method == 'POST':
		term = request.form.get('term')
		ci = ConcordanceIndex(corpus.tokens)
		results = concordance(ci, term)
		
		return '''<h1>The language value is: {}</h1>'''.format(results)
		
	return '''<form method="POST">
			This form contains the text of all <i>Los Angeles Times</i> articles containing the words "Filipino" or "Philippines" between January 1929 and June 1930. <br>
			<br>
			Enter your search term to find its concordance in the text corpus.<br>
			Term: <input type="text" name="term"><br>
			<input type="submit" value="Submit"><br>
			<br>
			This site uses NLTK and Flask.<br>
		</form>'''
		
if __name__ == '__main__':
	app1.run(debug=True, port=5000)