import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
  """Configuration file for the Microblog application"""
  SECRET_KEY = os.environ.get('SECRECT_KEY') or 'CnG28isstillyoucome'
  SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
      'sqlite:///' + os.path.join(basedir, 'app.db')
  SQLALCHEMY_TRACK_MODIFICATIONS = False
