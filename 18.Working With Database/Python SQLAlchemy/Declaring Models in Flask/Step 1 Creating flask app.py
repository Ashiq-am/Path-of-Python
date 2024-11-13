app = Flask(__name__, instance_relative_config=True)
app.config.from_pyfile('config.py', silent=True)
app.config.from_mapping(SECRET_KEY='dev')
