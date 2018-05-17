from flask import Flask, request

app1 = Flask(__name__)

import nltk

a=open("all.txt", "rU")
text=a.read()
text_a=text.lower()
text_b=text_a.split()
corpus=nltk.Text(text_b)

@app1.route('/form-example', methods=['GET', 'POST'])
def form_example():
	if request.method == 'POST':
		term = request.form.get('term')
		foo=len(corpus)
		
		return '''<h1>The language value is: {}</h1>'''.format(foo)
		
	return '''<form method="POST">
			Term: <input type="text" name="term"><br>
			<input type="submit" value="Submit"><br>
		</form>'''
		


@app1.route('/query-example')
def query_example():
	language = request.args.get('language')
	framework = request.args['framework']
	website = request.args.get('website')
	
	return '''<h1>The language value is: {}</h1>
	<h1>The framework value is: {}</h1>
	<h1>The website value is: {}'''.format(language, framework, website)
	

	
@app1.route('/json-example', methods=['POST'])
def json_example():
	req_data = request.get_json()
	
	language = req_data['language']
	framework = req_data['framework']
	python_version = req_data['version_info']['python']
	example = req_data['examples'][0]
	boolean_test = req_data['boolean_test']
	
	return '''
			The language value is: {}
			The framework value is: {}
			The Python version is: {}
			The item at index 0 in the example list is: {}
			The boolean value is: {}'''.format(language, framework, python_version, example, boolean_test)
	
if __name__ == '__main__':
	app1.run(debug=True, port=5000)
	