import http.server
import json
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
        elif self.path.find('/chairConstraints') != -1:

            dChairL = generateDiningChair("dCConstL", False)
            dChairU = generateDiningChair("dCConstU", False)

            sChairL = generateStoolChair("sCConstL", False)
            sChairU = generateStoolChair("sCConstU", False)

            mChairL = generateModernChair("mCConstL", False)
            mChairU = generateModernChair("mCConstU", False)

            x = f'{{\"dCConstL\" : {dChairL}, \"dCConstU\" : {dChairU}, \"sCConstL\" : {sChairL}, \"sCConstU\" : {sChairU}, \"mCConstL\" : {mChairL}, \"mCConstU\" : {mChairU}}}'

            self.send_response(200)
            self.send_header("Content-type", "text/plain; charset=utf-8")
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(bytes(x, "utf-8"))
            return None

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
                data = generateDiningChair(pname, True)
            elif (chairType == "stoolChair"):
                data = generateStoolChair(pname, True)
            elif (chairType == "modernChair"):
                data = generateModernChair(pname, True)

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

        post_string = post_body.decode('utf-8')
        parameters = post_string.split("&")
        chairType = parameters[0].split("=")[0]

        if (chairType == "dCConst"):
            # DINING LOWER CONSTRAINT
            width = parameters[5].split("=")[1]
            length = parameters[3].split("=")[1]
            height = parameters[1].split("=")[1]

            response = postDiningChair("dCConstL", float(
                width), float(length), float(height))

            # DINING UPPER CONSTRAINT
            width = parameters[6].split("=")[1]
            length = parameters[4].split("=")[1]
            height = parameters[2].split("=")[1]

            response = postDiningChair("dCConstU", float(
                width), float(length), float(height))

        elif (chairType == "sCConst"):
            # STOOL LOWER CONSTRAINT
            diameter = parameters[3].split("=")[1]
            height = parameters[1].split("=")[1]

            response = postStoolChair(
                "sCConstL", float(diameter), float(height))

            # STOOL UPPER CONSTRAINT
            diameter = parameters[4].split("=")[1]
            height = parameters[2].split("=")[1]

            response = postStoolChair(
                "sCConstU", float(diameter), float(height))

        elif (chairType == "mCConst"):
            # MODERN LOWER CONSTRAINT
            width = parameters[5].split("=")[1]
            length = parameters[3].split("=")[1]
            height = parameters[1].split("=")[1]

            response = postModernChair("mCConstL", float(
                width), float(length), float(height))

            # MODERN UPPER CONSTRAINT
            width = parameters[6].split("=")[1]
            length = parameters[4].split("=")[1]
            height = parameters[2].split("=")[1]

            response = postModernChair("mCConstU", float(
                width), float(length), float(height))

        elif (chairType == "dCName"):
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
