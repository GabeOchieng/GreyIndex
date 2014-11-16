"""
    Main logs recognition algorithms

"""

class Recognition():
    def __init__(self):
        pass

    @staticmethod
    def recbyseverity():
        """
        Tag logs by severity
        :return: Dictionary: {"info": [info_list], "error":[error_list], "warning":[warning_list]}
        """

        severity_results = {"info": [], "warning": [], "error": []}

        with open("test.log") as f:
            # Usage of readlines() is mandatory here 'cause of it's garbage collecting policy
            content = f.readlines()
            for line in content:
                if "info" in line.lower():
                    severity_results["info"].append(line)
                elif "warning" in line.lower():
                    severity_results["warning"].append(line)
                elif "error" in line.lower():
                    severity_results["error"].append(line)

        print severity_results
        return severity_results


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


if __name__ == "__main__":
    Recognition.recbyseverity()