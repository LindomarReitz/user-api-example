from bottle import get, request, run, response
import json

with open('fixtures/users.json') as f:
    data = json.load(f)

@get("/users")
def users():
    return dict(users=data)

@get("/users/<username>")
def hello(username):
    for user in data:
        if username in user['username']:
            return user

    response.status = 404
    response.content_type = 'application/json'
    return json.dumps({'error': 'User {username} not found!'.format(username=username)})
    
run(reloader=True, host='0.0.0.0', port=8081)