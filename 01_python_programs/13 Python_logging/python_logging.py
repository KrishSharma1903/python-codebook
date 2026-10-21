# Python Logging
'''Logging is a crucial aspect of any application, providing a way to track events, errors, and operational information. 
Python's built-in logging module offers a flexible framework for emitting log messages from Python programs.'''

# import logging

# #configure the basics logging settings 
# logging.basicConfig(level=logging.DEBUG)

# ## log messages with different sevierity levels
# logging.debug("This is a debug message")
# logging.info("This is an info message")
# logging.warning("This is a warining message")
# logging.error("This is a error message")
# logging.critical("This is a critical message")


# Log Levels
# Python's logging module has several log levels indicating the severity of events. The default levels are:

# DEBUG: Detailed information, typically of interest only when diagnosing problems.
# INFO: Confirmation that things are working as expected.
# WARNING: An indication that something unexpected happened or indicative of some problem in the near future (e.g., ‘disk space low’). The software is still working as expected.
# ERROR: Due to a more serious problem, the software has not been able to perform some function.
# CRITICAL: A very serious error, indicating that the program itself may be unable to continue running.

## configuring logging
import logging

logging.basicConfig(
    filename='app.log',
    filemode='w',
    level=logging.DEBUG,
    format='%(asctime)s-%(name)s-%(levelname)s-%(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
    )
## log messages with different severity levels
logging.debug("This is a debug message")
logging.info("This is an info message")
logging.warning("This is a warning message")
logging.error("This is an error message")
logging.critical("This is a critical message")


