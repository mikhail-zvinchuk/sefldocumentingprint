import inspect
import os
import sys


class writer:
    def __init__(self, writer):
        self.writer = writer

    def write(self, text):
        result = self_documenting_print()
        self.writer.write(text + result)

    # pass all other methods to __stdout__ so that we don't have to override them
    def __getattr__(self, name):
        atr = self.writer.__getattribute__(name)
        return atr


def self_documenting_print() -> str:
    previous_frame = inspect.currentframe().f_back.f_back
    info = inspect.getframeinfo(previous_frame)
    return " |=> "+info.function + ',' + str(info.lineno) + ',' + info.filename + os.linesep


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


if __name__ == '__main__':
    saved = sys.stdout
    sys.stdout = writer(sys.stdout)

    print_hi('PyCharm')



