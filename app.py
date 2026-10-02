from http.server import BaseHTTPRequestHandler, HTTPServer

count = 0

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        global count

        if self.path == "/":
            count += 1
            body = f"""<!DOCTYPE html>
<html>
<head>
<style>
body {{
    margin: 0;
    height: 100vh;
    display: flex;
    align-items: center;
    justify-content: center;
    font-family: "Comic Sans MS", cursive;
}}
.title {{
    font-size: 40px;
}}
.counter {{
    position: fixed;
    top: 20px;
    right: 25px;
    font-size: 20px;
    font-weight: bold;
    padding: 10px 16px;
    border: 2px solid #333;
    border-radius: 8px;
}}
</style>
</head>
<body>
<div class="title">1st deployment</div>
<div class="counter">Refresh Count: {count}</div>
</body>
</html>"""
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.send_header("Content-Length", str(len(body.encode())))
            self.end_headers()
            self.wfile.write(body.encode())
        elif self.path == "/favicon.ico":
            self.send_response(204)
            self.end_headers()
        else:
            self.send_response(404)
            self.end_headers()

HTTPServer(("0.0.0.0", 8000), Handler).serve_forever()
