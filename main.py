from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs
import os
import socketserver
from pyxlsweb import PYXLSWEB

SESSION_STORAGE = {}
PUBLIC_DIR = os.path.abspath("./res")


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
 def do_GET(self):
  mses = SESSION_STORAGE
  self.send_response(200)
  parsed_url = urlparse(self.path)
  query_arguments = parse_qs(parsed_url.query)
  pfor = query_arguments.get("code",[""])[0]
  # Set the content type to plain text
  pge = query_arguments.get("page",["home"])
  fln = pge[0]
  self.send_header("Content-type", "text/html")
  self.end_headers()
  pi = PYXLSWEB(PUBLIC_DIR,self.headers.get("host"),fln,self.path,self.headers,query_arguments,mses)
  html_content = str(pi)
  self.wfile.write(html_content.encode('utf-8'))

socketserver.TCPServer.allow_reuse_address = True
server_address = ("127.0.0.1", 8000)

# Create and run the server
httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
print("Server running on http://localhost:8000...")
httpd.serve_forever()

