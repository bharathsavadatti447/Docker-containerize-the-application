import os
from http.server import SimpleHTTPRequestHandler, HTTPServer

port = int(os.getenv("PORT", 8000))
env = os.getenv("APP_ENV", "development")

class CustomHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            message = f"<h2>Hello from SimpleHTTPServer!</h2><p>Running in {env} mode on port {port}.</p>"
            self.wfile.write(message.encode('utf-8'))
        else:
            super().do_GET()

if __name__ == '__main__':
    server = HTTPServer(('0.0.0.0', port), CustomHandler)
    print(f"Server running on port {port} in {env} mode...")
    server.serve_forever()