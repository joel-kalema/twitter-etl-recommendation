from flask import Flask
from routes import create_routes
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

create_routes(app)

if __name__ == '__main__':
    app.run(debug=True)
