import sys

from augumented_writer import augumented_writer


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


if __name__ == '__main__':
    saved = sys.stdout
    sys.stdout = augumented_writer(sys.stdout)

    print_hi('PyCharm')
