from flask import Flask

class ReverseProxied(object):
  def __init__(self, app):
      self.app = app
  def __call__(self, environ, start_response):
      script_name = environ.get('HTTP_X_SCRIPT_NAME', '')
      if script_name:
          environ['SCRIPT_NAME'] = script_name
          path_info = environ['PATH_INFO']
          if path_info.startswith(script_name):
              environ['PATH_INFO'] = path_info[len(script_name):]
      return self.app(environ, start_response)


app = Flask(__name__)
app.wsgi_app = ReverseProxied(app.wsgi_app)