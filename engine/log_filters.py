# Main logs recognition algorithms
import re

class LogFilters():
    def __init__(self, *patterns):
        self.types = ["info", "error", "warning"]
        self.patterns = patterns


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
        return re.findall(self.patterns[0][search_type]['root'], str(self.show_all()))



    def show_all(self):
        return self.log_file.read()

    def load(self, file_name="mob.log"):
        # Load log files and direct them into the corresponding method
        self.file_mame = file_name
        self.log_file = open(file_name, "r")

    def unload(self):
        self.log_file.close()
