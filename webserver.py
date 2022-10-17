from http.server import HTTPServer, BaseHTTPRequestHandler


#the work of the server being done
class helloHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('content-type', 'text/html')
        self.end_headers()

        self.wfile.write('Hello World'.encode())


#echo version to have words show in web window name
class echoHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('content-type', 'text/html')
        self.end_headers()

        self.wfile.write(self.path[1:].encode())


#running the server
def main():
    PORT = 7000
    server = HTTPServer(('', PORT), helloHandler)
    #echo version
    #server = HTTPServer(('', PORT), echoHandler)
    print('server is running on port %s' % PORT)
    server.serve_forever()


#from command/terminal to make sure it runs main
if __name__ == '__main__':
    main()