import tornado.ioloop
import tornado.web

data = []

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html", data=data)

class AddHandler(tornado.web.RequestHandler):
    def post(self):
        student = {
            "name": self.get_argument("name"),
            "roll": self.get_argument("roll"),
            "subject": self.get_argument("subject"),
            "percentage": self.get_argument("percentage")
        }
        data.append(student)
        self.redirect("/")

class DeleteHandler(tornado.web.RequestHandler):
    def get(self, index):
        data.pop(int(index))
        self.redirect("/")

class UpdateHandler(tornado.web.RequestHandler):
    def get(self, index):
        self.render("edit.html", index=index, student=data[int(index)])

    def post(self, index):
        data[int(index)] = {
            "name": self.get_argument("name"),
            "roll": self.get_argument("roll"),
            "subject": self.get_argument("subject"),
            "percentage": self.get_argument("percentage")
        }
        self.redirect("/")

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/add", AddHandler),
        (r"/delete/(.*)", DeleteHandler),
        (r"/update/(.*)", UpdateHandler),
    ], template_path="templates")

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()