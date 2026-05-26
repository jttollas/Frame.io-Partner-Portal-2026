import os, http.server, socketserver

PROJECT_DIR = '/Users/jtollas/Library/CloudStorage/OneDrive-Adobe/Work/Coding/frameio-dev-portal'
os.chdir(PROJECT_DIR)

PORT = int(os.environ.get('PORT', 8081))
Handler = http.server.SimpleHTTPRequestHandler
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Serving {PROJECT_DIR} at http://localhost:{PORT}")
    httpd.serve_forever()
