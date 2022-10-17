from http.server import  HTTPServer, BaseHTTPRequestHandler


class Serving( BaseHTTPRequestHandler):
    def do_GET(self):
        #set starting page
        if self.path == '/':
            self.path = '/index.html'
        try:
            #open file user typed
            file_to_open = open( self.path[1:]).read()
            self.send_response(200)
        except:
            file_to_open = 'File Not Found'
            self.send_response(404)
            
        self.end_headers()
        self.wfile.write( bytes( file_to_open, 'utf-8'))


httpd = HTTPServer(('localhost', 7000), Serving)
httpd.serve_forever()