from flask import Flask, request, jsonify

app = Flask(__name__)

MY_SECRET_KEY = "my_secret_12345"

@app.route('/like')
def handle_like():
    client_key = request.args.get('key')
    uid = request.args.get('uid')
    token = request.args.get('token')
    
    if client_key != MY_SECRET_KEY:
        return jsonify({"error": "Invalid or missing API key", "status": 3}), 403
        
    return jsonify({
        "status": "success", 
        "message": f"Successfully sent like to UID: {uid}"
    })
    
