import http.server
import socketserver


class MyRequestHandler(http.server.SimpleHTTPRequestHandler):
    data = ""
    def do_GET(self):
        # Redirects to main page
        if self.path == '/':
            self.path = '/ChairMaker/index.html'
        # Redirects to product_info page
        elif (self.path.find("/ChairMaker/product_info.html") != -1):
            # Parse parameters
            split_by_q = self.path.split("?")
            param_str = split_by_q[1]
            key_value_pairs = param_str.split("&")
            # Check if the customer want a round or square table
            if (key_value_pairs[2].split("=")[0] == 'ttdiam'):
                p1 = key_value_pairs[0].split("=")
                p2 = key_value_pairs[1].split("=")
                p3 = key_value_pairs[2].split("=")
                pname = p1[1].replace("+", "_")
                theight = p2[1]
                ttdiam = p3[1]
                # Post table to fuseki
                print(pname)
                response = 1  # postRoundTable(pname, theight, ttdiam)
                # Check if fuseki posted successfully
                if (response == 200):
                    # Generate a DFA-file
                    # generateRoundTable(pname)
                    print("tull")
                else:
                    # Display the error page
                    self.path = '/ChairMaker/error.html'
            else:
                # Parse parameters
                p1 = key_value_pairs[0].split("=")
                p2 = key_value_pairs[1].split("=")
                p3 = key_value_pairs[2].split("=")
                p4 = key_value_pairs[3].split("=")
                pname = p1[1].replace("+", "_")
                theight = p2[1]
                ttlength = p3[1]
                ttwidth = p4[1]
                # Post table to fuseki
                # postSquareTable(pname, theight, ttlength, ttwidth)
                response = 1
                # Check if fuseki posted successfully
                if (response == 200):
                    # Generate a DFA-file
                    # generateSquareTable(pname)
                    print("rull")
                else:
                    # Display the error page
                    self.path = '/ChairMaker/error.html'

        return http.server.SimpleHTTPRequestHandler.do_GET(self)

    def do_POST(self):
        content_len = int(self.headers['Content-Length'])
        post_body = self.rfile.read(content_len)
        self.data = post_body
        print(post_body)
        return http.server.SimpleHTTPRequestHandler.do_GET(self)


Handler = MyRequestHandler
# Set server to localhost and port 8080
server = socketserver.TCPServer(('127.0.0.1', 8080), Handler)

try:
    server.serve_forever()
except KeyboardInterrupt:
    pass
server.server_close()
