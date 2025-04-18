from flask import Flask
from ddtrace import patch_all
import logging

# Patch all libraries and enable logging integration
patch_all(logging=True)

logger = logging.getLogger()
logger.setLevel(logging.INFO)

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
