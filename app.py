from http.server import BaseHTTPRequestHandler
from urllib.parse import parse_qs, urlparse
import json

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed_path = urlparse(self.path)
        query_params = parse_qs(parsed_path.query)
        
        client_key = query_params.get('key', [None])[0]
        uid = query_params.get('uid', [None])[0]
        token = query_params.get('token', [None])[0]
        
        MY_SECRET_KEY = "my_secret_12345"
        
        if client_key != MY_SECRET_KEY:
            self.send_response(403)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({"error": "Invalid or missing API key", "status": 3}).encode())
            return
            
        response_data = {
            "status": "success",
            "message": f"Successfully sent like to UID: {uid}"
        }
        
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(response_data).encode())
        return
        
