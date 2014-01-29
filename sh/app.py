from flask import Flask, render_template, got_request_exception

app = Flask(__name__, static_url_path='', static_folder='../',
            template_folder='../')

@app.route('/')
def index():
  return render_template('index.html')

@got_request_exception.connect_via(app)
def log_exceptions(sender, exception, **extra):
  print(exception)
