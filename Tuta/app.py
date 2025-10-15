from flask import Flask, request
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return "API funcionando!"

@app.route("/imprimir", methods=["POST"])
def imprimir():
    
    dados = request.json
    texto = dados.get("texto", "Pedido vazio")
    with open("pedido.txt", "w", encoding="mbcs") as f:
        f.write(texto)
    # Envia para impressora compartilhada
    os.system('copy pedido.txt "\\\\localhost\\KPOS_58 Printer"')
    return {"status": "impresso"}

if __name__ == "__main__":
    app.run(port=5001)

# Teste com o comando curl:
# curl -X POST http://localhost:5001/imprimir -H "Content-Type: application/json" -d "{\"texto\":\"teste\"}"



