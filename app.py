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
            button {
                margin-top: 2rem;
                padding: 1rem 2rem;
                font-size: 1.2em;
                background: #00ff88;
                border: none;
                border-radius: 8px;
                color: #1a1c20;
                cursor: pointer;
                transition: transform 0.2s, box-shadow 0.2s;
            }
            button:hover {
                transform: translateY(-2px);
                box-shadow: 0 5px 15px rgba(0,255,136,0.4);
            }
            #windsurf-message {
                margin-top: 1rem;
                color: #00ff88;
                font-size: 1.2em;
                opacity: 0;
                transition: opacity 0.5s;
            }
            #windsurf-message.show {
                opacity: 1;
            }
        </style>
    </head>
    <body>
        <div class="message">
            <h1>Cartas a Lucilio</h1>
            <p>✨ "La filosofía no es un espectáculo público ni se presta a la ostentación" ✨</p>
            <p style="font-size: 1em; margin-top: 0.5em; color: #888;">- Séneca</p>
            <button onclick="showWindsurfMessage()">Click aquí</button>
            <p id="windsurf-message">Realizado con Windsurf 🏄‍♂️</p>
        </div>
        <script>
            function showWindsurfMessage() {
                const message = document.getElementById('windsurf-message');
                message.classList.add('show');
            }
        </script>
    </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)), debug=False)
