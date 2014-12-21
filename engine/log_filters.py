# Main logs recognition algorithms
import re
import difflib
# Note: be carefull to keep a limit to opened files
# and change the file loading with a better method


class CacheDiffs(): # File shall be loaded from cache and then filtered
    def _init_(self):
        self.file_mame = False
        self.user_diff_list = {}
        self.differ = difflib.Differ()

    def register_user(self, user):
        self.user_diff_list[user] = {}

    def renew_user(self, user, file_name):
        self.user_diff_list[user][file_name] = []

    def load(self, file_name="mob.log"):
        if self.file_mame is not False:
            self.log_file.close()
        self.file_mame = file_name
        self.log_file = open(file_name, "r")

    def unload(self):
        self.log_file.close()



class LogFilters():
    def __init__(self, *patterns):
        self.patterns = patterns
        self.file_mame = False

    def filter_based_type(self, search_type="all"):
        """
        Tag logs by severity
        :return: Dictionary: {"info": [info_list], "error":[error_list], "warning":[warning_list]}
        """
        # self.load()
        if (search_type == u"all"):
            return self.show_all().split('\n')
        else:
            try:
                return re.findall(self.patterns[0][search_type]['root'], str(self.show_all()))
            except KeyError:
                return ["It seems you called for a nonexistent search type"]

    def filter_based_word(self, search_word):
        """
        Tag logs by timestamp can by found by using a certain string
        :return: Dictionary filled with timestamps found and equivalent logs
        """
        pattern = r"^(.*%s.*)$" % (search_word)
        return re.findall(pattern, str(self.show_all()), re.VERBOSE | re.MULTILINE)


    def show_all(self):
        return self.log_file.read()

    def load(self, file_name="mob.log"):
        if self.file_mame is not False:
            self.log_file.close()
        # Load log files and direct them into the corresponding method
        self.file_mame = file_name
        self.log_file = open(file_name, "r")

    def unload(self):
        self.log_file.close()
