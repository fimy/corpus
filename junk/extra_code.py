# app_extra_code

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
	

	