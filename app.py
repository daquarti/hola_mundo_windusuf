from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello_world():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Mensaje para Gus</title>
        <style>
            body {
                background: linear-gradient(135deg, #1a1c20 0%, #2d3436 100%);
                height: 100vh;
                margin: 0;
                display: flex;
                justify-content: center;
                align-items: center;
                font-family: Arial, sans-serif;
            }
            .message {
                background: rgba(255, 255, 255, 0.1);
                padding: 2rem;
                border-radius: 15px;
                box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
                backdrop-filter: blur(4px);
                text-align: center;
            }
            h1 {
                color: #00ff88;
                font-size: 2.5em;
                margin-bottom: 0.5em;
                text-shadow: 2px 2px 4px rgba(0,0,0,0.5);
            }
            p {
                color: #fff;
                font-size: 1.8em;
                margin: 0;
                text-shadow: 1px 1px 2px rgba(0,0,0,0.5);
            }
        </style>
    </head>
    <body>
        <div class="message">
            <h1>¡Gus Capo!</h1>
            <p>✨ Viva los Agentes ✨</p>
        </div>
    </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)), debug=False)
