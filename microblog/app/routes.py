from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
  user = {'username':'Samiksha'}
  posts = [ { 'author':{'username': 'Sampath'}, 'body':' I am going to be a great friend' }, 
            { 'author':{'username': 'Kiran'}, 'body': 'I need to the asshole' },
            { 'author':{'username': 'Pavan'}, 'body': 'I dont need to be here.'}
          ]
  return render_template('index.html',title='Home',user=user, posts=posts)
