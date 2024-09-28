# Hello world
import flask in Flask

app = Flask(__name__)

@app.route('/')
def root_route():
  return '''
  <h1>Web Flask App</h1>
  <p>Hello from github Flask repsository</p>
  <p>Deploy in Azure via ???</p>
  <p>Deploy in Google via:</p>
  '''
