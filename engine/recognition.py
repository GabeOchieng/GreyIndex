"""
    Main logs recognition algorithms

"""

class Recognition():
    def __init__(self):
        pass

    @staticmethod
    def recbyseverity(self):
        """
        Tag logs by severity
        :return: Dictionary: {"info": [info_list], "error":[error_list], "warning":[warning_list]}
        """

        info_list = []
        warning_list = []
        error_list = []

        with open("test.log") as f:
            # Usage of readlines() is mandatory here 'cause of it's garbage collecting policy
            content = f.readlines()
            for line in content:
                if "info" in line.lower():
                    info_list.append(line)
                elif "warning" in line.lower():
                    warning_list.append(line)
                elif "error" in line.lower():
                    error_list.append(line)


    @staticmethod
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