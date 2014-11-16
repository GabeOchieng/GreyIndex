"""
    Main logs recognition algorithms

"""

class Recognition():
    def __init__(self):
        pass

    def recbyseverity(self):
        """
        Tag logs by severity
        :return: Dictionary: {"info": [info_list], "error":[error_list], "warning":[warning_list]}
        """
        pass

    def recbytimestamp(self):
        """
        Tag logs by timestamp
        :return: Dictionary filled with timestamps found and equivalent logs
        """
        pass

    def load(self):
        """
        Load log files and direct them into the corresponding method
        :return:
        """