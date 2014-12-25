"""
    Listing all available patterns that are going to be
    used in the logs recognition algorithms.
"""
import re

diff_regex = re.compile(r'\+ (.+)')

log_search_patterns = {
    'info' : {
        'root': re.compile(r'INFO:root:(.+)', re.VERBOSE | re.MULTILINE),
        'os': re.compile(r'INFO:root:os:(.+)', re.VERBOSE | re.MULTILINE),
        'limit': re.compile(r'INFO:root:limit:(.+)', re.VERBOSE | re.MULTILINE),
        'webcontext': re.compile(r'INFO:root:web context:(.+)', re.VERBOSE | re.MULTILINE),
        'tornado.access': re.compile(r'INFO:tornado\.access:(.+)', re.VERBOSE | re.MULTILINE)
    },
    'warning' : {
        'root': re.compile(r'WARNING:root:(.+)', re.VERBOSE | re.MULTILINE),
        # TODO Improve Warnings to include tracebacks
    }
}

argument_search_patters = {

}