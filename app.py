from flask import Flask, render_template
import threading
import time
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# 🔄 Função de autopinger (executa a cada 5 minutos)
def auto_ping():
    while True:
        try:
            print("[AutoPing] Enviando ping para o app...")
            requests.get("https://mostravip.onrender.com")  # ⬅️ Substitua pelo seu domínio Render
        except Exception as e:
            print(f"[AutoPing] Erro ao pingar: {e}")
        time.sleep(300)  # 5 minutos = 300 segundos

if __name__ == '__main__':
    # Inicia a thread de autoping
    threading.Thread(target=auto_ping, daemon=True).start()
    # Inicia o servidor Flask
    app.run(host='0.0.0.0', port=10000)
