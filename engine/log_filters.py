# Main logs recognition algorithms


class LogFilters():
    def __init__(self):
        self.types = ["info", "error", "warning"]

    def filter_based_type(self, search_type="all"):
        """
        Tag logs by severity
        :return: Dictionary: {"info": [info_list], "error":[error_list], "warning":[warning_list]}
        """
        self.load()
        self.results = {}
        if (search_type == "all"):
            for type in self.types:
                self.results[type] = []
        else:
            self.results[search_type] = []

        content = self.log_file.readlines()
        if (search_type == "all"):
            for line in content:
                if "info" in line.lower():
                    self.results["info"].append(line)
                elif "warning" in line.lower():
                    self.results["warning"].append(line)
                elif "error" in line.lower():
                    self.results["error"].append(line)
        else:
            for line in content:
                if search_type in line.lower():
                    self.results[search_type].append(line)

        print self.results
        return self.results


    def filter_based_timestamp(self):
        """
        Tag logs by timestamp
        :return: Dictionary filled with timestamps found and equivalent logs
        """
        self.load()

    def load(self, file_name="test.log"):
        # Load log files and direct them into the corresponding method
        self.file_mame = file_name
        self.log_file = open(file_name, "r")

if __name__ == "__main__":
    Recognition.recbyseverity()