from flask import Flask, jsonify, request

app = Flask(__name__)

users = {}

@app.route('/users/<int:user_id>', methods = ['GET'])
def get_user(user_id):
    """Returns user info by ID"""
    user = users.get(user_id)
    if user:
        return jsonify({'id': user_id, 'name': user}), 200
    return jsonify({'error': "User not found"}), 404

@app.route('/users', methods = ['POST'])
def add_user():
    '''Add a new User'''
    data = request.json
    users_id = data.get('id')
    name = data.get('name')

    if not users_id or not name:
        return jsonify({'error': 'invalid data'}), 400
    
    if users_id in users:
        return jsonify({'error': "User_id already exists"}), 400
    
    users[users_id] = name
    return jsonify({'id': users_id, 'name': name}), 201