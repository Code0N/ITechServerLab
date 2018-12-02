from http.server import BaseHTTPRequestHandler, HTTPServer
from os import curdir, sep

from requests import HTTPError

PORT_NUMBER = 8080

class myHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path=='/':
            self.path="/index.html"
        try:
            sendReply = False
            if self.path.endswith(".html"):
                mimetype = 'text/html'
                sendReply = True
            if self.path.endswith(".jpg"):
                mimetype = 'image/jpg'
                sendReply = True
            if self.path.endswith(".gif"):
                mimetype = 'image/gif'
                sendReply = True
            if self.path.endswith(".js"):
                mimetype = 'application/javascript'
                sendReply = True
            if self.path.endswith(".css"):
                mimetype = 'text/css'
                sendReply = True

            if sendReply == True:
                self.send_response(200)
                self.send_header('Content-type', mimetype)
                self.end_headers()
                if mimetype == 'text/html' or mimetype == 'application/javascript' or mimetype == 'text/css':
                    f = open(curdir + sep + self.path)
                    self.wfile.write(bytes(f.read(), "utf-8"))
                else:
                    f = open(curdir + sep + self.path, 'rb')
                    self.wfile.write(f.read())
                f.close()
            return

        except IOError:
            self.send_error(404, 'File {} not found'.format(self.path))
        except ConnectionError:
            self.send_error(500)
        except HTTPError:
            self.send_error(406)
        except TimeoutError:
            self.send_error(504)


try:
    server = HTTPServer(('', PORT_NUMBER), myHandler)
    print("Server started at port {}".format(PORT_NUMBER))
    server.serve_forever()
except KeyboardInterrupt:
    print("User killed script")
    server.socket.close()