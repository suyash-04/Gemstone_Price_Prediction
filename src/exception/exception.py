import sys
from types import ModuleType 
 
class customexception(Exception):
    def __init__(self, error_message, error_details: ModuleType):
        self.error_message = error_message
        _, _, exc_tb = error_details.exc_info()  # Get traceback object
        self.lineno = exc_tb.tb_lineno  # Line number where exception occurred
        self.file_name = exc_tb.tb_frame.f_code.co_filename  # File name where exception occurred

    def __str__(self):
        return "Error occurred in python script name [{0}] line number [{1}] error message [{2}]".format(
            self.file_name, self.lineno, str(self.error_message)
        )


if __name__ == "__main__":
    try:
        a = 1 / 0
    except Exception as e:
        raise customexception(e, sys)
