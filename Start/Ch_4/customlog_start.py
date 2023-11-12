# Demonstrate how to customize logging output

import logging

# TODO: add another function to log from
def another_function():
    logging.debug("This is a debug level log message", extra=extdata)
    #logging.info("This is a info level log message without extra data") #doesn't work; all log lines need same format apparently


# set the output file and debug level, and
# TODO: use a custom formatting specification
fmtstr = "User: %(user)s %(asctime)s: %(levelname)s: %(funcName)s Line:%(lineno)d %(message)s"
datestr = "%m/%d/%Y %I:%M:%S %p"
extdata = {"user": "joemarini@example.com"}

logging.basicConfig(filename="output.log",
                    level=logging.DEBUG,
                    format=fmtstr,
                    datefmt=datestr)

logging.info("This is an info-level log message",extra=extdata)
logging.warning("This is a warning-level message", extra=extdata)

another_function()