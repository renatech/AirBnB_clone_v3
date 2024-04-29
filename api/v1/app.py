from os import getenv

from flask import Flask, jsonify
from models import storage
from api.v1.views import app_views

app = Flask(__name__)

app.register_blueprint(app_views)


@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Not found"}), 404


def teardown(error=None):
    storage.close()


app.teardown_appcontext(teardown)

if __name__ == '__main__':
    host = getenv("HBNB_API_HOST", '0.0.0.0')
    port = int(getenv("HBNB_API_PORT", 5000))

    app.run(host=host, port=port, threaded=True)
