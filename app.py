from flask import Flask, render_template, jsonify, request
import os
import threading
import time
import requests

app = Flask(__name__)

# Pega variáveis do Render
DOMAIN = os.getenv('DOMAIN', 'seu-dominio-aqui.com')
TOKEN = os.getenv('TOKEN_AUTOPING', 'token-padrao')

# Rota principal do quiz
@app.route('/')
def index():
    return render_template('index.html')

# Rota de autoping
@app.route('/autoping')
def autoping_route():
    token = request.args.get("token")
    if token != TOKEN:
        return jsonify({"status": "error", "message": "Token inválido"}), 401
    return jsonify({"status": "ok", "message": f"AUTOPING {DOMAIN}"}), 200

# Função para enviar ping automaticamente a cada 10 minutos
def autoping_thread():
    while True:
        try:
            url = f"https://{DOMAIN}/autoping?token={TOKEN}"
            response = requests.get(url)
            print(f"[AUTOPING] Status: {response.status_code}, Mensagem: {response.json()}")
        except Exception as e:
            print(f"[AUTOPING] Erro ao enviar ping: {e}")
        time.sleep(10 * 60)  # 10 minutos

# Inicia a thread de autoping
threading.Thread(target=autoping_thread, daemon=True).start()

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
