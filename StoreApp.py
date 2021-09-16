from flask import Flask, jsonify, request

app = Flask(__name__)

stores=[
			{
				'name' : 'My Store',
				'items': [
                {
							'name':'Pen',
							'price':'10'
                            }
						]
			}
		]
		
@app.route('/store')
def get_stores():
	return jsonify({'stores':stores})
    
@app.route('/store/<string:name>')
def get_store(name):
    for i in  stores:
        if i['name'] == name:
            return jsonify(i)
@app.route('/store', methods = ['POST'])
def create_store():
    data = request.get_json()
    stores.append(data)
    return jsonify(data)
    
@app.route('/store/<string:name>', methods = ['POST'])
def create_item_in_store(name):
    data = request.get_json()
    for i in stores:
        if i["name"] == name:
            i["items"].append(data)
    return jsonify(data)
		
app.run(port=3000)