import http.server
from py.generateDFA import generateDiningChair, generateStoolChair, generateModernChair
from py.fusekiposter import postDiningChair, postModernChair, postStoolChair
import socketserver

IP_NUMBER = '127.0.0.1'
PORT_NUMBER = 8080


class MyRequestHandler(http.server.SimpleHTTPRequestHandler):

    def do_GET(self):
        # Redirects to main page
        if self.path == '/':
            self.path = '/ChairMaker/index.html'
        # Response to order.html http request
        elif self.path.find('/info') != -1:
            # Get chair name from url param
            split_by_q = self.path.split("?")
            param_str = split_by_q[1]

            parameters = param_str.split("&")
            pname = parameters[0]
            chairType = parameters[1]

            data = ""

            if (chairType == "diningChair"):
                data = generateDiningChair(pname)
            elif (chairType == "stoolChair"):
                data = generateStoolChair(pname)
            elif (chairType == "modernChair"):
                data = generateModernChair(pname)

            self.send_response(200)
            self.send_header("Content-type", "text/plain; charset=utf-8")
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()

            self.wfile.write(bytes(data, "utf-8"))
            return None
        return http.server.SimpleHTTPRequestHandler.do_GET(self)

    def do_POST(self):
        content_len = int(self.headers['Content-Length'])
        post_body = self.rfile.read(content_len)
        self.path = '/ChairMaker/order.html?test'

        post_string = post_body.decode('utf-8')
        parameters = post_string.split("&")
        chairType = parameters[0].split("=")[0]

        if (chairType == "dCName"):
            # DINING
            pname = parameters[0].split("=")[1]
            width = parameters[3].split("=")[1]
            length = parameters[2].split("=")[1]
            height = parameters[1].split("=")[1]

            response = postDiningChair(pname, float(
                width), float(length), float(height))

        elif (chairType == "sCName"):
            # STOOL
            print(parameters)
            pname = parameters[0].split("=")[1]
            diameter = parameters[2].split("=")[1]
            height = parameters[1].split("=")[1]

            response = postStoolChair(pname, float(diameter), float(height))
        elif (chairType == "mCName"):
            # MODERN
            pname = parameters[0].split("=")[1]
            width = parameters[3].split("=")[1]
            length = parameters[2].split("=")[1]
            height = parameters[1].split("=")[1]

            response = postModernChair(pname, float(
                width), float(length), float(height))

        return http.server.SimpleHTTPRequestHandler.do_GET(self)


Handler = MyRequestHandler
# Set server to localhost and port 8080
server = socketserver.TCPServer((IP_NUMBER, PORT_NUMBER), Handler)

try:
    server.serve_forever()
except KeyboardInterrupt:
    pass
server.server_close()
