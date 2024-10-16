from datetime import datetime
import json
from http.server import SimpleHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs, urlparse
from Model import Model
from field import *
from Database import Database

Model.db = Database('database.sqlite')
Model.connection = Model.db.connect()

Port = 8000

class Post(Model):
    title = CharField()
    body = TextField()
    #something wrong in text two lines
    #understood
    created_at = DateTimeField()
    published = BooleanField()

class User(Model):
    first_name = CharField()
    last_name = CharField(max_length=225)
    age = IntegerField()


#if __name__ == '__main__':
#    print(Post.get(1))


if __name__ == '__main__':
    class MyHandler(SimpleHTTPRequestHandler):
        def do_GET(self):
            if self.path == '/':
                return SimpleHTTPRequestHandler.do_GET(self)
            
            elif self.path == '/posts':
                self.send_response(200)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps(Post.all()).encode('utf-8'))
            else:
                post_id = int(self.path.split('/')[-1])
                result = Post.get(post_id)
                if result is False:
                    self.send_response(404)
                    self.wfile.write(b'Not Found')
                    return
                self.send_response(200)
                self.send_header('Content-type', 'apllication/json')
                self.end_headers()
                self.wfile.write(json.dumps(Post.get(post_id)).encode('utf-8'))

        def do_Post(self):
            length = int(self.headers.get('Content-lenght'))
            body = self.rfile.read(length)
            string = urlparse(body)
            post = parse_qs(string.path.decode('utf-8'))
            Post.create(title=post['title'[0]], body=post['body'[0]], create_at=datetime.now(), published=False)
            self.send_response(301)
            self.send_header('Location', 'localhost:8000')
            self.end_headers()




        # def do_POST(self):
        #     length = int(self.headers.get('Content-length'))
        #     body = self.rfile.read(length)
        #     string = urlparse(body)
        #     post = parse_qs(string.path.decode('utf-8'))
        #     Post.create(title=post['title'][0], body=post['body'][0], created_at=datetime.now(), pulished=False)
        #     self.send_response(301)
        #     self.send_header('Location', 'localhost: 8000')
        #     self.end_headers()


                
    with HTTPServer(("", Port), MyHandler) as httpd:
        print("Serving at port", Port)
        httpd.serve_forever()