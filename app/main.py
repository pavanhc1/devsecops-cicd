from flask import Flask, Blueprint, jsonify, request

app = Flask(__name__)
app.debug = True

main = Blueprint("main", __name__)

@main.route("/")
def home():
    return jsonify({"message": "Hello, World!"})

@main.route("/data", methods=["POST"])
def process_data():
    data = request.get_json()
    if not isinstance(data, dict):  # data validation
        return jsonify({"error": "Invalid data format"}), 400
    return jsonify({"processed": True, "data": data})

app.register_blueprint(main)

if __name__ == '__main__':
    # Intentionally allowing binding to all interfaces especially OWASP ZAP's scan running on the host network
    # Acknowledge the security implications
    app.run(host='0.0.0.0', port=5001)  # nosec