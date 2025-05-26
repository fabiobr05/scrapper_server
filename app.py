from flask import Flask, request, jsonify
from src.collect import buscar_google

app = Flask(__name__)

@app.route("/buscar", methods=["POST"])
def request_busca():
    data = request.get_json()

    if not data or "desc" not in data:
        return jsonify({"error": "JSON inválido. Envie {'desc': 'valor'}"}), 400

    try:
        resultado = buscar_google(data)
        return jsonify(resultado), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
