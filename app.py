import tornado.ioloop
import tornado.web

from engine.recognition import Recognition

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("GreyIndex")

class LogHandler(tornado.web.RequestHandler):
    def get(self, recognition_type="severity", recognition_arguments="error"):
        self.write("Log Dumps about: %s %s<br>" % (recognition_type, recognition_arguments))
        self.write("%s" % (str(Recognition.recbyseverity())))


application = tornado.web.Application([
    (r"/", MainHandler),
    (r"/logs", LogHandler),
    (r"/logs/([a-zA-Z]+)/([a-zA-Z]+)", LogHandler),
])

if __name__ == "__main__":
    application.listen(8000)
    tornado.ioloop.IOLoop.instance().start()