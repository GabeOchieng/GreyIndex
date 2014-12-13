import tornado.ioloop
import tornado.web
import engine.patterns as patterns
from engine.log_filters import LogFilters
from engine.engine_web_interactions import *

log_filter = LogFilters()


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("GreyIndex")

class LogHandler(tornado.web.RequestHandler):
    def get(self, recognition_type="type", recognition_arguments="all"):
        self.write("Log Dumps about: %s %s<br>" % (recognition_type, recognition_arguments))

        if (recognition_type == "timestamp"):
            self.write("%s" % (str(log_filter.filter_based_timestamp())))
        else:
            self.write("%s" % (replace_newlines(str(log_filter.filter_based_type(recognition_arguments)))))


application = tornado.web.Application([
    (r"/", MainHandler),
    (r"/logs", LogHandler),
    (r"/logs/([a-zA-Z]+)/([a-zA-Z]+)", LogHandler),
])

if __name__ == "__main__":
    application.listen(8000)
    tornado.ioloop.IOLoop.instance().start()