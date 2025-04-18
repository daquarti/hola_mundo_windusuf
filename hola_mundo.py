from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hola mundo'

if __name__ == '__main__':
    # En desarrollo usa debug=True, en producción usa debug=False
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)), debug=False)
