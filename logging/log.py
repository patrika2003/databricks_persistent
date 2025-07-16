import logging

# Set up basic configuration
logging.basicConfig(level=logging.DEBUG)


# Logging various types of messages
logging.debug("This is a debug message")     # For developers
logging.info("This is an info message")      # General info
logging.warning("This is a warning message") # Something might be wrong
logging.error("This is an error message")    # Something went wrong
logging.critical("This is a critical message") # Serious error
