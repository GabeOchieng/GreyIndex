import os.path
import tornado.ioloop
import tornado.web
import engine.patterns as patterns
from engine.log_filters import LogFilters

log_filter = LogFilters(patterns.log_search_patterns)

class LogHandler(tornado.web.RequestHandler):
    def get(self, *arguments):
        self.arguments = list(arguments)

        log_filter.load(self.arguments[0])
        if self.arguments[1] == "type":
            results = log_filter.filter_based_type(self.arguments[2])
        elif self.arguments[1] == "word":
            results = log_filter.filter_based_word(self.arguments[2])
        # if (recognition_type == "timestamp"):
        #    self.write("%s" % (str(log_filter.filter_based_timestamp())))
        self.render("log.html", logs=reversed(results))



class ErrorHandler(tornado.web.RequestHandler):
    @staticmethod
    def raise_404(self, *args, **kwargs):
        tornado.web.RequestHandler.write_error(404,message="this is a custom 404 error message")
    @staticmethod
    def raise_403(self, *args, **kwargs):
        tornado.web.RequestHandler.write_error(403,message="this is a custom 403 error message")
    @staticmethod
    def raise_500(self, *args, **kwargs):
        tornado.web.RequestHandler.write_error(500,message="this is a custom 500 error message")

application = tornado.web.Application(
    [
    (r"/", LogHandler),
    (r"/logs", LogHandler),
    (r"/logs/file:([a-zA-Z0-9]+\.[a-zA-Z]+)/type:([a-zA-Z0-9]+)/args:([a-zA-Z0-9]+)", LogHandler)
    ],
    template_path=os.path.join(os.path.dirname(__file__), "templates"),
    static_path=os.path.join(os.path.dirname(__file__), "static"),
    )

if __name__ == "__main__":
    application.listen(8000)
    tornado.ioloop.IOLoop.instance().start()