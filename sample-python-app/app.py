from flask import Flask
from ddtrace import tracer, patch_all

# Automatically patch supported libraries (Flask in this case)


patch_all()
ddtrace_logging_patch()

logger = logging.getLogger()
logger.setLevel(logging.INFO)

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
