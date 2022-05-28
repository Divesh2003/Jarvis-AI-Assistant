import os

from jarvis._version import __version__


class OutputStyler:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    CYAN = '\033[36m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


user_input = OutputStyler.CYAN + ':-$ ' + OutputStyler.ENDC

DASH = '='


def headerize(text=DASH):
    """
    Add dashes based on terminal length.

    Example:
    ---------------------------------------------------
    text   -->                  Result
    ---------------------------------------------------

    SYSTEM --> ================ SYSTEM ================
    None   --> ========================================

    """

    process = os.popen('stty size', 'r')
    result = process.read()
    process.close()
    terminal_height, terminal_length = result.split()
    if text:
        text_length = len(text)
        remaining_places = int(terminal_length) - text_length
        if remaining_places > 0:
            return DASH * (remaining_places // 2 - 1) + ' ' + text + ' ' + DASH * (remaining_places // 2 - 1)
    else:
        # If there is no text, it returns a line with the length of terminal.
        return DASH * int(terminal_length)


def print_console_header(text=DASH):
    """
    Create a dynamic header based on terminal length.
    """
    print(headerize(text))


jarvis_logo = "\n" \
              "      ██╗ █████╗ ██████╗ ██╗   ██╗██╗███████╗\n" \
              "      ██║██╔══██╗██╔══██╗██║   ██║██║██╔════╝\n" \
              "      ██║███████║██████╔╝██║   ██║██║███████╗\n" \
              " ██   ██║██╔══██║██╔══██╗╚██╗ ██╔╝██║╚════██║\n" \
              " ╚█████╔╝██║  ██║██║  ██║ ╚████╔╝ ██║███████║\n" \
              "  ╚════╝ ╚═╝  ╚═╝╚═╝  ╚═╝  ╚═══╝  ╚═╝╚══════╝\n"
start_text =" -  Voice Assistant Platform (Sample) " + "v" +  __version__ + "  -"  +"\n    - Build by Divesh and Ankita -"
