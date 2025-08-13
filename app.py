from flask import Flask, render_template, jsonify
import os

app = Flask(__name__)

# Rota principal do quiz
@app.route('/')
def index():
    return render_template('index.html')

# Rota de autoping
@app.route('/autoping')
def autoping():
    domain = os.getenv('DOMAIN', 'seu-dominio-aqui.com')
    return jsonify({"status": "ok", "message": f"AUTOPING {domain}"})

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
