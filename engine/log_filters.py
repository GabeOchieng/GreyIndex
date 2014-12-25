# Main logs recognition algorithms
import re
from pprint import pprint
# Note: be carefull to keep a limit to opened files
# and change the file loading with a better method


class CacheDiffs(): # File shall be loaded from cache and then filtered
    def __init__(self, diff_regex):
        self.diff_regex = diff_regex
        self.files_cache = {}
        self.file_diffs = {}

    def load(self, file_name):
        self.log_file = open(file_name, "r")
        file_contents = self.log_file.read()
        if not (file_name in self.files_cache.keys()):
            self.file_diffs[file_name] = ""
        else:
            self.file_diffs[file_name] = file_contents[len(self.files_cache[file_name]):]
        self.files_cache[file_name] = file_contents
        self.log_file.close()


class LogFilters():
    def __init__(self, diff_object, *patterns):
        self.cachediffs = diff_object
        self.patterns = patterns
        self.file_mame = False

    def filter_based_type(self,  file_name, search_type="all"):

        self.cachediffs.load(file_name)
        print self.cachediffs.files_cache[file_name][:50]
        if (search_type == u"all"):
            return self.cachediffs.files_cache[file_mame].split('\n')
        else:
            try:
                return re.findall(self.patterns[0][search_type]['root'], self.cachediffs.files_cache[file_name])
            except KeyError:
                return ["It seems you called for a nonexistent search type"]

    def filter_based_word(self, file_mame, search_word):
        self.cachediffs.load(file_name)
        pattern = r"^(.*%s.*)$" % (search_word)
        return re.findall(pattern, self.cachediffs.files_cache[file_mame], re.VERBOSE | re.MULTILINE)

