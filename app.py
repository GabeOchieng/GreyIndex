import os.path
import tornado.ioloop
import tornado.web
import engine.patterns as patterns
from engine.log_filters import LogFilters, CacheDiffs
from pprint import pprint

cache_diffs = CacheDiffs(patterns.diff_regex)
log_filter = LogFilters(cache_diffs, patterns.log_search_patterns)

class LogHandler(tornado.web.RequestHandler):
    def get(self, arguments):
        self.arguments = dict(arg.split(":") for arg in arguments.split("/") if arg)
        pprint(self.arguments)
        #pprint(repr(self.request.remote_ip))
        if ("update" in self.arguments.keys()):
            if self.arguments['type'] == "type":
                results = log_filter.filter_based_type(self.arguments['file'], self.arguments['args'],
                                                       self.arguments['update'])
            elif self.arguments['type'] == "word":
                results = log_filter.filter_based_word(self.arguments['file'], self.arguments['args'],
                                                       self.arguments['update'])
        else:
            if self.arguments['type'] == "type":
                results = log_filter.filter_based_type(self.arguments['file'], self.arguments['args'])
            elif self.arguments['type'] == "word":
                results = log_filter.filter_based_word(self.arguments['file'], self.arguments['args'])
        # if (recognition_type == "timestamp"):
        #    self.write("%s" % (str(log_filter.filter_based_timestamp())))
        if ("update" in self.arguments.keys()):
            for result in results:
                self.write("<tr><td>"+result+"</td></tr>")
        else:
            self.render("log.html", logs=results, args=arguments)



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
    (r"/logs/(.+)", LogHandler)
    ],
    template_path=os.path.join(os.path.dirname(__file__), "templates"),
    static_path=os.path.join(os.path.dirname(__file__), "static"),
    )

if __name__ == "__main__":
    application.listen(8000)
    tornado.ioloop.IOLoop.instance().start()