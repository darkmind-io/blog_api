#!flask/bin/python
from flask import Flask, jsonify, abort, make_response, request

app = Flask(__name__)

posts = [
    {
        'id': 1,
        'title': u'Getting Google AppEngine',
        'description': u'You have to use this',
    },
    {
        'id': 2,
        'title': u'CSIS 604',
        'description': u'This is the best class ever',
    }
]

@app.route('/blog/api/posts', methods=['GET'])
def get_posts():
    return jsonify({'posts': posts})

@app.route('/blog/api/posts/<int:post_id>', methods=['GET'])
def get_post(post_id):
    post = [post for post in posts if post['id'] == post_id]
    if len(post) == 0:
        abort(404)
    return jsonify({'post': post[0]})

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

@app.route('/blog/api/posts', methods=['POST'])
def create_post():
    if not (request.json and 'title' in request.json):
        abort(400)
    post = {
        'id': posts[-1]['id'] + 1,
        'title': request.json['title'],
        'description': request.json.get('description', "")
    }
    posts.append(post)
    return jsonify({'post': post}), 201

@app.route('/blog/api/posts/<int:post_id>', methods=['PUT'])
def update_post(post_id):
    post = [post for post in posts if post['id'] == post_id]
    if len(post) == 0:
        abort(404)
    if not request.json:
        abort(400)
    if 'title' in request.json and type(request.json['title']) != unicode:
        abort(400)
    if 'description' in request.json and type(request.json['description']) is not unicode:
        abort(400)
    post[0]['title'] = request.json.get('title', post[0]['title'])
    post[0]['description'] = request.json.get('description', post[0]['description'])
    return jsonify({'post': post[0]})

@app.route('/blog/api/posts/<int:post_id>', methods=['DELETE'])
def delete_post(post_id):
    post = [post for post in posts if post['id'] == post_id]
    if len(post) == 0:
        abort(404)
    posts.remove(post[0])
    return jsonify({'result': True})

if __name__ == '__main__':
    app.run(debug=True)
