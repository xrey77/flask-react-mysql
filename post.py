from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

# pip install flask_marshmallow
# pip install flask_sqlalchemy

app = Flask(__name__)
app.config['SLQALCHEMY_DATABASE_URI'] = 'mysql://rey:rey@127.0.0.1/flask_react_mysql'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
ma = Marshmallow(app)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.string(100))
    description = db.Column(db.String(100))
    
    def __init__(self, title, description):
        self.title = title
        self.description = description

class PostSchema(ma.Schema):
    class Meta:
        fields = ("title","description")

post_schema = PostSchema()              #single record
posts_schema = PostSchema(many=True)    #all records

@app.route('/post', methods = ['POST'])
def add_post():
    title = request.json('title')
    description = request.json('description')
    
    my_post = Post(title, description)
    db.session.add(my_post)
    db.session.commit()
    return post_schema.jsonify(my_post)

@app.route('/getallpost', methods = ['GET'])
def get_post():
    all_post = Post.query.all()
    result = post_schema.dump(all_post)
    return post_schema.jsonify(result)

@app.route('/getpostid/<id>', methods = ['GET'])
def get_postid(id):
    post = Post.query.get(id)
    return post

@app.route('/updatepost/<id>', methods = ['PUT'])
def update_post(id):
    post = Post.query.get(id)
    title = request.json('title')
    description = request.json('description')
    post.title = title
    post.description = description
    db.session.commit()        
    return post_schema.jsonify(post)

@app.route('/deletepost/<id>', methods = ['DELETE'])
def delete_postid(id):
    post = Post.query.get(id)
    db.session.delete(post)
    db.session.commit()    
    return post_schema.jsonify(post)
