# Put and Delete--HTTP verb
# Working with API's --json

from flask import Flask, render_template, request, url_for, redirect, jsonify


app = Flask(__name__)

items = [
    {"id": 1, "name": "Item 1", "description": "This is item 1"},
    {"id": 2, "name": "Item 2", "description": "This is item 2"}
]


@app.route('/')
def display():
    return f"Welcome to the Sample To DO list!! "

# GET:-Retrieve all the data


@app.route('/items')
def get_items():
    return jsonify(items)

# GET:-Retrieve a perticular item based on ID


@app.route('/items/<int:item_id>',methods=['GET'])
def get_item_id(item_id):
    item = next((item for item in items if items['id'] == item_id), None)
    if item == None:
        return jsonify({"item": "NOt found"})
    return jsonify(item)
# post :- Create a new task :API


@app.route('/items', methods=['POST'])
def post_item():
    if not request.json or 'name' not in request.json:
        return jsonify({"item": "NOt found"})
    l = []
    item = {'id': items[-1]['id']+1,
            'name': request.json['name'],
             'description': request.json['description']
            }
    l.append(item)
    return jsonify(item)
# PUT :- update an existing task


@app.route('/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    item = next((item for item in items if item['id'] == item_id), None)
    if item == None:
        return jsonify({"item": "NOt found"})
    item['name'] = request.json.get('name', item['name'])
    item['description'] = request.json.get('description', item['description'])
    return jsonify(item)

# DELETE:- to delete item


@app.route('/items/<int:item_id>',methods=['DELETE'])
def delete_item(item_id):
    global items
    items = [item for item in items if item['id'] != 'item_id']
    return jsonify({"result": "Item deleted"})


if __name__ == "__main__":
    app.run(debug=True)
