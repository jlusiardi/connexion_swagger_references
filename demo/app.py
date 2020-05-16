import connexion
from flask_cors import CORS

app = connexion.App(__name__, specification_dir='swagger/')
CORS(app.app)

app.add_api('api.yaml')


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
