import tornado.ioloop
import tornado.web
import engine.patterns as patterns
from engine.log_filters import LogFilters
from engine.engine_web_interactions import *

log_filter = LogFilters(patterns.log_search_patterns)


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("GreyIndex")

class LogHandler(tornado.web.RequestHandler):
    def get(self, *arguments): # TODO Unpack arguments
        self.write("Log Dumps about: %s <br>" % (str(arguments)))

        # if (recognition_type == "timestamp"):
        #    self.write("%s" % (str(log_filter.filter_based_timestamp())))
        # else:
        for result in log_filter.filter_based_type('info'):
            self.write("%s<br>" % (str(result)))


application = tornado.web.Application([
    (r"/", MainHandler),
    (r"/logs", LogHandler),
    (r"/logs/(([a-zA-Z]+)/?)+", LogHandler),
])

if __name__ == "__main__":
    application.listen(8000)
    tornado.ioloop.IOLoop.instance().start()