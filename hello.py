from flask import Flask, request, url_for, render_template, redirect, abort

from flask import session, escape


app = Flask(__name__)

@app.errorhandler(404)
def page_not_found(error):
  #return render_template('page_not_found.html'),404
  resp = make_response(render_template('page_not_found.html'), 404)
  resp.headers['Ola'] = 'Fucked'
  return resp

app.secret_key = b'123*&X^&()\n\x]/'
@app.route('/loggedin')
def loggedin():
  if username in session:
    return 'Logged in as %s' % escape(session['username']) 
  return 'You are not logged in'

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

@app.route('/logout')
def logout():
  session.pop('username', None)
  return redirect(url_for('index'))

@app.route('/')
def index():
  uname = request.cookies.get('username')
  if len(uname) == 0:
    return redirect(url_for('login'))
  return "index"

@app.route('/fukc')
def pubg():
  return "I know you, you little fuck"

@app.route('/user/<uname>')
def showuser(uname):
  return 'Hello %s' % uname

@app.route('/group/<groupname>')
def showgroup(groupname):
  return 'Welcome to our %s tribe :)' % groupname

@app.route('/event/<int:event_id>')
def showevent(event_id):
  return ' Event %d ' % event_id

@app.route('/event/<int:event_id>/<path:subpath>')
def showpath(event_id,subpath):
  return 'Subpath %s' % subpath

@app.route('/events/')
def events():
  return 'events page'

@app.route('/about')
def about():
  return 'We are the most awesomely travel motivated entrepreneus'

@app.route('/login', methods=['GET','POST'])
def login():
  error = None
  if request.method == 'POST':
    if valid_login(request.form['username'], request.fomr['password']):
      resp = make_response(render_template(...))
      resp.set_cookie('username', 'the username')
      return log_the_user_in(request.form['username'])
    else:
      abort(401)

  return render_template('login.html',error=error)

@app.route('/upload', methods=['GET','POST'])
def upload():
  error = None
  if request.method == 'POST':
    f = request.files['the_file']
    f.save('/var/www/uploads/filth.txt')


with app.test_request_context():
  print(url_for('index'))
  print(url_for('login'))
  print(url_for('login', next='/'))
  print(url_for('showuser', uname='Ass hole'))
