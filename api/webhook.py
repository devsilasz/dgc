from flask import Flask, request, jsonify

app = Flask(__name__)

# Configurações
API_KEY_TICTO = "9dba0303-6274-4c63-b3e3-1d69668e1c6b"

# Endpoint do Webhook
@app.route('/webhook', methods=['POST'])
def webhook():
    # Verifica a chave da API
    auth_header = request.headers.get("Authorization")
    if auth_header != API_KEY_TICTO:
        return jsonify({"error": "Unauthorized"}), 403

    data = request.json
    print(f"Evento recebido: {data}")

    # Processa os eventos relevantes
    user_id_discord = data.get("user_id")  # ID do Discord deve vir no payload
    event = data.get("status")
    plan = data.get("plan")  # "mensal" ou "anual"

    if not user_id_discord or not event:
        return jsonify({"error": "Invalid payload"}), 400

    # Apenas exibe o evento para teste (você conectará ao bot depois)
    print(f"User ID Discord: {user_id_discord}, Evento: {event}, Plano: {plan}")

    return jsonify({"status": "success"}), 200

# Exporta o app Flask
if __name__ == "__main__":
    app.run()
